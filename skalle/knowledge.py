"""Public pages the bot may use when someone asks, or in a direct message.

The file leads with short answers. Matching page text is added only for the
question in front of us, so a reply does not have to carry every article.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from skalle.config import ROOT

KNOWLEDGE_PATH = ROOT / "knowledge" / "network.md"
CORPUS_DIR = ROOT / "knowledge" / "corpus"
_SOURCE = "\n## SOURCE NOTES\n"
_PAGE = "\n### PAGE\n"
_EACH = 4200
_MASTER_EACH = 1600

_TOPIC = re.compile(
    r"real[-\s]?time\s+web|realtimeweb|\brtw\b|\bsynx\b|skalle\.ai|"
    r"\bskalle\s+ai\b|morphic|morph\s+space|\bghosts?\b|ghost\s*space|"
    r"kerneliz|micropage|\bbijective\b|data\s+channels?|\bnornir\b|oslobygg|"
    r"\bpaal\b|\blevang\b|\bthiru\b|silverkant|superintelligence|"
    r"training\s+dataset|friend\s+or\s+foe|last\s+it\s+project|"
    r"internet\s+for\s+machines|two\s+webs|\bntnu\b|synx\s+pass|synx\s+bios|synx\s+dns|"
    r"\bkeycloak\b|micropayment|hive collective|synx hive|\bhive\b|\bbins\b|"
    r"bijective network|\bcioty\b|synx-cat|synx cat|synxpass|maskinen|synaptic technologies",
    re.IGNORECASE,
)
_DETAIL = re.compile(
    r"\b(?:in detail|more detail|full detail|elaborate|go deeper|longer explanation)\b|"
    r"\bexplain (?:this |it |that )?(?:to me )?(?:in )?detail\b|"
    r"\b(?:give|show) (?:me )?(?:an |some )?(?:example|examples|analogy|analogies)\b",
    re.IGNORECASE,
)
_STOP = {
    "about",
    "after",
    "also",
    "because",
    "been",
    "before",
    "being",
    "could",
    "does",
    "from",
    "have",
    "into",
    "just",
    "like",
    "more",
    "only",
    "over",
    "some",
    "than",
    "that",
    "them",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "very",
    "what",
    "when",
    "where",
    "which",
    "with",
    "would",
    "your",
}


@dataclass(frozen=True)
class Page:
    url: str
    title: str
    also: tuple[str, ...]
    body: str


@dataclass(frozen=True)
class Book:
    rapid: str
    pages: tuple[Page, ...]


_BOOK: Book | None = None
_MISSING = False


def asks_for_detail(text: str) -> bool:
    return _DETAIL.search(text) is not None


def knowledge_note(text: str, *, direct: bool = False) -> str:
    if not direct and _TOPIC.search(text) is None:
        return ""
    book = _book()
    if book is None:
        return ""
    parts = [book.rapid]
    matched = _matching(book.pages, text)
    if matched:
        parts.append(
            "Matching pages from the public sites and the older source corpus. "
            "Prefer a 2026 public page when it conflicts with an older note. "
            "Quote a short piece. Do not dump the page.\n\n"
            + matched
        )
    return "\n\n".join(parts)


def _book() -> Book | None:
    global _BOOK, _MISSING
    if _BOOK is not None:
        return _BOOK
    if _MISSING or not KNOWLEDGE_PATH.is_file():
        _MISSING = True
        return None
    text = KNOWLEDGE_PATH.read_text(encoding="utf-8")
    rapid, _, _after_index = text.partition("\n## PAGE INDEX\n")
    _, _, source = text.partition(_SOURCE)
    rapid = rapid.strip()
    if not rapid:
        _MISSING = True
        return None
    pages = _pages(source)
    pages.extend(_corpus_pages())
    _BOOK = Book(rapid, tuple(pages))
    return _BOOK


def _pages(source: str) -> list[Page]:
    pages: list[Page] = []
    for chunk in source.split(_PAGE):
        if "url: " not in chunk:
            continue
        lines = chunk.strip().splitlines()
        url = ""
        title = ""
        also: list[str] = []
        body_at = len(lines)
        for index, line in enumerate(lines):
            if line.startswith("url: "):
                url = line[5:].strip()
            elif line.startswith("also: "):
                also.append(line[6:].strip())
            elif line.startswith("title: "):
                title = line[7:].strip()
            elif line == "":
                body_at = index + 1
                break
        body = "\n".join(lines[body_at:]).strip()
        if url and body:
            pages.append(Page(url, title, tuple(also), body))
    return pages


def _matching(pages: tuple[Page, ...], text: str) -> str:
    asked = _words(text)
    if not asked:
        return ""
    scored: list[tuple[int, Page]] = []
    for page in pages:
        label = _words(f"{page.title} {page.url} {' '.join(page.also)}")
        score = 4 * len(asked & label) + len(asked & _words(page.body))
        if score >= 3:
            scored.append((score, page))
    scored.sort(key=lambda item: item[0], reverse=True)
    public = [page for _score, page in scored if not page.url.startswith("corpus:")]
    older = [page for _score, page in scored if page.url.startswith("corpus:")]
    chosen: list[Page] = []
    if public:
        chosen.append(public[0])
    if older:
        chosen.append(older[0])
    elif len(public) > 1:
        chosen.append(public[1])
    blocks: list[str] = []
    for page in chosen:
        limit = _MASTER_EACH if page.url.startswith("corpus:") else _EACH
        body = _excerpt(page.body, asked, limit)
        urls = page.url
        if page.also:
            urls += " (also " + ", ".join(page.also) + ")"
        blocks.append(f"### {page.title}\n{urls}\n\n{body}")
    return "\n\n".join(blocks)


def _corpus_pages() -> list[Page]:
    if not CORPUS_DIR.is_dir():
        return []
    pages: list[Page] = []
    for path in sorted(CORPUS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "aToken_e72a41abb3f2f66b6e1366d03ac55d55646a212c18023798086530dae9026370",
            "aToken_<your SynxPass token>",
        )
        title = path.stem
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        pages.extend(_sections(title, text, path.name))
    return pages


def _sections(doc_title: str, body: str, filename: str) -> list[Page]:
    pages: list[Page] = []
    for chunk in re.split(r"\n(?=## )", body.strip()):
        chunk = chunk.strip()
        if len(chunk) < 120:
            continue
        first = chunk.splitlines()[0]
        heading = first.lstrip("#").strip() if first.startswith("#") else doc_title
        slug = re.sub(r"[^a-z0-9]+", "-", f"{filename} {heading}".lower()).strip("-")[:90]
        pages.append(Page(f"corpus:{slug}", f"{doc_title} — {heading}", (filename,), chunk[:14000]))
    return pages


def _excerpt(body: str, asked: set[str], limit: int) -> str:
    lower = body.lower()
    start = 0
    for word in sorted(asked, key=len, reverse=True):
        at = lower.find(word)
        if at > 400:
            start = max(0, at - 240)
            break
    snippet = body[start:]
    if len(snippet) <= limit:
        return snippet
    clipped = snippet[:limit]
    if "\n" in clipped:
        clipped = clipped.rsplit("\n", 1)[0]
    return clipped.rstrip() + "\n…"


_KEEP = {"bins", "cat", "iot", "ioe", "mad", "rtw"}


def _words(text: str) -> set[str]:
    folded = text.lower().replace("-", " ")
    words: set[str] = set()
    for word in re.findall(r"[a-z0-9]+", folded):
        if word in _STOP or word.isdigit():
            continue
        if len(word) >= 4 or word in _KEEP:
            words.add(word)
    return words
