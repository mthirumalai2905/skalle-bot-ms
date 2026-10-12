"""Plain-text commands people can type in the channel."""

from __future__ import annotations

import re
from dataclasses import dataclass

_LEAD = re.compile(
    r"^(?:hey[,!\s]+|ok[,!\s]+|okay[,!\s]+|please[,!\s]+)?@?skalle\b[\s,!:\-]*",
    re.IGNORECASE,
)
_QUIET = re.compile(
    r"\b(?:quiet|mute|shh|silence|stop talking|don'?t talk|do not talk|shut up|be quiet)\b",
    re.IGNORECASE,
)
_ABOUT = re.compile(r"\b(?:about|regarding)\b", re.IGNORECASE)
_TALK = re.compile(
    r"^(?:please\s+)?(?:you can |start |can you )?(?:talk|speak|unmute|come back)(?:\s+again)?\s*[.!]?\s*$",
    re.IGNORECASE,
)
_STATUS = re.compile(
    r"^(?:please\s+)?(?:status|are you quiet|are you muted|are you there)\s*[?.!]?\s*$",
    re.IGNORECASE,
)
_DURATION = re.compile(
    r"(\d+(?:\.\d+)?)\s*(hours?|hrs?|h|minutes?|mins?|m)\b",
    re.IGNORECASE,
)
_NUMBER = re.compile(r"\b(\d+(?:\.\d+)?)\b")


@dataclass(frozen=True)
class QuietCommand:
    hours: float | None


@dataclass(frozen=True)
class TalkCommand:
    pass


@dataclass(frozen=True)
class StatusCommand:
    pass


ChannelCommand = QuietCommand | TalkCommand | StatusCommand


def parse_hours(text: str) -> float | None:
    match = _DURATION.search(text)
    if match:
        value = float(match.group(1))
        unit = match.group(2).lower()
        if unit.startswith("m"):
            return value / 60.0
        return value
    match = _NUMBER.search(text)
    if match:
        return float(match.group(1))
    return None


def parse_channel_command(text: str) -> ChannelCommand | None:
    stripped = text.strip()
    lead = _LEAD.match(stripped)
    if lead is None:
        return None
    rest = stripped[lead.end() :].strip()
    if _STATUS.fullmatch(rest):
        return StatusCommand()
    if _TALK.fullmatch(rest):
        return TalkCommand()
    if _QUIET.search(rest) and _ABOUT.search(rest) is None:
        return QuietCommand(parse_hours(rest))
    return None
