"""Turn a Discord message into text without downloading uploads.

Pictures, GIFs, stickers, voice messages, and Nitro emoji stay as short
labels. Reading a message never raises.
"""

from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import dataclass

log = logging.getLogger(__name__)

_CUSTOM_EMOJI = re.compile(r"<a?:([A-Za-z0-9_]{2,32}):[0-9]{15,22}>")
_GIF_URL = re.compile(
    r"https?://(?:"
    r"(?:www\.)?tenor\.com/\S+"
    r"|c\.tenor\.com/\S+"
    r"|media\.tenor\.com/\S+"
    r"|(?:www\.)?giphy\.com/\S+"
    r"|media\.giphy\.com/\S+"
    r"|gph\.is/\S+"
    r")",
    re.IGNORECASE,
)
_IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".avif"}
_VIDEO_EXT = {".mp4", ".webm", ".mov", ".mkv"}
_AUDIO_EXT = {".mp3", ".wav", ".ogg", ".m4a", ".flac"}
_PLURAL = {
    "image": "images",
    "gif": "gifs",
    "video": "videos",
    "audio": "audio",
    "sticker": "stickers",
    "spoiler image": "spoiler images",
    "spoiler gif": "spoiler gifs",
    "spoiler video": "spoiler videos",
    "spoiler audio": "spoiler audio",
    "voice message": "voice messages",
    "forwarded": "forwarded",
}
_GIF_PROVIDERS = {"tenor", "giphy"}


@dataclass(frozen=True)
class Seen:
    """speech is what the person said. display is speech plus media labels."""

    speech: str
    display: str


def see_message(message: object) -> Seen:
    try:
        return _finish(_parts(message, depth=0))
    except Exception:
        log.exception("Could not read a Discord message")
        return Seen("", "")


def _parts(message: object, depth: int) -> tuple[list[str], list[str]]:
    notes: list[str] = []
    labels: list[str] = []

    content = _tidy(_visible(_strip_gif_urls(_normalize(_message_content(message)))))
    if content:
        notes.append(content)

    for attachment in _as_list(_attr(message, "attachments")):
        label, note = _attachment(attachment)
        if label:
            labels.append(label)
        if note:
            notes.append(note)

    for sticker in _as_list(_attr(message, "stickers")):
        labels.append(_sticker_label(sticker))

    if _has_gif_embed(message) and not _already_gif(labels):
        labels.append("gif")

    poll = _poll_text(message)
    if poll:
        notes.append(poll)

    if depth < 1:
        for snapshot in _as_list(_attr(message, "message_snapshots")):
            inner_notes, inner_labels = _parts(snapshot, depth=1)
            if not inner_notes and not inner_labels:
                continue
            if "forwarded" not in labels:
                labels.append("forwarded")
            notes.extend(inner_notes)
            labels.extend(inner_labels)

    return notes, labels


def _finish(parts: tuple[list[str], list[str]]) -> Seen:
    notes, labels = parts
    speech = "\n".join(dict.fromkeys(note for note in notes if note))
    media = _format_labels(labels)
    if speech and media:
        display = f"{speech} {media}"
    else:
        display = speech or media
    return Seen(speech, display)


def _message_content(message: object) -> str:
    raw = _string_attr(message, "content")
    try:
        cleaned = getattr(message, "clean_content")
    except Exception:
        cleaned = None
    if not isinstance(cleaned, str):
        return raw
    if cleaned.strip():
        return cleaned
    return raw or cleaned


def _normalize(text: str) -> str:
    return _CUSTOM_EMOJI.sub(lambda match: f":{match.group(1)}:", text)


def _strip_gif_urls(text: str) -> str:
    return _GIF_URL.sub(" ", text)


def _visible(text: str) -> str:
    kept: list[str] = []
    for char in text:
        category = unicodedata.category(char)
        if category == "Cf":
            continue
        if category == "Cc" and char not in "\n\t":
            continue
        kept.append(char)
    return "".join(kept)


def _tidy(text: str) -> str:
    lines = [" ".join(line.split()) for line in text.splitlines()]
    return "\n".join(line for line in lines if line).strip()


def _attachment(attachment: object) -> tuple[str, str]:
    kind = "voice message" if _is_voice(attachment) else _file_kind(attachment)
    note = _safe_phrase(_string_attr(attachment, "description"), 200)
    spoiler = _is_spoiler(attachment)
    if kind == "file":
        name = _safe_phrase(_string_attr(attachment, "filename"), 60) or "file"
        label = f"file: {name}"
        if spoiler:
            label = f"spoiler {label}"
        return label, note
    if spoiler:
        return f"spoiler {kind}", note
    return kind, note


def _file_kind(attachment: object) -> str:
    content_type = _string_attr(attachment, "content_type").lower().split(";", 1)[0].strip()
    filename = _string_attr(attachment, "filename").lower()
    ext = filename[filename.rfind(".") :] if "." in filename else ""
    if content_type == "image/gif" or ext == ".gif":
        return "gif"
    if content_type.startswith("image/") or ext in _IMAGE_EXT:
        return "image"
    if content_type.startswith("video/") or ext in _VIDEO_EXT:
        return "video"
    if content_type.startswith("audio/") or ext in _AUDIO_EXT:
        return "audio"
    return "file"


def _is_spoiler(attachment: object) -> bool:
    method = getattr(attachment, "is_spoiler", None)
    if callable(method):
        try:
            if method():
                return True
        except Exception:
            pass
    return _string_attr(attachment, "filename").upper().startswith("SPOILER_")


def _is_voice(attachment: object) -> bool:
    method = getattr(attachment, "is_voice_message", None)
    if callable(method):
        try:
            return bool(method())
        except Exception:
            pass
    duration = _attr(attachment, "duration")
    waveform = _attr(attachment, "waveform")
    return duration is not None and waveform is not None


def _sticker_label(sticker: object) -> str:
    name = _safe_phrase(_string_attr(sticker, "name"), 40)
    if not name:
        return "sticker"
    return f"sticker: {name}"


def _has_gif_embed(message: object) -> bool:
    for embed in _as_list(_attr(message, "embeds")):
        kind, provider = _embed_names(embed)
        if kind == "gifv" or provider.lower() in _GIF_PROVIDERS:
            return True
    return False


def _embed_names(embed: object) -> tuple[str, str]:
    try:
        if isinstance(embed, dict):
            provider = embed.get("provider") or {}
            provider_name = provider.get("name") if isinstance(provider, dict) else ""
            return str(embed.get("type") or "").lower(), str(provider_name or "")
        return str(getattr(embed, "type", "") or "").lower(), _provider_name(embed)
    except Exception:
        return "", ""


def _provider_name(embed: object) -> str:
    provider = getattr(embed, "provider", None)
    if provider is None:
        return ""
    if isinstance(provider, dict):
        return str(provider.get("name") or "")
    try:
        return str(getattr(provider, "name", "") or "")
    except Exception:
        return ""


def _already_gif(labels: list[str]) -> bool:
    return any(label == "gif" or label.endswith(" gif") for label in labels)


def _poll_text(message: object) -> str:
    poll = _attr(message, "poll")
    if poll is None:
        return ""
    question = _attr(poll, "question")
    if isinstance(question, str):
        return _safe_phrase(question, 200)
    if question is None:
        return ""
    return _safe_phrase(_string_attr(question, "text"), 200)


def _format_labels(labels: list[str]) -> str:
    order: list[str] = []
    counts: dict[str, int] = {}
    for label in labels:
        if label not in counts:
            order.append(label)
            counts[label] = 0
        counts[label] += 1
    parts: list[str] = []
    for label in order:
        count = counts[label]
        plural = _PLURAL.get(label)
        if plural is None or count == 1:
            parts.append(" ".join(f"[{label}]" for _ in range(count)))
        else:
            parts.append(f"[{count} {plural}]")
    return " ".join(parts)


def _safe_phrase(value: str, limit: int) -> str:
    cleaned = value.replace("@everyone", "everyone").replace("@here", "here")
    cleaned = cleaned.replace("[", "(").replace("]", ")")
    cleaned = " ".join(_visible(cleaned).split())
    if not cleaned:
        return ""
    if len(cleaned) > limit:
        return cleaned[: limit - 1].rstrip() + "…"
    return cleaned


def _string_attr(obj: object, name: str) -> str:
    value = _attr(obj, name)
    if isinstance(value, str):
        return value
    return ""


def _attr(obj: object, name: str) -> object:
    try:
        return getattr(obj, name, None)
    except Exception:
        return None


def _as_list(value: object) -> list[object]:
    if not value or isinstance(value, (str, bytes)):
        return []
    try:
        return list(value)  # type: ignore[arg-type]
    except TypeError:
        return []
