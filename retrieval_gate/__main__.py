"""python -m retrieval_gate {index|search|eval|compare}"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .evaluate import evaluate
from .index import INDEX_VERSION, build_index, load_index
from .rankers import RANKERS
from .search import search_report

ROOT = Path(__file__).resolve().parent.parent
CORPUS, INDEX, GOLDEN = ROOT / "corpus", ROOT / "build" / "index.json", ROOT / "evals" / "golden.json"


def _index() -> dict:
    """The saved index, rebuilt when it is missing or was written by older code."""
    if INDEX.exists():
        index = load_index(INDEX)
        if index.get("version") == INDEX_VERSION:
            return index
    return build_index(CORPUS, INDEX)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="retrieval_gate")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("index", help="build build/index.json from corpus/")
    s = sub.add_parser("search", help="rank the corpus for a query")
    s.add_argument("query")
    s.add_argument("--k", type=int, default=5)
    s.add_argument("--exclude", help="an item to work blind to, e.g. PEP-634")
    s.add_argument("--ranker", choices=sorted(RANKERS), default="capped")
    e = sub.add_parser("eval", help="score a ranker on the golden set; exit 1 below the minimums")
    e.add_argument("--ranker", choices=sorted(RANKERS), default="capped")
    e.add_argument("--k", type=int, default=5)
    sub.add_parser("compare", help="every ranker against the same golden set")
    args = parser.parse_args(argv)

    if args.command == "index":
        index = build_index(CORPUS, INDEX)
        print(f"indexed {len(index['documents'])} documents into {INDEX.relative_to(ROOT)}")
        return 0
    if args.command == "search":
        print(json.dumps(search_report(_index(), args.query, k=args.k, exclude=args.exclude, ranker=args.ranker), indent=2))
        return 0
    if args.command == "eval":
        result = evaluate(_index(), GOLDEN, k=args.k, ranker=args.ranker)
        m = result["metrics"]
        print(f"{m['ranker']}: hit@{m['k']} {m['hit_rate_at_k']:.3f}  MRR {m['mean_reciprocal_rank']:.3f}  "
              f"recall@{m['k']} {m['mean_recall_at_k']:.3f}  over {m['cases']} cases")
        for failure in result["failures"]:
            print(f"  BELOW MINIMUM  {failure}")
        print("PASS" if result["pass"] else "FAIL")
        return 0 if result["pass"] else 1
    if args.command == "compare":
        index = _index()
        print(f"{'ranker':8s} {'hit@5':>7s} {'MRR':>7s} {'recall@5':>9s}  gate")
        for name in sorted(RANKERS):
            r = evaluate(index, GOLDEN, ranker=name)
            m = r["metrics"]
            print(f"{name:8s} {m['hit_rate_at_k']:7.3f} {m['mean_reciprocal_rank']:7.3f} {m['mean_recall_at_k']:9.3f}  "
                  f"{'pass' if r['pass'] else 'FAIL'}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
