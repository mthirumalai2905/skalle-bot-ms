"""Fresh text from the three company sites.

A stored prompt goes stale. Skalle rereads these pages on a schedule and
treats that fetch as the newest company news.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from html.parser import HTMLParser

import httpx

log = logging.getLogger(__name__)

COMPANY_URLS = (
    "https://synx.tools/",
    "https://www.realtimeweb.org/",
    "https://www.realtimeweb.org/blog",
    "https://skalle.ai/",
)
_PAGE_LIMIT = 1600
_SKIP_TAGS = {"script", "style", "noscript", "svg"}
_LIVE = re.compile(
    r"synx\.tools|realtimeweb\.org|skalle\.ai|"
    r"\b(?:synx|skalle|real[-\s]?time\s+web)\b|"
    r"\bwhat(?:'s| is) happening\b|\bcompany\b|\blaunch\b|\bnews\b|"
    r"what are we building|going to happen|working on",
    re.IGNORECASE,
)


class SiteCache:
    def __init__(self, urls: tuple[str, ...] = COMPANY_URLS) -> None:
        self.urls = urls
        self.pages: dict[str, str] = {}
        self.errors: dict[str, str] = {}
        self.fetched_at: datetime | None = None

    def note(self) -> str:
        if self.fetched_at is None and not self.pages and not self.errors:
            return ""
        when = "not yet" if self.fetched_at is None else self.fetched_at.strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            "Live company pages. This is the newest fetch of https://synx.tools/, "
            "https://www.realtimeweb.org/ (including /blog), and https://skalle.ai/. "
            f"Fetched {when}. Prefer this over older essays when they disagree. "
            "If a status is not written here, say you have not seen it on these sites. "
            "Do not invent a launch, a price, a date, or a product.",
        ]
        for url in self.urls:
            if url in self.pages:
                lines.append(f"### {url}\n{self.pages[url]}")
            elif url in self.errors:
                lines.append(f"### {url}\nUnavailable at this fetch.")
        return "\n\n".join(lines)

    async def refresh(self) -> None:
        async with httpx.AsyncClient(
            timeout=httpx.Timeout(20.0),
            follow_redirects=True,
            headers={"User-Agent": "SkalleBot/1.0"},
        ) as client:
            for url in self.urls:
                try:
                    response = await client.get(url)
                    response.raise_for_status()
                    text = html_to_text(response.text)[:_PAGE_LIMIT]
                    if text:
                        self.pages[url] = text
                        self.errors.pop(url, None)
                    else:
                        self.errors[url] = "empty"
                except (httpx.HTTPError, ValueError):
                    log.warning("Could not refresh %s", url)
                    self.errors[url] = "unavailable"
        self.fetched_at = datetime.now(timezone.utc)

    async def watch(self, interval_seconds: int = 6 * 60 * 60) -> None:
        while True:
            await self.refresh()
            await asyncio_sleep(interval_seconds)


def wants_company_pages(text: str) -> bool:
    return _LIVE.search(text) is not None


def html_to_text(html: str) -> str:
    parser = _TextExtractor()
    parser.feed(html)
    parser.close()
    lines: list[str] = []
    for part in parser.parts:
        if not lines or lines[-1] != part:
            lines.append(part)
    return "\n".join(lines)


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _SKIP_TAGS:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in _SKIP_TAGS and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if self._skip:
            return
        text = " ".join(data.split())
        if text:
            self.parts.append(text)


async def asyncio_sleep(seconds: int) -> None:
    import asyncio

    await asyncio.sleep(seconds)
