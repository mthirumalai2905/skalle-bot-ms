from skalle.interactions import build_interaction_response
from skalle.quiet import QuietStore


CHANNEL = 1556158479188758579


def test_ping_and_quiet_command(tmp_path):
    store = QuietStore(tmp_path / "quiet.json")
    assert build_interaction_response({"type": 1}, store, channel_id=CHANNEL, max_hours=168) == {"type": 1}

    response = build_interaction_response(
        {
            "type": 2,
            "channel_id": str(CHANNEL),
            "data": {"name": "quiet", "options": [{"name": "hours", "value": 2}]},
        },
        store,
        channel_id=CHANNEL,
        max_hours=168,
    )
    assert response["type"] == 4
    assert "2 hours" in response["data"]["content"]
    assert store.is_quiet() is True

    wrong_channel = build_interaction_response(
        {"type": 2, "channel_id": "1", "data": {"name": "talk"}},
        store,
        channel_id=CHANNEL,
        max_hours=168,
    )
    assert wrong_channel["data"]["flags"] == 64
    assert store.is_quiet() is True
