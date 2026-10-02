"""Build the index once; searching never re-reads the corpus."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from pathlib import Path

from .text import mentions, preview, status, terms, title

TOP_TERMS = 250       # per document: enough vocabulary to match, small enough to ship
TOP_PATH_TERMS = 40
# Bump when the stored fields change, so a saved index from older code is rebuilt.
INDEX_VERSION = 2


def _own_item(path: Path) -> str:
    match = re.fullmatch(r"pep-0*(\d+)\.rst", path.name)
    return f"PEP-{int(match.group(1))}" if match else ""


def build_index(corpus: Path, out: Path | None = None) -> dict:
    documents = []
    for path in sorted(corpus.glob("*.rst")):
        content = path.read_text(encoding="utf-8", errors="replace")
        relative = path.name
        all_terms = terms(content)
        own = _own_item(path)
        documents.append({
            "path": relative,
            "sha256": hashlib.sha256(content.encode()).hexdigest(),
            "length": len(all_terms),
            "terms": Counter(all_terms).most_common(TOP_TERMS),
            "path_terms": Counter(terms(re.sub(r"[/._-]+", " ", relative))).most_common(TOP_PATH_TERMS),
            # A document always "mentions" itself, so excluding an item removes its own page too.
            "mentions": sorted(set(mentions(content)) | ({own} if own else set())),
            "status": status(content),
            "title": title(content),
            "preview": preview(content),
        })
    index = {"version": INDEX_VERSION, "documents": documents}
    if out:
        _atomic_json(out, index)
    return index


def load_index(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _atomic_json(path: Path, payload: dict) -> None:
    """Write then rename, so a reader never sees half an index."""
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(dir=path.parent, prefix=".index-", suffix=".json")
    with os.fdopen(handle, "w", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=1)
    os.replace(temporary, path)
