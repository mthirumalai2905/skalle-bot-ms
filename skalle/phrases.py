"""User-facing sentences for quiet mode."""

from __future__ import annotations

from datetime import datetime, timezone


def format_duration(hours: float) -> str:
    if hours < 1:
        minutes = max(1, round(hours * 60))
        unit = "minute" if minutes == 1 else "minutes"
        return f"{minutes} {unit}"
    if abs(hours - round(hours)) < 1e-6:
        whole = int(round(hours))
        unit = "hour" if whole == 1 else "hours"
        return f"{whole} {unit}"
    return f"{hours:.1f} hours"


def format_until(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def quiet_confirmation(hours: float, until: datetime) -> str:
    return (
        f"Alright, I won't talk for {format_duration(hours)}. "
        f"I'm back after {format_until(until)}. "
        "Say `skalle talk` or use `/talk` if you want me sooner."
    )


def talk_confirmation(was_quiet: bool) -> str:
    if was_quiet:
        return "I'm back."
    return "I'm already here."


def status_text(until: datetime | None) -> str:
    if until is None:
        return "I'm listening. Tell me `skalle don't talk for 2 hours` or use `/quiet` if you want the channel to yourselves."
    return f"I'm staying quiet until {format_until(until)}."


def ask_for_hours() -> str:
    return "How many hours? Try `skalle don't talk for 2 hours` or `/quiet`."
