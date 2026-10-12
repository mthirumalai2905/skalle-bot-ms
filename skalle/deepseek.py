"""Short channel replies through the DeepSeek chat API."""

from __future__ import annotations

import re

import httpx

from skalle.config import Settings

SYSTEM_PROMPT = """You are Skalle, the Discord bot in this channel.

Reply only to what the latest message says. Other people's earlier messages are the only background you can use. Your own earlier replies are not facts. If you brought something up and nobody else said it, drop it. If someone says you are wrong, or that there is no link, accept that and answer their actual point.

Never invent a link, site, event, person, or topic that is not in another person's message. Do not guess what the server is for.

Do not open with a greeting unless their latest message is a greeting, and do not repeat a greeting you already used.

If someone asks whether you are an AI or a bot, say that you are Skalle, the bot in this channel.

One to three sentences. Match their language. No @everyone or @here.
"""

_LEADING_NAME = re.compile(r"^skalle\s*:\s*", re.IGNORECASE)


class DeepSeekError(RuntimeError):
    """The model call failed. The message does not include the API key."""


class DeepSeekClient:
    def __init__(self, settings: Settings, transport: httpx.BaseTransport | None = None) -> None:
        self._model = settings.deepseek_model
        self._client = httpx.AsyncClient(
            base_url=settings.deepseek_base_url,
            headers={"Authorization": f"Bearer {settings.deepseek_api_key}"},
            timeout=httpx.Timeout(45.0),
            transport=transport,
        )

    async def aclose(self) -> None:
        await self._client.aclose()

    async def reply(self, history: list[tuple[str, str]]) -> str:
        messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]
        for name, content in history:
            if name == "Skalle":
                messages.append({"role": "assistant", "content": content})
            else:
                messages.append({"role": "user", "content": f"{name}: {content}"})
        try:
            response = await self._client.post(
                "/chat/completions",
                json={
                    "model": self._model,
                    "messages": messages,
                    "max_tokens": 200,
                    "temperature": 0.3,
                    "thinking": {"type": "disabled"},
                },
            )
        except httpx.HTTPError as exc:
            raise DeepSeekError("DeepSeek request failed before a response.") from exc
        if response.status_code >= 400:
            raise DeepSeekError(f"DeepSeek returned HTTP {response.status_code}.")
        try:
            payload = response.json()
            content = payload["choices"][0]["message"].get("content") or ""
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            raise DeepSeekError("DeepSeek returned an unexpected response.") from exc
        return sanitize_reply(str(content))


def sanitize_reply(text: str) -> str:
    cleaned = _LEADING_NAME.sub("", text.strip())
    cleaned = cleaned.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
    if len(cleaned) > 1900:
        cleaned = cleaned[:1899].rstrip() + "…"
    return cleaned
