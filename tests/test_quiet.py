from datetime import datetime, timedelta, timezone

from skalle.phrases import format_duration, quiet_confirmation
from skalle.quiet import DurationError, QuietStore, validate_hours


def test_validate_hours():
    assert validate_hours(2) == 2
    try:
        validate_hours(0)
    except DurationError as exc:
        assert "0" in str(exc)
    else:
        raise AssertionError("expected DurationError")
    try:
        validate_hours(200)
    except DurationError:
        pass
    else:
        raise AssertionError("expected DurationError")


def test_quiet_store_round_trip(tmp_path):
    store = QuietStore(tmp_path / "quiet.json")
    assert store.is_quiet() is False
    until = store.set_quiet(2)
    assert store.is_quiet() is True
    assert until > datetime.now(timezone.utc)

    restored = QuietStore(tmp_path / "quiet.json")
    assert restored.is_quiet() is True
    assert restored.clear() is True
    assert QuietStore(tmp_path / "quiet.json").is_quiet() is False


def test_expired_quiet_is_cleared(tmp_path):
    path = tmp_path / "quiet.json"
    store = QuietStore(path)
    store.set_quiet(1)
    store._until = datetime.now(timezone.utc) - timedelta(minutes=1)
    store._write(store._until)
    assert QuietStore(path).is_quiet() is False


def test_confirmation_mentions_duration():
    until = datetime(2026, 10, 12, 12, 0, tzinfo=timezone.utc)
    text = quiet_confirmation(2, until)
    assert "2 hours" in text
    assert "2026-10-12 12:00 UTC" in text
    assert format_duration(0.5) == "30 minutes"
