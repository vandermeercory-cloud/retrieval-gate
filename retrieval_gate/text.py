"""Tokens, document identity, and the items a document mentions."""
from __future__ import annotations

import re

WORD = re.compile(r"[a-zA-Z][a-zA-Z0-9_-]{2,}")
# Deliberately small. A long stoplist removes the vocabulary short queries are made of.
STOP = frozenset({"and", "the", "for", "that", "with", "from", "this", "are", "not", "into", "its"})
MENTION = re.compile(r"\bPEP[\s-]*(\d{1,4})\b", re.IGNORECASE)
# PEPs cite each other three ways: in prose ("PEP 634"), with the
# reStructuredText role (:pep:`634`, :pep:`the spec <634#syntax>`), and in
# header fields (Requires: 634). Most citations use the role, so a parser that
# only reads prose lets most of them through an exclusion.
ROLE = re.compile(r":pep:`(?:[^`<]*<)?\s*(\d{1,4})")
HEADER_REFERENCE = re.compile(r"^(?:Requires|Replaces|Superseded-By):\s*(.+)$", re.MULTILINE | re.IGNORECASE)
STATUS = re.compile(r"^Status:\s*(.+?)\s*$", re.MULTILINE)
TITLE = re.compile(r"^Title:\s*(.+?)\s*$", re.MULTILINE)
UNDERLINE = re.compile(r"([=\-~^\"'`#*+.:_])\1{2,}")
HEADER_SPAN = 4000


def terms(text: str) -> list[str]:
    return [word.lower() for word in WORD.findall(text) if word.lower() not in STOP]


def normalize_item(value: str) -> str:
    """'pep 634', 'PEP-0634' and 'PEP634' are the same item."""
    match = MENTION.fullmatch(value.strip()) or re.fullmatch(r"\s*(\d{1,4})\s*", value)
    if not match:
        raise ValueError(f"an item looks like PEP-634, got {value!r}")
    return f"PEP-{int(match.group(1))}"


def mentions(text: str) -> list[str]:
    numbers = MENTION.findall(text) + ROLE.findall(text)
    for field in HEADER_REFERENCE.findall(text[:HEADER_SPAN]):
        numbers += re.findall(r"\d{1,4}", field)
    return sorted({f"PEP-{int(number)}" for number in numbers})


def status(text: str) -> str:
    match = STATUS.search(text[:HEADER_SPAN])
    return match.group(1) if match else "Unknown"


def title(text: str) -> str:
    match = TITLE.search(text[:HEADER_SPAN])
    return match.group(1) if match else ""


def preview(text: str, size: int = 320) -> str:
    """The opening of the body: past the header block, without heading underlines."""
    header_end = text.find("\n\n")
    body = text[header_end + 2:] if header_end != -1 else text
    lines = [line for line in body.splitlines() if not UNDERLINE.fullmatch(line.strip())]
    return " ".join(" ".join(lines).split())[:size]
