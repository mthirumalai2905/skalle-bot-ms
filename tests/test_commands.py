from skalle.commands import QuietCommand, StatusCommand, TalkCommand, parse_channel_command, parse_hours


def test_quiet_phrases():
    assert parse_channel_command("skalle don't talk for 2 hours") == QuietCommand(2)
    assert parse_channel_command("skalle dont talk for 3 hours") == QuietCommand(3)
    assert parse_channel_command("skalle quiet 4h") == QuietCommand(4)
    assert parse_channel_command("@Skalle shut up for 90 minutes") == QuietCommand(1.5)
    assert parse_channel_command("please skalle, be quiet") == QuietCommand(None)
    assert parse_channel_command("hey skalle mute 1 hour") == QuietCommand(1)


def test_other_commands_and_normal_chat():
    assert parse_channel_command("skalle talk") == TalkCommand()
    assert parse_channel_command("skalle, you can talk") == TalkCommand()
    assert parse_channel_command("skalle status") == StatusCommand()
    assert parse_channel_command("skalle talk about pizza") is None
    assert parse_channel_command("skalle don't talk about the movie") is None
    assert parse_channel_command("hey skalle what's going on") is None
    assert parse_channel_command("someone said skalle quiet 2 hours") is None


def test_parse_hours_units():
    assert parse_hours("for 2 hours") == 2
    assert parse_hours("30m") == 0.5
    assert parse_hours("no number") is None
