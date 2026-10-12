from skalle.commands import TalkCommand, parse_channel_command
from skalle.content import see_message


class Box:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def message(content="", **kwargs):
    data = {
        "content": content,
        "clean_content": content,
        "attachments": [],
        "stickers": [],
        "embeds": [],
        "message_snapshots": [],
        "poll": None,
    }
    data.update(kwargs)
    return Box(**data)


def attachment(**kwargs):
    data = {"filename": "file.bin", "content_type": None, "description": None}
    data.update(kwargs)
    return Box(**data)


def test_plain_text_and_unicode_emoji_stay():
    seen = see_message(message("please code urself better 😂"))
    assert seen.speech == "please code urself better 😂"
    assert seen.display == seen.speech


def test_nitro_emoji_becomes_a_name():
    text = "<:kekw:123456789012345678> <a:party_blob:123456789012345679>"
    seen = see_message(message(text))
    assert seen.speech == ":kekw: :party_blob:"
    assert seen.display == seen.speech


def test_image_gif_video_voice_and_file_labels():
    image = see_message(message(attachments=[attachment(filename="meme.png", content_type="image/png")]))
    assert image.speech == ""
    assert image.display == "[image]"

    gif = see_message(message(attachments=[attachment(filename="loop.gif", content_type="image/gif")]))
    assert gif.display == "[gif]"

    video = see_message(message(attachments=[attachment(filename="clip.mp4", content_type="video/mp4")]))
    assert video.display == "[video]"

    voice = see_message(
        message(
            attachments=[
                attachment(
                    filename="voice-message.ogg",
                    content_type="audio/ogg",
                    duration=1.4,
                    waveform=b"\x01",
                )
            ]
        )
    )
    assert voice.display == "[voice message]"

    uploaded = see_message(
        message(attachments=[attachment(filename="@everyone-notes.pdf", content_type="application/pdf")])
    )
    assert uploaded.speech == ""
    assert uploaded.display == "[file: everyone-notes.pdf]"


def test_spoiler_image_and_alt_text():
    seen = see_message(
        message(
            attachments=[
                attachment(
                    filename="SPOILER_meme.png",
                    content_type="image/png",
                    description="the beach one",
                )
            ]
        )
    )
    assert seen.speech == "the beach one"
    assert seen.display == "the beach one [spoiler image]"

    flagged = see_message(
        message(attachments=[attachment(filename="meme.png", content_type="image/png", is_spoiler=lambda: True)])
    )
    assert flagged.display == "[spoiler image]"


def test_caption_counts_and_tenor_gif():
    caption = see_message(
        message(
            "look",
            attachments=[
                attachment(filename="a.png", content_type="image/png"),
                attachment(filename="b.png", content_type="image/png"),
            ],
        )
    )
    assert caption.speech == "look"
    assert caption.display == "look [2 images]"

    tenor = see_message(
        message(
            "lol https://tenor.com/view/nobody-123",
            embeds=[Box(type="gifv", provider=Box(name="Tenor"))],
        )
    )
    assert tenor.speech == "lol"
    assert tenor.display == "lol [gif]"

    bare = see_message(message("https://giphy.com/gifs/abc", embeds=[Box(type="gifv", provider=Box(name="Giphy"))]))
    assert bare.speech == ""
    assert bare.display == "[gif]"


def test_sticker_poll_forward_and_invisible_text():
    sticker = see_message(message(stickers=[Box(name="catJAM")]))
    assert sticker.speech == ""
    assert sticker.display == "[sticker: catJAM]"

    poll = see_message(message("vote", poll=Box(question=Box(text="tacos?"))))
    assert poll.speech == "vote\ntacos?"

    forwarded_text = see_message(message(message_snapshots=[message("hello")]))
    assert forwarded_text.speech == "hello"
    assert forwarded_text.display == "hello [forwarded]"

    forwarded_image = see_message(
        message(message_snapshots=[message(attachments=[attachment(filename="meme.png", content_type="image/png")])])
    )
    assert forwarded_image.speech == ""
    assert forwarded_image.display == "[forwarded] [image]"

    blank = see_message(
        message("\u200b\u200d", attachments=[attachment(filename="meme.png", content_type="image/png")])
    )
    assert blank.speech == ""
    assert blank.display == "[image]"


def test_clean_content_failure_falls_back_and_garbage_does_not_raise():
    class Broken:
        content = "hello <:wave:123456789012345678>"

        @property
        def clean_content(self):
            raise TypeError("content is None")

        attachments = []
        stickers = []
        embeds = []
        message_snapshots = []
        poll = None

    seen = see_message(Broken())
    assert seen.speech == "hello :wave:"

    class Hostile:
        content = "hi"

        @property
        def attachments(self):
            raise RuntimeError("nitro payload")

    hostile = see_message(Hostile())
    assert hostile.speech == "hi"
    assert see_message(object()) == see_message(message(""))


def test_commands_use_words_not_uploads():
    talked = see_message(message("skalle talk", attachments=[attachment(filename="meme.png", content_type="image/png")]))
    assert parse_channel_command(talked.speech) == TalkCommand()

    sticker = see_message(message(stickers=[Box(name="skalle quiet")]))
    assert parse_channel_command(sticker.speech) is None
    assert sticker.display == "[sticker: skalle quiet]"
