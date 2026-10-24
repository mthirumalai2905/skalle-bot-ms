from datetime import datetime, timezone

from skalle.sites import SiteCache, html_to_text, wants_company_pages


def test_html_keeps_visible_words_and_drops_scripts():
    text = html_to_text("<html><style>body{}</style><script>var x</script><h1>Skalle</h1><p>Preparing for launch</p></html>")
    assert "Skalle" in text
    assert "Preparing for launch" in text
    assert "var x" not in text
    assert "body{}" not in text


def test_a_company_question_asks_for_the_live_pages():
    assert wants_company_pages("what is happening with the launch")
    assert wants_company_pages("what is synx")
    assert not wants_company_pages("lol")
    assert not wants_company_pages("what time is it")


def test_the_note_names_the_fetch_and_hides_a_failed_site():
    cache = SiteCache(urls=("https://synx.tools/", "https://skalle.ai/"))
    assert cache.note() == ""
    cache.pages["https://synx.tools/"] = "Signals from Synx"
    cache.errors["https://skalle.ai/"] = "unavailable"
    cache.fetched_at = datetime(2026, 10, 24, 8, 0, tzinfo=timezone.utc)
    note = cache.note()
    assert "2026-10-24 08:00 UTC" in note
    assert "https://synx.tools/" in note
    assert "Signals from Synx" in note
    assert "https://skalle.ai/" in note
    assert "Unavailable" in note
    assert "Do not invent a launch" in note
