"""Optional HTTP interactions endpoint with ed25519 verification.

Regular messages still arrive on the gateway. Turn this on only when the
Developer Portal Interactions Endpoint URL points at /interactions.
"""

from __future__ import annotations

import json
import logging

from aiohttp import web

from skalle.config import Settings
from skalle.phrases import ask_for_hours, quiet_confirmation, status_text, talk_confirmation
from skalle.quiet import DurationError, QuietStore, validate_hours
from skalle.verify import verify_discord_signature

log = logging.getLogger(__name__)

EPHEMERAL = 64
PING = 1
APPLICATION_COMMAND = 2


def build_interaction_response(
    payload: dict,
    store: QuietStore,
    *,
    channel_id: int,
    max_hours: float,
) -> dict:
    kind = payload.get("type")
    if kind == PING:
        return {"type": PING}
    if kind != APPLICATION_COMMAND:
        return _ephemeral("I don't know that interaction.")

    incoming = _channel_id(payload)
    if incoming != channel_id:
        return _ephemeral("I only listen in my channel.")

    data = payload.get("data") or {}
    name = data.get("name")
    if name == "quiet":
        raw_hours = _option(data, "hours")
        if raw_hours is None:
            return _ephemeral(ask_for_hours())
        try:
            hours = validate_hours(float(raw_hours), max_hours)
        except (TypeError, ValueError, DurationError) as exc:
            text = str(exc) if isinstance(exc, DurationError) else ask_for_hours()
            return _ephemeral(text)
        until = store.set_quiet(hours, max_hours=max_hours)
        return _message(quiet_confirmation(hours, until))
    if name == "talk":
        was_quiet = store.clear()
        return _message(talk_confirmation(was_quiet))
    if name == "status":
        return _message(status_text(store.until()))
    return _ephemeral("I don't know that command.")


async def start_interactions_server(settings: Settings, store: QuietStore) -> web.AppRunner:
    async def handler(request: web.Request) -> web.Response:
        body = await request.read()
        if not verify_discord_signature(
            settings.public_key,
            request.headers.get("X-Signature-Ed25519", ""),
            request.headers.get("X-Signature-Timestamp", ""),
            body,
        ):
            return web.Response(status=401, text="invalid request signature")
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            return web.Response(status=400, text="invalid json")
        if not isinstance(payload, dict):
            return web.Response(status=400, text="invalid json")
        response = build_interaction_response(
            payload,
            store,
            channel_id=settings.channel_id,
            max_hours=settings.max_quiet_hours,
        )
        return web.json_response(response)

    app = web.Application()
    app.router.add_post("/interactions", handler)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, settings.http_host, settings.http_port).start()
    log.info(
        "HTTP interactions listening on %s:%s/interactions",
        settings.http_host,
        settings.http_port,
    )
    return runner


def _channel_id(payload: dict) -> int:
    try:
        return int(payload.get("channel_id") or 0)
    except (TypeError, ValueError):
        return 0


def _option(data: dict, name: str) -> object | None:
    for option in data.get("options") or []:
        if isinstance(option, dict) and option.get("name") == name:
            return option.get("value")
    return None


def _message(content: str) -> dict:
    return {"type": 4, "data": {"content": content}}


def _ephemeral(content: str) -> dict:
    return {"type": 4, "data": {"content": content, "flags": EPHEMERAL}}
