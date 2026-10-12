"""Tiny HTTP server so a free Render web service can stay awake.

Render sets PORT and checks that the process listens on it. Local runs leave
PORT unset, so this server stays off.
"""

from __future__ import annotations

import logging
import os

from aiohttp import web

log = logging.getLogger(__name__)


async def start_health_server() -> web.AppRunner | None:
    raw_port = os.environ.get("PORT", "").strip()
    if not raw_port:
        return None
    port = int(raw_port)

    async def health(_request: web.Request) -> web.Response:
        return web.Response(text="ok")

    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
    log.info("Health check listening on port %s", port)
    return runner
