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
_PROJECT_ASK = re.compile(
    r"\bwhat(?:'s| is| are) (?:we |you |they |this )?(?:building|gonna do|going to do|going to happen|working on)\b|"
    r"\bwhat are we (?:building|doing)\b|"
    r"\bwhat(?:'s| is) going to happen\b|"
    r"\bwhat(?:'s| is) this (?:server|project|about)\b|"
    r"\bwhat do (?:we|you) (?:do|build)\b|"
    r"\bwhat happens next\b|"
    r"\bwhat is going to happen\b",
    re.IGNORECASE,
)
_PROJECT_FILE = "09-what-we-are-building.md"
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
    blocks: tuple[tuple[str, str], ...]
    pages: tuple[Page, ...]


_BOOK: Book | None = None
_MISSING = False


def asks_for_detail(text: str) -> bool:
    return _DETAIL.search(text) is not None


_ANCHOR = (
    "Synx is not file synchronization. Synx AS makes the Real Time Web tools: "
    "Synx DNS names domains and services, Synx BIOS is the command-line network stack "
    "(not a PC firmware BIOS), and Synx Pass is identity, currently Keycloak. "
    "Morph Space is how people join. This Discord bot cannot create a domain, a Ghost, or a service. "
    "Skalle AI at skalle.ai is the product interface. "
    "Answer from this note. If it defines the term, do not say you cannot place it."
)


def knowledge_note(text: str, *, direct: bool = False, background: str = "") -> str:
    blob = f"{background}\n{text}".strip()
    project = _PROJECT_ASK.search(text) is not None
    if not direct and _TOPIC.search(blob) is None and not project:
        return ""
    book = _book()
    if book is None:
        return ""
    asked = _words(text)
    if background and _TOPIC.search(text) is None:
        asked |= _words(background)
    parts = ["# Public knowledge", _ANCHOR]
    if project:
        brief = _project_article(book)
        if brief:
            parts.append(brief)
    picked = _best_blocks(book.blocks, asked)
    if picked:
        parts.append("Relevant notes:\n\n" + "\n\n".join(picked))
    matched = _matching(book.pages, asked)
    if matched:
        parts.append(
            "Matching pages from the public sites and the older source corpus. "
            "Prefer a 2026 public page when it conflicts with an older note. "
            "Quote a short piece. Do not dump the page.\n\n"
            + matched
        )
    return "\n\n".join(parts)


def _project_article(book: Book) -> str:
    pages = [page for page in book.pages if _PROJECT_FILE in page.also]
    if not pages:
        return ""
    blocks = [f"### {page.title}\n\n{page.body}" for page in pages]
    return (
        "From the knowledge corpus article on what we are building. "
        "Add another essay by editing that file. Do not invent a date.\n\n" + "\n\n".join(blocks)
    )


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
    _BOOK = Book(tuple(_rapid_blocks(rapid)), tuple(pages))
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


def _rapid_blocks(rapid: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for section in re.split(r"\n(?=## )", rapid.strip()):
        section = section.strip()
        if not section:
            continue
        first = section.splitlines()[0]
        heading = first.lstrip("#").strip() if first.startswith("#") else "Note"
        body = section.split("\n", 1)[1].strip() if "\n" in section else ""
        paras = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
        if len(paras) <= 1:
            if len(section) >= 80:
                blocks.append((heading, section[:4000]))
            continue
        for para in paras:
            if len(para) < 40:
                continue
            title = para.split("?", 1)[0].strip() if "?" in para[:90] else heading
            blocks.append((title[:140], para[:4000]))
    return blocks


def _best_blocks(blocks: tuple[tuple[str, str], ...], asked: set[str], limit: int = 4) -> list[str]:
    if not asked:
        return []
    scored: list[tuple[int, str]] = []
    for title, body in blocks:
        score = 4 * len(asked & _words(title)) + len(asked & _words(body[:2500]))
        if score >= 2:
            scored.append((score, body))
    scored.sort(key=lambda item: item[0], reverse=True)
    chosen: list[str] = []
    for _score, body in scored[:limit]:
        chosen.append(_excerpt(body, asked, 1500))
    return chosen


def _matching(pages: tuple[Page, ...], asked: set[str]) -> str:
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
        limit = 800 if page.url.startswith("corpus:") else 1000
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
    cut = max(clipped.rfind(". "), clipped.rfind("\n"))
    if cut > limit // 2:
        return clipped[: cut + 1].rstrip()
    cut = clipped.rfind(" ")
    if cut > limit // 2:
        return clipped[:cut].rstrip() + "…"
    return clipped.rstrip() + "…"


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
