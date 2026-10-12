import asyncio
from datetime import datetime, timezone

import httpx

from skalle.facts import asks_for_code, asks_for_members, live_note, needs_live_facts

NOON = datetime(2026, 10, 12, 12, 0, tzinfo=timezone.utc)
LATE = datetime(2026, 10, 12, 22, 30, tzinfo=timezone.utc)


def _note(text: str, *, now=NOON, members=None, online=None, client=None) -> str:
    return asyncio.run(live_note(text, now=now, members=members, online=online, client=client))


def test_member_questions_use_the_live_count():
    assert asks_for_members("how many members do we have in this group")
    assert not asks_for_members("how many pizzas")
    note = _note("how many members do we have in this group", members=100, online=7)
    assert "Members in this server: 100." in note
    assert "Online members" not in note
    assert "Norway" not in note
    missing = _note("how many members")
    assert "Members in this server: unavailable." in missing
    online = _note("how many members are online", members=100, online=7)
    assert "Online members: 7." in online
    assert "Members in this server" not in online


def test_clock_is_norway_until_someone_asks_for_an_offset():
    note = _note("what time is it")
    assert "Norway (Europe/Oslo): Monday 12 October 2026, 14:00" in note
    assert "Weather" not in note
    ahead = _note("what time is it +4")
    assert "Norway +4: Monday 12 October 2026, 18:00" in ahead
    behind = _note("what time is it 4 hours behind")
    assert "Norway -4: Monday 12 October 2026, 10:00" in behind
    rolled = _note("what day is it -4", now=LATE)
    assert "Norway -4: Monday 12 October 2026, 20:30" in rolled
    assert _note("lol") == ""
    assert needs_live_facts("what year is it")
    assert not needs_live_facts("write a song")


def test_a_named_place_uses_that_clock_and_weather():
    def handler(request: httpx.Request) -> httpx.Response:
        url = str(request.url)
        if "geocoding-api" in url:
            assert request.url.params["name"] == "Tokyo"
            return httpx.Response(
                200,
                json={
                    "results": [
                        {
                            "name": "Tokyo",
                            "country": "Japan",
                            "latitude": 35.68,
                            "longitude": 139.69,
                            "timezone": "Asia/Tokyo",
                        }
                    ]
                },
            )
        raise AssertionError(url)

    transport = httpx.MockTransport(handler)

    async def run():
        async with httpx.AsyncClient(transport=transport) as client:
            return await live_note(
                "what time is it in Tokyo",
                now=NOON,
                members=None,
                online=None,
                client=client,
            )

    note = asyncio.run(run())
    assert "Tokyo, Japan: Monday 12 October 2026, 21:00" in note
    assert "Weather" not in note


def test_weather_defaults_to_oslo_and_can_name_a_place():
    def oslo(request: httpx.Request) -> httpx.Response:
        assert "forecast" in str(request.url)
        assert "geocoding" not in str(request.url)
        assert float(request.url.params["latitude"]) == 59.9139
        return httpx.Response(200, json={"current": {"temperature_2m": 3.2, "weather_code": 3}})

    async def run_oslo():
        async with httpx.AsyncClient(transport=httpx.MockTransport(oslo)) as client:
            return await live_note("what's the weather", now=NOON, members=None, online=None, client=client)

    note = asyncio.run(run_oslo())
    assert "Weather in Oslo, Norway: 3°C, Overcast." in note
    assert "Norway (Europe/Oslo):" not in note

    def bergen(request: httpx.Request) -> httpx.Response:
        if "geocoding-api" in str(request.url):
            assert request.url.params["name"] == "Bergen"
            return httpx.Response(
                200,
                json={
                    "results": [
                        {
                            "name": "Bergen",
                            "country": "Norway",
                            "latitude": 60.39,
                            "longitude": 5.32,
                            "timezone": "Europe/Oslo",
                        }
                    ]
                },
            )
        return httpx.Response(200, json={"current": {"temperature_2m": 8.2, "weather_code": 61}})

    async def run_bergen():
        async with httpx.AsyncClient(transport=httpx.MockTransport(bergen)) as client:
            return await live_note(
                "what's the weather in Bergen today",
                now=NOON,
                members=None,
                online=None,
                client=client,
            )

    named = asyncio.run(run_bergen())
    assert "Weather in Bergen, Norway: 8°C, Rain." in named

    def missing(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"results": []})

    async def run_missing():
        async with httpx.AsyncClient(transport=httpx.MockTransport(missing)) as client:
            return await live_note("weather in Atlantis", now=NOON, members=None, online=None, client=client)

    unknown = asyncio.run(run_missing())
    assert "Weather in Atlantis: unavailable." in unknown
    assert "°C" not in unknown


def test_code_is_only_when_they_ask_for_code():
    assert asks_for_code("write a python function that adds two numbers")
    assert asks_for_code("can you code a script")
    assert asks_for_code("debug this bug")
    assert asks_for_code("```python\nprint(1)\n``` why is this wrong")
    assert not asks_for_code("write a song")
    assert not asks_for_code("I love python")
    assert not asks_for_code("how many members do we have")
