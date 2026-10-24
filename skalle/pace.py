"""Decide when a channel message is between other people, not for Skalle."""

from __future__ import annotations


def reply_target_id(message: object) -> int | None:
    reference = getattr(message, "reference", None)
    if reference is None:
        return None
    target = getattr(reference, "message_id", None)
    if isinstance(target, int) and target > 0:
        return target
    return None


def mentions_user(message: object, user_id: int | None) -> bool:
    if user_id is None:
        return False
    mentions = getattr(message, "mentions", None) or []
    return any(getattr(person, "id", None) == user_id for person in mentions)


def is_between_other_people(message: object, bot_id: int | None) -> bool:
    """True when this message is a reply to someone other than Skalle."""
    if mentions_user(message, bot_id):
        return False
    target = reply_target_id(message)
    if target is None:
        return False
    resolved = getattr(getattr(message, "reference", None), "resolved", None)
    if resolved is None:
        return True
    author = getattr(resolved, "author", None)
    author_id = getattr(author, "id", None)
    if bot_id is not None and author_id == bot_id:
        return False
    return True
