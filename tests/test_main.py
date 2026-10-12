from pathlib import Path

import discord

from main import AlreadyRunning, acquire_single_instance, is_fatal


def test_bad_login_does_not_restart():
    assert is_fatal(KeyboardInterrupt())
    assert is_fatal(SystemExit(1))
    assert is_fatal(discord.PrivilegedIntentsRequired(None))
    assert is_fatal(discord.LoginFailure())
    assert is_fatal(RuntimeError("gateway dropped")) is False


def test_a_second_process_is_told_to_leave(tmp_path: Path):
    first = acquire_single_instance(tmp_path / "skalle.lock")
    try:
        try:
            acquire_single_instance(tmp_path / "skalle.lock")
        except AlreadyRunning:
            pass
        else:
            raise AssertionError("expected AlreadyRunning")
    finally:
        first.close()
