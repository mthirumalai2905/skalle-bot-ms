"""Live facts Skalle may use only when someone asks.

The clock is Norway (Europe/Oslo). A +4 or -4 in the question shifts that
clock. Weather defaults to Oslo, and a named place uses that place instead.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import httpx

NORWAY = ZoneInfo("Europe/Oslo")
OSLO_LATITUDE = 59.9139
OSLO_LONGITUDE = 10.7522

_MEMBER_QUESTION = re.compile(
    r"\bhow many members\b"
    r"|\bhow many (?:people|users) (?:are )?(?:here|in|on)\b"
    r"|\bhow many of us\b"
    r"|\bmember count\b"
    r"|\bhow (?:big|large) is (?:this |the |our )?(?:server|group|guild|discord)\b"
    r"|\bhow many\b.{0,40}\b(?:server|group|guild)\b"
    r"|\bhow many\b.{0,30}\bonline\b",
    re.IGNORECASE | re.DOTALL,
)
_ONLINE = re.compile(r"\bonline\b", re.IGNORECASE)
_TOTAL = re.compile(
    r"\b(?:members?|member count|people|users|of us|server size|group size|how (?:big|large))\b",
    re.IGNORECASE,
)
_ONLINE_ONLY = re.compile(
    r"\b(?:members?|people|users)\b.{0,24}\bonline\b|\bonline\b.{0,24}\b(?:members?|people|users)\b",
    re.IGNORECASE | re.DOTALL,
)
_CLOCK = re.compile(
    r"\bwhat time is it\b"
    r"|\bwhat(?:'s| is) the time\b"
    r"|\bcurrent time\b"
    r"|\btell me the time\b"
    r"|\btime (?:now|in|at)\b"
    r"|\bwhat day is it\b"
    r"|\bwhat(?:'s| is) (?:the )?day today\b"
    r"|\bwhat(?:'s| is) today\b"
    r"|\bwhat(?:'s| is) the date\b"
    r"|\btoday'?s date\b"
    r"|\bwhat month is it\b"
    r"|\bwhat year is it\b"
    r"|\bwhat year are we in\b"
    r"|\bwhich (?:day|month|year) is it\b"
    r"|\bdate (?:today|now|in|at)\b",
    re.IGNORECASE,
)
_WEATHER = re.compile(
    r"\bweather\b"
    r"|\bforecast\b"
    r"|\bhow (?:hot|cold|warm) is it\b"
    r"|\bis it (?:raining|snowing)\b"
    r"|\btemperature outside\b",
    re.IGNORECASE,
)
_PLACE = re.compile(
    r"\b(?:weather|forecast|temperature|time|date|day)\b"
    r"(?:\s+\w+){0,6}?\s+\b(?:in|at)\s+"
    r"([A-Za-z][A-Za-z.'\-]*(?:\s+[A-Za-z][A-Za-z.'\-]*){0,2})",
    re.IGNORECASE,
)
_TRAIL = re.compile(
    r"(?:\s+\b(?:today|now|please|rn|tonight|currently|outside|like)\b)+\s*$",
    re.IGNORECASE,
)
_NOT_A_PLACE = {
    "norway",
    "here",
    "there",
    "real",
    "sure",
    "me",
    "us",
    "you",
    "fun",
    "once",
    "now",
    "today",
    "tonight",
    "later",
    "home",
    "bed",
    "work",
    "school",
    "general",
    "discord",
}
_SIGNED_OFFSET = re.compile(
    r"(?:^|\s)([+-])\s*(\d{1,2})(?:\s*(?:h|hrs?|hours?))?(?=\s|$|[?.!,])",
    re.IGNORECASE,
)
_WORD_OFFSET = re.compile(
    r"\b(\d{1,2})\s*hours?\s+(ahead|behind|forward|back)\b",
    re.IGNORECASE,
)
_CODE_DIRECT = re.compile(
    r"\b(?:can you code|write code|help me code|coding problem|programming problem|leetcode)\b",
    re.IGNORECASE,
)
_CODE_VERB = re.compile(
    r"\b(?:write|code|implement|debug|fix|solve|program|refactor)\b",
    re.IGNORECASE,
)
_CODE_NOUN = re.compile(
    r"\b(?:code|script|function|program|class|bug|algorithm|python|javascript|typescript|java|rust|golang|sql|c\+\+|programming|snippet)\b",
    re.IGNORECASE,
)
_CODE_FENCE_ASK = re.compile(r"\b(?:fix|debug|why|help|wrong|error|bug)\b", re.IGNORECASE)
_WEATHER_TEXT = {
    0: "Clear",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Fog",
    51: "Drizzle",
    53: "Drizzle",
    55: "Drizzle",
    56: "Freezing drizzle",
    57: "Freezing drizzle",
    61: "Rain",
    63: "Rain",
    65: "Rain",
    66: "Freezing rain",
    67: "Freezing rain",
    71: "Snow",
    73: "Snow",
    75: "Snow",
    77: "Snow",
    80: "Rain showers",
    81: "Rain showers",
    82: "Rain showers",
    85: "Snow showers",
    86: "Snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm",
    99: "Thunderstorm",
}

_FACTS_HEADER = (
    "Live facts for this reply only. They asked, so you may use these. "
    "Say every number and time exactly. If a fact says unavailable, say you cannot see it and do not guess."
)


@dataclass(frozen=True)
class Place:
    label: str
    latitude: float
    longitude: float
    timezone: str


OSLO = Place("Oslo, Norway", OSLO_LATITUDE, OSLO_LONGITUDE, "Europe/Oslo")


def asks_for_members(text: str) -> bool:
    return _MEMBER_QUESTION.search(text) is not None


def asks_for_clock(text: str) -> bool:
    return _CLOCK.search(text) is not None


def asks_for_weather(text: str) -> bool:
    return _WEATHER.search(text) is not None


def asks_for_code(text: str) -> bool:
    if _CODE_DIRECT.search(text):
        return True
    if "```" in text and _CODE_FENCE_ASK.search(text):
        return True
    return _CODE_VERB.search(text) is not None and _CODE_NOUN.search(text) is not None


def needs_live_facts(text: str) -> bool:
    return asks_for_members(text) or asks_for_clock(text) or asks_for_weather(text)


def parse_place(text: str) -> str | None:
    match = _PLACE.search(text)
    if match is None:
        return None
    raw = _TRAIL.sub("", match.group(1).strip(" .,-!?'\"")).strip(" .,-!?'\"")
    if not raw:
        return None
    key = raw.lower()
    if key in _NOT_A_PLACE or key.startswith("this ") or key.startswith("the "):
        return None
    return raw


def parse_offset(text: str) -> int | None:
    word = _WORD_OFFSET.search(text)
    if word:
        parsed = _signed_hours(int(word.group(1)), word.group(2))
        if parsed is not None:
            return parsed
    signed = _SIGNED_OFFSET.search(text)
    if signed is None:
        return None
    hours = int(signed.group(2))
    if signed.group(1) == "-":
        hours = -hours
    if abs(hours) > 14:
        return None
    return hours


async def live_note(
    text: str,
    *,
    now: datetime,
    members: int | None,
    online: int | None,
    client: httpx.AsyncClient | None = None,
) -> str:
    if not needs_live_facts(text):
        return ""
    lines = [_FACTS_HEADER]
    if asks_for_members(text):
        lines.extend(_member_lines(text, members, online))
    need_clock = asks_for_clock(text)
    need_weather = asks_for_weather(text)
    place_name = parse_place(text) if need_clock or need_weather else None
    offset = parse_offset(text) if need_clock and place_name is None else None
    own_client = False
    if client is None and (place_name or need_weather):
        client = httpx.AsyncClient(timeout=httpx.Timeout(8.0))
        own_client = True
    try:
        resolved: Place | None = None
        missing_place = False
        if place_name:
            if client is None:
                missing_place = True
            else:
                resolved = await find_place(place_name, client)
                missing_place = resolved is None
        if need_clock:
            lines.append(_clock_fact(now, offset, resolved, place_name if missing_place else None))
        if need_weather:
            if missing_place or client is None:
                lines.append(f"Weather in {place_name or OSLO.label}: unavailable.")
            else:
                lines.append(await weather_fact(resolved or OSLO, client))
    finally:
        if own_client and client is not None:
            await client.aclose()
    return "\n".join(lines)


async def find_place(name: str, client: httpx.AsyncClient) -> Place | None:
    try:
        response = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": name, "count": 1, "language": "en", "format": "json"},
        )
        if response.status_code != 200:
            return None
        results = response.json().get("results") or []
    except (httpx.HTTPError, ValueError, TypeError, AttributeError):
        return None
    if not isinstance(results, list) or not results or not isinstance(results[0], dict):
        return None
    item = results[0]
    try:
        latitude = float(item["latitude"])
        longitude = float(item["longitude"])
    except (KeyError, TypeError, ValueError):
        return None
    zone_name = str(item.get("timezone") or "")
    if _zone(zone_name) is None:
        return None
    city = str(item.get("name") or name).strip()
    country = str(item.get("country") or "").strip()
    label = f"{city}, {country}" if country else city
    return Place(label, latitude, longitude, zone_name)


async def weather_fact(place: Place, client: httpx.AsyncClient) -> str:
    try:
        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": place.latitude,
                "longitude": place.longitude,
                "current": "temperature_2m,weather_code",
                "timezone": place.timezone,
            },
        )
        if response.status_code != 200:
            raise ValueError(response.status_code)
        current = response.json().get("current") or {}
        temperature = round(float(current["temperature_2m"]))
        code = int(current["weather_code"])
    except (httpx.HTTPError, ValueError, TypeError, KeyError):
        return f"Weather in {place.label}: unavailable."
    condition = _WEATHER_TEXT.get(code, "unlisted conditions")
    return f"Weather in {place.label}: {temperature}°C, {condition}."


def _member_lines(text: str, members: int | None, online: int | None) -> list[str]:
    online_question = _ONLINE.search(text) is not None
    total_question = _TOTAL.search(text) is not None or not online_question
    if online_question and _ONLINE_ONLY.search(text):
        total_question = False
    lines: list[str] = []
    if total_question:
        lines.append(_count_line("Members in this server", members))
    if online_question:
        lines.append(_count_line("Online members", online))
    return lines


def _count_line(label: str, value: int | None) -> str:
    if value is None:
        return f"{label}: unavailable."
    return f"{label}: {value}."


def _clock_fact(
    now: datetime,
    offset: int | None,
    place: Place | None,
    missing_name: str | None,
) -> str:
    if missing_name:
        return f"Clock for {missing_name}: unavailable."
    moment = _as_utc(now)
    if place is not None:
        zone = _zone(place.timezone)
        if zone is None:
            return f"Clock for {place.label}: unavailable."
        return _format_when(moment.astimezone(zone), place.label)
    hours = offset or 0
    local = moment.astimezone(NORWAY) + timedelta(hours=hours)
    return _format_when(local, _norway_label(hours))


def _format_when(moment: datetime, label: str) -> str:
    clock = moment.strftime("%H:%M")
    return f"{label}: {moment.strftime('%A')} {moment.day} {moment.strftime('%B %Y')}, {clock}"


def _norway_label(hours: int) -> str:
    if hours > 0:
        return f"Norway +{hours}"
    if hours < 0:
        return f"Norway {hours}"
    return "Norway (Europe/Oslo)"


def _signed_hours(hours: int, direction: str) -> int | None:
    if hours > 14:
        return None
    if direction.lower() in {"behind", "back"}:
        return -hours
    return hours


def _as_utc(now: datetime) -> datetime:
    if now.tzinfo is None:
        return now.replace(tzinfo=timezone.utc)
    return now.astimezone(timezone.utc)


def _zone(name: str) -> ZoneInfo | None:
    try:
        return ZoneInfo(name)
    except Exception:
        return None
