"""Environment configuration. Credentials are never hardcoded."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from nacl.exceptions import CryptoError
from nacl.signing import VerifyKey

from skalle.quiet import MAX_QUIET_HOURS

ROOT = Path(__file__).resolve().parent.parent

TOKEN_HELP = """DISCORD_BOT_TOKEN is not set.

The public key is not a bot token. Discord only shows the token in the Developer Portal:

1. Open https://discord.com/developers/applications/1559040703592661102/bot
2. In the Bot section, click Reset Token and copy the new token. Discord shows it once.
3. Put it in .env on its own line: DISCORD_BOT_TOKEN=the-token-you-copied
4. On that same Bot page, turn on Message Content Intent under Privileged Gateway Intents, then save.
5. Invite Skalle with this URL, then authorize it on your server:
   https://discord.com/oauth2/authorize?client_id=1559040703592661102&permissions=68608&scope=bot%20applications.commands
6. Leave the Interactions Endpoint URL empty. Skalle listens through the gateway.
7. From this folder, run: python main.py

Keep .env on this machine. Do not commit it or paste the token into chat.
"""


class ConfigError(Exception):
    """The process cannot start with the current environment."""


@dataclass(frozen=True)
class Settings:
    application_id: int
    public_key: str
    bot_token: str
    channel_id: int
    deepseek_api_key: str
    deepseek_base_url: str
    deepseek_model: str
    enable_http_interactions: bool
    http_host: str
    http_port: int
    max_history: int
    max_quiet_hours: float
    quiet_path: Path


def load_settings(env_file: Path | None = ROOT / ".env") -> Settings:
    if env_file is not None and env_file.exists():
        load_dotenv(env_file, override=False)

    application_id = _snowflake("DISCORD_APPLICATION_ID", _required("DISCORD_APPLICATION_ID"))
    public_key = _public_key(_required("DISCORD_PUBLIC_KEY"))
    bot_token = _bot_token(os.environ.get("DISCORD_BOT_TOKEN", ""), public_key)
    channel_id = _snowflake("DISCORD_CHANNEL_ID", _required("DISCORD_CHANNEL_ID"))
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise ConfigError(
            "DEEPSEEK_API_KEY is not set. Create one at https://platform.deepseek.com/api_keys "
            "and store it only in .env."
        )

    max_history = _int("MAX_HISTORY", 12, minimum=1, maximum=30)
    max_quiet = _float("MAX_QUIET_HOURS", MAX_QUIET_HOURS, minimum=0.25, maximum=168)
    http_port = _int("HTTP_INTERACTIONS_PORT", 8080, minimum=1, maximum=65535)
    return Settings(
        application_id=application_id,
        public_key=public_key,
        bot_token=bot_token,
        channel_id=channel_id,
        deepseek_api_key=api_key,
        deepseek_base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").strip().rstrip("/"),
        deepseek_model=os.environ.get("DEEPSEEK_MODEL", "deepseek-flash").strip() or "deepseek-flash",
        enable_http_interactions=_bool("ENABLE_HTTP_INTERACTIONS", False),
        http_host=os.environ.get("HTTP_INTERACTIONS_HOST", "0.0.0.0").strip() or "0.0.0.0",
        http_port=http_port,
        max_history=max_history,
        max_quiet_hours=max_quiet,
        quiet_path=ROOT / "data" / "quiet.json",
    )


def _required(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise ConfigError(f"{name} is not set. Add it to .env.")
    return value


def _snowflake(name: str, value: str) -> int:
    if not value.isdigit():
        raise ConfigError(f"{name} must be a numeric Discord id.")
    number = int(value)
    if number <= 0:
        raise ConfigError(f"{name} must be a numeric Discord id.")
    return number


def _public_key(value: str) -> str:
    key = value.strip().lower()
    if len(key) != 64 or any(char not in "0123456789abcdef" for char in key):
        raise ConfigError(
            "DISCORD_PUBLIC_KEY must be the 64-character hex key from the application page. "
            "It is not the bot token."
        )
    try:
        VerifyKey(bytes.fromhex(key))
    except (ValueError, CryptoError) as exc:
        raise ConfigError("DISCORD_PUBLIC_KEY is not a valid ed25519 public key.") from exc
    return key


def _bot_token(value: str, public_key: str) -> str:
    token = value.strip()
    if not token:
        raise ConfigError(TOKEN_HELP)
    if token.lower() == public_key or (
        len(token) == 64 and all(char in "0123456789abcdefABCDEF" for char in token)
    ):
        raise ConfigError(
            "DISCORD_BOT_TOKEN is set to the public key. That key cannot log the bot in. "
            "Reset the bot token on the Bot page of the Developer Portal and put that value in .env."
        )
    return token


def _bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _int(name: str, default: int, *, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be an integer.") from exc
    if value < minimum or value > maximum:
        raise ConfigError(f"{name} must be between {minimum} and {maximum}.")
    return value


def _float(name: str, default: float, *, minimum: float, maximum: float) -> float:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be a number.") from exc
    if value < minimum or value > maximum:
        raise ConfigError(f"{name} must be between {minimum:g} and {maximum:g}.")
    return value
