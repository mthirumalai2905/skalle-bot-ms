"""How long Skalle stays silent, including across restarts."""

from __future__ import annotations

import json
import logging
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = logging.getLogger(__name__)

MAX_QUIET_HOURS = 168.0


class DurationError(ValueError):
    """The requested quiet period is outside the allowed range."""


def validate_hours(hours: float, max_hours: float = MAX_QUIET_HOURS) -> float:
    if hours != hours or hours in (float("inf"), float("-inf")):
        raise DurationError("Tell me a real number of hours.")
    if hours <= 0:
        raise DurationError("Tell me more than 0 hours.")
    if hours > max_hours:
        raise DurationError(f"I can stay quiet for up to {max_hours:g} hours.")
    return hours


class QuietStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = threading.Lock()
        self._until = self._read()

    def until(self) -> datetime | None:
        with self._lock:
            if self._until is not None and self._until <= datetime.now(timezone.utc):
                self._until = None
                self._write(None)
            return self._until

    def is_quiet(self) -> bool:
        return self.until() is not None

    def set_quiet(self, hours: float, *, max_hours: float = MAX_QUIET_HOURS) -> datetime:
        hours = validate_hours(hours, max_hours)
        until = datetime.now(timezone.utc) + timedelta(hours=hours)
        with self._lock:
            self._until = until
            self._write(until)
        return until

    def clear(self) -> bool:
        with self._lock:
            was_quiet = self._until is not None and self._until > datetime.now(timezone.utc)
            self._until = None
            self._write(None)
            return was_quiet

    def _read(self) -> datetime | None:
        if not self.path.exists():
            return None
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
            raw = payload.get("until")
            if not raw:
                return None
            moment = datetime.fromisoformat(raw)
        except (OSError, json.JSONDecodeError, TypeError, ValueError):
            log.warning("Ignoring unreadable quiet state at %s", self.path)
            return None
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=timezone.utc)
        if moment <= datetime.now(timezone.utc):
            return None
        return moment.astimezone(timezone.utc)

    def _write(self, until: datetime | None) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"until": until.isoformat() if until is not None else None}
        temporary = self.path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(self.path)
