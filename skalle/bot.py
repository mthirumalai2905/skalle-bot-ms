"""Gateway bot: reply in one channel, and stay quiet when asked."""

from __future__ import annotations

import asyncio
import logging

import discord
from discord import app_commands

from skalle.commands import QuietCommand, StatusCommand, TalkCommand, parse_channel_command
from skalle.config import Settings
from skalle.content import see_message
from skalle.deepseek import DeepSeekClient, DeepSeekError
from skalle.phrases import ask_for_hours, quiet_confirmation, status_text, talk_confirmation
from skalle.quiet import DurationError, QuietStore

log = logging.getLogger(__name__)


class SkalleBot(discord.Client):
    def __init__(self, settings: Settings, store: QuietStore, deepseek: DeepSeekClient) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents, application_id=settings.application_id)
        self.settings = settings
        self.store = store
        self.deepseek = deepseek
        self.tree = app_commands.CommandTree(self)
        self._queue: asyncio.Queue[discord.Message] = asyncio.Queue()
        self._worker: asyncio.Task[None] | None = None
        self._synced = False
        self._register_commands()

    async def setup_hook(self) -> None:
        self._worker = asyncio.create_task(self._reply_worker())

    async def close(self) -> None:
        if self._worker is not None:
            self._worker.cancel()
            try:
                await self._worker
            except asyncio.CancelledError:
                pass
        await super().close()

    async def on_ready(self) -> None:
        log.info("Logged in as %s", self.user)
        await self._sync_commands()
        log.info("Listening in channel %s", self.settings.channel_id)

    async def on_message(self, message: discord.Message) -> None:
        try:
            author_is_bot = message.author.bot
            guild = message.guild
            channel_id = message.channel.id
        except Exception:
            log.exception("Could not read a channel message")
            return
        if author_is_bot or guild is None:
            return
        if channel_id != self.settings.channel_id:
            return
        seen = see_message(message)
        command = parse_channel_command(seen.speech)
        if command is not None:
            await self._handle_text_command(message, command)
            return
        if self.store.is_quiet() or not seen.speech:
            return
        await self._queue.put(message)

    async def _handle_text_command(self, message: discord.Message, command: object) -> None:
        if isinstance(command, StatusCommand):
            await self._send(message, status_text(self.store.until()))
            return
        if isinstance(command, TalkCommand):
            was_quiet = self.store.clear()
            await self._send(message, talk_confirmation(was_quiet))
            return
        if isinstance(command, QuietCommand):
            if command.hours is None:
                await self._send(message, ask_for_hours())
                return
            try:
                until = self.store.set_quiet(command.hours, max_hours=self.settings.max_quiet_hours)
            except DurationError as exc:
                await self._send(message, str(exc))
                return
            await self._send(message, quiet_confirmation(command.hours, until))

    async def _reply_worker(self) -> None:
        while True:
            message = await self._queue.get()
            try:
                if not self.store.is_quiet():
                    await self._reply(message)
                    await asyncio.sleep(1)
            except asyncio.CancelledError:
                raise
            except Exception:
                log.exception("Could not answer a channel message")
            finally:
                self._queue.task_done()

    async def _reply(self, message: discord.Message) -> None:
        seen = see_message(message)
        if not seen.speech:
            return
        history = await self._history(message)
        current = seen.display[:800]
        if current:
            history.append((self._speaker(message), current))
        if not history:
            return
        try:
            async with message.channel.typing():
                text = await self.deepseek.reply(history)
        except DeepSeekError as exc:
            log.warning("%s", exc)
            text = "I lost that thought. Say it again?"
        if not text:
            return
        await message.reply(
            text,
            mention_author=False,
            allowed_mentions=discord.AllowedMentions.none(),
        )

    async def _history(self, message: discord.Message) -> list[tuple[str, str]]:
        items: list[tuple[str, str]] = []
        try:
            async for older in message.channel.history(
                limit=self.settings.max_history,
                before=message,
                oldest_first=True,
            ):
                item = self._history_item(older)
                if item is not None:
                    items.append(item)
        except Exception:
            log.exception("Could not read channel history")
        return items

    def _history_item(self, older: discord.Message) -> tuple[str, str] | None:
        try:
            author = older.author
            if author.bot and (self.user is None or author.id != self.user.id):
                return None
            seen = see_message(older)
            if not seen.display:
                return None
            return (self._speaker(older), seen.display[:800])
        except Exception:
            log.exception("Skipping a channel message")
            return None

    def _speaker(self, message: discord.Message) -> str:
        try:
            if self.user is not None and message.author.id == self.user.id:
                return "Skalle"
            name = message.author.display_name
        except Exception:
            return "Someone"
        if not isinstance(name, str) or not name.strip():
            return "Someone"
        return " ".join(name.split())[:80]

    async def _sync_commands(self) -> None:
        if self._synced:
            return
        channel = self.get_channel(self.settings.channel_id)
        if channel is None:
            try:
                channel = await self.fetch_channel(self.settings.channel_id)
            except discord.HTTPException:
                log.warning(
                    "Cannot see channel %s yet. Invite the bot and grant View Channel, then restart.",
                    self.settings.channel_id,
                )
                await self.tree.sync()
                self._synced = True
                return
        guild = getattr(channel, "guild", None)
        if guild is None:
            await self.tree.sync()
            self._synced = True
            return
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        self._synced = True
        log.info("Synced slash commands to guild %s", guild.id)

    async def _send(self, message: discord.Message, content: str) -> None:
        await message.reply(
            content,
            mention_author=False,
            allowed_mentions=discord.AllowedMentions.none(),
        )

    def _register_commands(self) -> None:
        settings = self.settings
        store = self.store

        @self.tree.command(name="quiet", description="Tell Skalle to stay quiet for a number of hours")
        @app_commands.describe(hours="How many hours Skalle should stay quiet")
        async def quiet(interaction: discord.Interaction, hours: float) -> None:
            if not _in_channel(interaction, settings.channel_id):
                await interaction.response.send_message("I only listen in my channel.", ephemeral=True)
                return
            try:
                until = store.set_quiet(hours, max_hours=settings.max_quiet_hours)
            except DurationError as exc:
                await interaction.response.send_message(str(exc), ephemeral=True)
                return
            await interaction.response.send_message(quiet_confirmation(hours, until))

        @self.tree.command(name="talk", description="Let Skalle talk in the channel again")
        async def talk(interaction: discord.Interaction) -> None:
            if not _in_channel(interaction, settings.channel_id):
                await interaction.response.send_message("I only listen in my channel.", ephemeral=True)
                return
            was_quiet = store.clear()
            await interaction.response.send_message(talk_confirmation(was_quiet))

        @self.tree.command(name="status", description="See whether Skalle is quiet")
        async def status(interaction: discord.Interaction) -> None:
            if not _in_channel(interaction, settings.channel_id):
                await interaction.response.send_message("I only listen in my channel.", ephemeral=True)
                return
            await interaction.response.send_message(status_text(store.until()))


def _in_channel(interaction: discord.Interaction, channel_id: int) -> bool:
    return interaction.channel_id == channel_id
