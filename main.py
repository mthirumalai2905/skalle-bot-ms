"""Run Skalle."""

from __future__ import annotations

import asyncio
import logging
import sys

import discord

from skalle.bot import SkalleBot
from skalle.config import ConfigError, Settings, load_settings
from skalle.deepseek import DeepSeekClient
from skalle.interactions import start_interactions_server
from skalle.quiet import QuietStore


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    try:
        settings = load_settings()
    except ConfigError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from None
    try:
        asyncio.run(run(settings))
    except KeyboardInterrupt:
        pass
    except discord.PrivilegedIntentsRequired:
        print(
            "Discord rejected the gateway connection because Message Content Intent is off. "
            "Open the Bot page for this application, enable Message Content Intent, save, and start again.",
            file=sys.stderr,
        )
        raise SystemExit(1) from None
    except discord.LoginFailure:
        print(
            "Discord rejected DISCORD_BOT_TOKEN. Reset the token on the Bot page and update .env. "
            "The public key cannot be used as the token.",
            file=sys.stderr,
        )
        raise SystemExit(1) from None


async def run(settings: Settings) -> None:
    store = QuietStore(settings.quiet_path)
    deepseek = DeepSeekClient(settings)
    bot = SkalleBot(settings, store, deepseek)
    runner = None
    if settings.enable_http_interactions:
        runner = await start_interactions_server(settings, store)
    try:
        await bot.start(settings.bot_token)
    finally:
        await deepseek.aclose()
        if runner is not None:
            await runner.cleanup()


if __name__ == "__main__":
    main()
