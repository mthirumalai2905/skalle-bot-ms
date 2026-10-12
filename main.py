"""Run Skalle."""

from __future__ import annotations

import asyncio
import logging
import os
import sys
import time
from pathlib import Path

import discord

from skalle.bot import SkalleBot
from skalle.config import ROOT, ConfigError, Settings, load_settings
from skalle.deepseek import DeepSeekClient
from skalle.health import start_health_server
from skalle.interactions import start_interactions_server
from skalle.quiet import QuietStore

log = logging.getLogger(__name__)

_LOCK: object | None = None


class AlreadyRunning(Exception):
    """Another Skalle process already holds the lock."""


def is_fatal(exc: BaseException) -> bool:
    """These exits need a person. Everything else should start Skalle again."""
    return isinstance(exc, (KeyboardInterrupt, SystemExit, discord.PrivilegedIntentsRequired, discord.LoginFailure))


def acquire_single_instance(path: Path):
    """Hold an exclusive lock until this process exits."""
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = open(path, "a+b")
    try:
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        handle.close()
        raise AlreadyRunning from exc
    return handle


def main() -> None:
    global _LOCK
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
        _LOCK = acquire_single_instance(ROOT / "data" / "skalle.lock")
    except AlreadyRunning:
        print("Skalle is already running.", file=sys.stderr)
        raise SystemExit(0) from None

    delay = 5
    while True:
        started = time.monotonic()
        try:
            asyncio.run(run(settings))
        except BaseException as exc:
            if isinstance(exc, discord.PrivilegedIntentsRequired):
                print(
                    "Discord rejected the gateway connection because Message Content Intent is off. "
                    "Open the Bot page for this application, enable Message Content Intent, save, and start again.",
                    file=sys.stderr,
                )
                raise SystemExit(1) from None
            if isinstance(exc, discord.LoginFailure):
                print(
                    "Discord rejected DISCORD_BOT_TOKEN. Reset the token on the Bot page and update .env. "
                    "The public key cannot be used as the token.",
                    file=sys.stderr,
                )
                raise SystemExit(1) from None
            if is_fatal(exc):
                return
            log.exception("Skalle stopped unexpectedly.")
        else:
            log.error("Discord connection ended.")
        if time.monotonic() - started >= 60:
            delay = 5
        else:
            delay = min(delay * 2, 60)
        log.info("Starting Skalle again in %s seconds.", delay)
        time.sleep(delay)


async def run(settings: Settings) -> None:
    store = QuietStore(settings.quiet_path)
    deepseek = DeepSeekClient(settings)
    bot = SkalleBot(settings, store, deepseek)
    runner = None
    if settings.enable_http_interactions:
        runner = await start_interactions_server(settings, store)
    health = await start_health_server()
    try:
        await bot.start(settings.bot_token)
    finally:
        await deepseek.aclose()
        if runner is not None:
            await runner.cleanup()
        if health is not None:
            await health.cleanup()


if __name__ == "__main__":
    main()
