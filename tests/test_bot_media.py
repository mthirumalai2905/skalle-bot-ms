import asyncio

from skalle.bot import SkalleBot
from skalle.config import Settings
from skalle.quiet import QuietStore


class Box:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Typing:
    async def __aenter__(self):
        return None

    async def __aexit__(self, *_args):
        return False


class Channel:
    def __init__(self, channel_id, pages):
        self.id = channel_id
        self.pages = pages

    def history(self, **_kwargs):
        pages = self.pages

        async def generate():
            for item in pages:
                if isinstance(item, BaseException):
                    raise item
                yield item

        return generate()

    def typing(self):
        return Typing()


def settings(tmp_path):
    return Settings(
        application_id=1,
        public_key="ab" * 32,
        bot_token="placeholder.token.value",
        channel_id=99,
        deepseek_api_key="test-key",
        deepseek_base_url="https://api.deepseek.com",
        deepseek_model="deepseek-flash",
        enable_http_interactions=False,
        http_host="127.0.0.1",
        http_port=8080,
        max_history=12,
        max_quiet_hours=72,
        quiet_path=tmp_path / "quiet.json",
    )


def person(name, user_id):
    return Box(bot=False, id=user_id, display_name=name)


def upload(filename, content_type):
    return Box(filename=filename, content_type=content_type, description=None)


def posted(channel, author, content="", attachments=None, stickers=None):
    replies = []

    async def reply(text, **_kwargs):
        replies.append(text)

    message = Box(
        author=author,
        guild=Box(),
        channel=channel,
        content=content,
        clean_content=content,
        attachments=attachments or [],
        stickers=stickers or [],
        embeds=[],
        message_snapshots=[],
        poll=None,
        reply=reply,
    )
    message.replies = replies
    return message


def test_uploads_do_not_stop_the_next_reply(tmp_path):
    async def scenario():
        store = QuietStore(tmp_path / "quiet.json")
        deepseek = Box()

        async def reply(history, note="", coding=False):
            deepseek.history = history
            deepseek.note = note
            deepseek.coding = coding
            return "yeah"

        deepseek.reply = reply
        bot = SkalleBot(settings(tmp_path), store, deepseek)
        try:
            channel = Channel(99, [])
            image = posted(channel, person("JoMama", 5), attachments=[upload("meme.png", "image/png")])
            emoji = posted(channel, person("Thiru", 6), content="<:kekw:123456789012345678>")
            sticker = posted(channel, person("JoMama", 5), stickers=[Box(name="catJAM")])
            lol = posted(channel, person("Thiru", 6), content="lol")

            await bot.on_message(image)
            await bot.on_message(emoji)
            await bot.on_message(sticker)
            await bot.on_message(lol)

            assert bot._queue.qsize() == 2
            queued = []
            while not bot._queue.empty():
                queued.append(await bot._queue.get())
            assert [item.content for item in queued] == ["<:kekw:123456789012345678>", "lol"]

            image_then_crash = posted(
                Channel(99, [image, RuntimeError("bad attachment")]),
                person("JoMama", 5),
                attachments=[upload("meme.png", "image/png")],
            )
            channel = Channel(99, [image_then_crash, RuntimeError("bad attachment")])
            lol.channel = channel
            await bot._reply(lol)
            assert deepseek.history[0] == ("JoMama", "[image]")
            assert deepseek.history[-1] == ("Thiru", "lol")
            assert lol.replies == ["yeah"]

            crashed = Channel(99, [RuntimeError("bad attachment")])
            again = posted(crashed, person("Thiru", 6), content="lol")
            await bot._reply(again)
            assert deepseek.history == [("Thiru", "lol")]
            assert again.replies == ["yeah"]
            assert deepseek.note == ""
            assert deepseek.coding is False
        finally:
            await bot.close()

    asyncio.run(scenario())


def test_a_command_still_works_beside_an_image(tmp_path):
    async def scenario():
        bot = SkalleBot(settings(tmp_path), QuietStore(tmp_path / "quiet.json"), Box())
        try:
            channel = Channel(99, [])
            message = posted(channel, person("Thiru", 6), content="skalle talk", attachments=[upload("meme.png", "image/png")])
            await bot.on_message(message)
            assert message.replies == ["I'm already here."]
            assert bot._queue.qsize() == 0
        finally:
            await bot.close()

    asyncio.run(scenario())


def test_member_count_clock_and_code_are_passed_through(tmp_path):
    async def scenario():
        deepseek = Box()

        async def reply(history, note="", coding=False):
            deepseek.history = history
            deepseek.note = note
            deepseek.coding = coding
            return "ok"

        deepseek.reply = reply
        bot = SkalleBot(settings(tmp_path), QuietStore(tmp_path / "quiet.json"), deepseek)

        async def fetch_guild(guild_id, with_counts=False):
            deepseek.fetched = (guild_id, with_counts)
            return Box(approximate_member_count=100, approximate_presence_count=7, member_count=99)

        bot.fetch_guild = fetch_guild
        try:
            channel = Channel(99, [])
            members = posted(channel, person("Thiru", 6), content="how many members do we have in this group")
            members.guild = Box(id=5, member_count=3)
            await bot._reply(members)
            assert deepseek.fetched == (5, True)
            assert "Members in this server: 100." in deepseek.note
            assert "Online members" not in deepseek.note
            assert "Norway" not in deepseek.note
            assert deepseek.coding is False

            online = posted(channel, person("Thiru", 6), content="how many members are online")
            online.guild = Box(id=5)
            await bot._reply(online)
            assert "Online members: 7." in deepseek.note
            assert "Members in this server" not in deepseek.note

            clock = posted(channel, person("Thiru", 6), content="what time is it")
            await bot._reply(clock)
            assert "Norway (Europe/Oslo):" in deepseek.note
            assert "Members" not in deepseek.note

            code = posted(channel, person("Thiru", 6), content="write a python function that adds two numbers")
            await bot._reply(code)
            assert deepseek.coding is True
            assert deepseek.note == ""

            async def broken_fetch(guild_id, with_counts=False):
                raise RuntimeError("portal down")

            bot.fetch_guild = broken_fetch
            fallback = posted(channel, person("Thiru", 6), content="how many members")
            fallback.guild = Box(id=5, member_count=42)
            await bot._reply(fallback)
            assert "Members in this server: 42." in deepseek.note
        finally:
            await bot.close()

    asyncio.run(scenario())
