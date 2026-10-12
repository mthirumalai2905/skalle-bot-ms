"""Short channel replies through the DeepSeek chat API."""

from __future__ import annotations

import re

import httpx

from skalle.config import Settings

SYSTEM_PROMPT = """You are Skalle, the Discord bot in this channel. Sound like a person in the group, not a help desk. Be funny when it fits, and skip the joke when it does not. Encourage someone who is trying, stuck, or sharing a win. Roast only when they are joking or the vibe is playful, and keep the roast light. You are still a bot. If someone asks whether you are an AI or a bot, say that you are Skalle, the bot in this channel.

Reply only to what the latest message says. Other people's earlier messages are the only background you can use. Your own earlier replies are not facts. If you brought something up and nobody else said it, drop it. If someone says you are wrong, or that there is no link, accept that and answer their actual point.

Never invent a link, site, event, person, or topic that is not in another person's message. Do not guess what the server is for.

Labels in square brackets, such as [image], [gif], [video], [voice message], [sticker: name], and [forwarded], mean they shared that. You cannot see pictures or hear audio. Do not guess what is in them. A word in colons, such as :name:, is a custom emoji.

Never start a reply with "Morning", "Good morning", or any other greeting. The time of day is not a reason to greet. Start with the answer.

Answer general knowledge when they ask a direct question. Do not volunteer extra facts. Do not bring up the time, the date, the weather, the member count, or code unless they asked. When a live facts note is included below, say those numbers and times exactly. If a fact says unavailable, say you cannot see it. Do not invent a count, a clock, or a forecast.

For a normal message, one to three sentences. Do not write code unless they explicitly asked you to code or to solve a programming problem. Match their language. No @everyone or @here.
"""

_CODE_NOTE = (
    "They explicitly asked for code. Write the code in a markdown block and one short comment. "
    "The one-to-three-sentence limit does not apply to this reply."
)
_CHAT_TOKENS = 200
_CODE_TOKENS = 700

_LEADING_NAME = re.compile(r"^skalle\s*:\s*", re.IGNORECASE)
_LEADING_GREETING = re.compile(r"^(?:good\s+)?morning\b[.!,:\-]*\s*", re.IGNORECASE)


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

    async def reply(self, history: list[tuple[str, str]], *, note: str = "", coding: bool = False) -> str:
        messages: list[dict[str, str]] = [{"role": "system", "content": _instructions(note, coding)}]
        for name, content in history:
            if name == "Skalle":
                earlier = strip_leading_greeting(content)
                if earlier:
                    messages.append({"role": "assistant", "content": earlier})
            else:
                messages.append({"role": "user", "content": f"{name}: {content}"})
        try:
            response = await self._client.post(
                "/chat/completions",
                json={
                    "model": self._model,
                    "messages": messages,
                    "max_tokens": _CODE_TOKENS if coding else _CHAT_TOKENS,
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
        return sanitize_reply(str(content), coding=coding)


def _instructions(note: str, coding: bool) -> str:
    parts = [SYSTEM_PROMPT]
    if note.strip():
        parts.append(note.strip())
    if coding:
        parts.append(_CODE_NOTE)
    return "\n\n".join(parts)


def strip_leading_greeting(text: str) -> str:
    cleaned = text.strip()
    while True:
        stripped = _LEADING_GREETING.sub("", cleaned, count=1).strip()
        if stripped == cleaned:
            return cleaned
        cleaned = stripped


def sanitize_reply(text: str, *, coding: bool = False) -> str:
    cleaned = strip_leading_greeting(_LEADING_NAME.sub("", text.strip()))
    cleaned = cleaned.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
    if len(cleaned) <= 1900:
        return cleaned
    if not coding:
        return cleaned[:1899].rstrip() + "…"
    clipped = cleaned[:1900]
    if "\n" in clipped:
        clipped = clipped.rsplit("\n", 1)[0]
    closer = "\n```"
    if clipped.count("```") % 2 == 1 and len(clipped) + len(closer) <= 2000:
        clipped += closer
    return clipped
