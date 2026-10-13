from skalle.deepseek import sanitize_reply
from skalle.knowledge import asks_for_detail, knowledge_note


def test_channel_chat_stays_free_of_the_knowledge_file():
    assert knowledge_note("lol") == ""
    assert knowledge_note("what time is it") == ""


def test_a_network_question_includes_the_short_answers_and_a_page():
    note = knowledge_note("what is a ghost on the real time web")
    assert note.startswith("# Public knowledge")
    assert "bijective" in note.lower()
    assert "https://realtimeweb.org" in note
    assert "Matching pages" in note
    assert "SOURCE NOTES" not in note


def test_a_direct_message_has_the_short_answers_even_for_a_greeting():
    note = knowledge_note("hey", direct=True)
    assert "Skalle AI" in note
    assert "Synx" in note
    assert "Matching pages" not in note


def test_detail_is_only_an_explicit_ask():
    assert asks_for_detail("explain this in detail")
    assert asks_for_detail("can you give me an analogy")
    assert not asks_for_detail("what is a ghost")
    assert not asks_for_detail("for example the lamp")


def test_a_direct_message_is_clipped_unless_they_asked_for_detail():
    long = "One.\nTwo.\nThree.\nFour.\nFive.\nSix."
    assert sanitize_reply(long, direct=True) == "One.\nTwo.\nThree."
    assert sanitize_reply(long, direct=True, detail=True).count("\n") == 4


def test_a_hive_question_pulls_the_older_corpus():
    note = knowledge_note("what is the nornir hive collective", direct=True)
    assert "corpus:" in note
    assert "intranet" in note.lower() or "private" in note.lower()


def test_an_article_question_pulls_that_essay():
    note = knowledge_note("are we raising a superintelligence to be a narcissist", direct=True)
    assert "Five traps" in note or "parenting" in note.lower()
    assert "raising-a-superintelligence" in note
