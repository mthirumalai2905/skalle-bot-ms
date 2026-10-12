import json

import httpx

from skalle.config import ROOT, ConfigError, load_settings
from skalle.deepseek import DeepSeekClient, sanitize_reply


def _settings(monkeypatch):
    monkeypatch.setenv("DISCORD_APPLICATION_ID", "1559040703592661102")
    monkeypatch.setenv("DISCORD_PUBLIC_KEY", "0994483824edc1d739e9185a9825223026a9526a9d0e693d34d518c38a7c30e2")
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "placeholder.token.value")
    monkeypatch.setenv("DISCORD_CHANNEL_ID", "1556158479188758579")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    monkeypatch.setenv("DEEPSEEK_MODEL", "deepseek-flash")
    monkeypatch.setenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    return load_settings(env_file=None)


def test_missing_token_explains_the_portal(monkeypatch):
    monkeypatch.setenv("DISCORD_APPLICATION_ID", "1559040703592661102")
    monkeypatch.setenv("DISCORD_PUBLIC_KEY", "0994483824edc1d739e9185a9825223026a9526a9d0e693d34d518c38a7c30e2")
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "")
    monkeypatch.setenv("DISCORD_CHANNEL_ID", "1556158479188758579")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    try:
        load_settings(env_file=None)
    except ConfigError as exc:
        text = str(exc)
    else:
        raise AssertionError("expected ConfigError")
    assert "Developer Portal" in text
    assert "public key is not a bot token" in text
    assert "placeholder" not in text


def test_public_key_is_rejected_as_token(monkeypatch):
    monkeypatch.setenv("DISCORD_APPLICATION_ID", "1559040703592661102")
    monkeypatch.setenv("DISCORD_PUBLIC_KEY", "0994483824edc1d739e9185a9825223026a9526a9d0e693d34d518c38a7c30e2")
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "0994483824edc1d739e9185a9825223026a9526a9d0e693d34d518c38a7c30e2")
    monkeypatch.setenv("DISCORD_CHANNEL_ID", "1556158479188758579")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    try:
        load_settings(env_file=None)
    except ConfigError as exc:
        assert "public key" in str(exc).lower()
    else:
        raise AssertionError("expected ConfigError")


def test_project_env_has_the_application_ids(monkeypatch):
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "placeholder.token.value")
    settings = load_settings()
    assert settings.application_id == 1559040703592661102
    assert settings.public_key == "0994483824edc1d739e9185a9825223026a9526a9d0e693d34d518c38a7c30e2"
    assert settings.channel_id == 1556158479188758579
    assert settings.deepseek_model == "deepseek-flash"
    assert settings.bot_token == "placeholder.token.value"
    assert settings.enable_http_interactions is False


def test_source_does_not_hardcode_an_api_key():
    files = list((ROOT / "skalle").glob("*.py"))
    files.append(ROOT / "main.py")
    for path in files:
        assert "sk-" not in path.read_text(encoding="utf-8"), path.name


def test_deepseek_reply_disables_thinking(monkeypatch):
    settings = _settings(monkeypatch)
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["auth"] = request.headers["Authorization"]
        seen["body"] = json.loads(request.content)
        return httpx.Response(200, json={"choices": [{"message": {"content": "Skalle: hey"}}]})

    client = DeepSeekClient(settings, transport=httpx.MockTransport(handler))
    import asyncio

    text = asyncio.run(client.reply([("Ada", "hello")]))
    assert text == "hey"
    assert seen["auth"] == "Bearer test-key"
    assert seen["body"]["model"] == "deepseek-flash"
    assert seen["body"]["temperature"] == 0.3
    assert seen["body"]["max_tokens"] == 200
    assert "Live facts" not in seen["body"]["messages"][0]["content"]
    assert "one to three sentences" in seen["body"]["messages"][0]["content"]
    assert "Never invent" in seen["body"]["messages"][0]["content"]
    assert "You cannot see pictures" in seen["body"]["messages"][0]["content"]
    assert seen["body"]["thinking"] == {"type": "disabled"}
    assert seen["body"]["messages"][1] == {"role": "user", "content": "Ada: hello"}


def test_live_facts_and_code_change_the_request(monkeypatch):
    settings = _settings(monkeypatch)
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content)
        return httpx.Response(200, json={"choices": [{"message": {"content": "here"}}]})

    client = DeepSeekClient(settings, transport=httpx.MockTransport(handler))
    import asyncio

    asyncio.run(client.reply([("Ada", "write a python function")], note="Members in this server: 100.", coding=True))
    system = seen["body"]["messages"][0]["content"]
    assert "Members in this server: 100." in system
    assert "markdown block" in system
    assert seen["body"]["max_tokens"] == 700


def test_sanitize_reply_limits_length_and_mentions():
    assert sanitize_reply("Morning. I can write code, yeah.") == "I can write code, yeah."
    assert sanitize_reply("Good morning, Thiru just said bye.") == "Thiru just said bye."
    assert sanitize_reply("I'm already here.") == "I'm already here."
    assert sanitize_reply("  Skalle: hi @everyone ") == "hi @\u200beveryone"
    assert sanitize_reply("x" * 2000).endswith("…")
    assert len(sanitize_reply("x" * 2000)) == 1900
    code = "```python\n" + ("print(1)\n" * 400)
    clipped = sanitize_reply(code, coding=True)
    assert clipped.count("```") % 2 == 0
    assert len(clipped) <= 2000
    assert not clipped.endswith("…")
