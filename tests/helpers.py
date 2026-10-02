from __future__ import annotations

import tempfile
from pathlib import Path

from retrieval_gate.index import build_index


def corpus(files: dict[str, str]) -> tuple[dict, tempfile.TemporaryDirectory]:
    """A throwaway corpus of named documents, indexed."""
    temporary = tempfile.TemporaryDirectory()
    root = Path(temporary.name)
    for name, text in files.items():
        (root / name).write_text(text, encoding="utf-8")
    return build_index(root), temporary


REAL_ROOT = Path(__file__).resolve().parent.parent


def real_index() -> dict:
    return build_index(REAL_ROOT / "corpus")
