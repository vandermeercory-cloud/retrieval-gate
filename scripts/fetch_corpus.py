#!/usr/bin/env python3
"""Fetch a fixed set of Python Enhancement Proposals as the public corpus.

PEPs are placed in the public domain or under CC0, and each one carries a
Status line (Final, Rejected, Withdrawn, ...), which is what the authority
labels in this project read. The fetch is pinned to one commit of python/peps,
every file's SHA-256 is recorded in corpus/MANIFEST.json, and a document
without a public-domain or CC0 statement is refused rather than included.

    python3 scripts/fetch_corpus.py
"""
import hashlib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

COMMIT = "e449c7e446faec3ecf953e83fbe677b771bf5d7c"
RAW = "https://raw.githubusercontent.com/python/peps/{commit}/peps/pep-{num:04d}.rst"
# Language features and tooling, plus rejected and deferred proposals on the
# same topics, so retrieval has to rank near-misses and labels have work to do.
PEPS = [8, 20, 257, 263, 275, 285, 289, 308, 318, 328, 342, 343, 380, 405, 420,
        428, 435, 443, 448, 450, 453, 463, 465, 471, 484, 485, 492, 498, 505, 506,
        515, 518, 525, 526, 530, 544, 557, 563, 567, 570, 572, 584, 585, 586, 589,
        591, 593, 604, 612, 616, 617, 618, 634, 635, 636, 640, 642, 646, 654, 655,
        657, 668, 673, 675, 678, 680, 681, 684, 688, 695, 698, 701, 703, 709, 3103,
        3150]
LICENSED = re.compile(r"placed in the public domain|CC0", re.I)


def main() -> int:
    out = Path(__file__).resolve().parent.parent / "corpus"
    out.mkdir(exist_ok=True)
    manifest = {"source": "https://github.com/python/peps", "commit": COMMIT, "files": {}}
    refused = []
    for num in PEPS:
        name = f"pep-{num:04d}.rst"
        url = RAW.format(commit=COMMIT, num=num)
        body = None
        # Bounded retry: three attempts, then stop. An unbounded loop against a
        # flaky host turns one timeout into a stream of requests.
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "retrieval-gate"}), timeout=60) as r:
                    body = r.read()
                break
            except (TimeoutError, OSError):
                if attempt == 2:
                    raise
                time.sleep(2 * (attempt + 1))
        text = body.decode("utf-8")
        if not LICENSED.search(text):
            refused.append(num)
            continue
        (out / name).write_bytes(body)
        manifest["files"][name] = hashlib.sha256(body).hexdigest()
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(manifest['files'])} documents fetched at {COMMIT[:12]}; refused without a license statement: {refused or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
