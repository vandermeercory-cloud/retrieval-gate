"""Score a ranker against a golden set and refuse it below the stated minimums."""
from __future__ import annotations

import json
from pathlib import Path

from .search import search_report


def evaluate(index: dict, golden: Path, *, k: int = 5, ranker: str = "capped") -> dict:
    payload = json.loads(golden.read_text(encoding="utf-8"))
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("an evaluation needs a non-empty cases array")
    details, reciprocal_ranks, recalls, hits = [], [], [], 0
    for case in cases:
        query, relevant = case.get("query"), set(case.get("relevant", []))
        if not isinstance(query, str) or not query.strip() or not relevant:
            raise ValueError("every case needs a query and at least one relevant path")
        ranked = [item["path"] for item in search_report(index, query, k=k, ranker=ranker, labeled=False)["results"]]
        positions = sorted(ranked.index(path) + 1 for path in relevant if path in ranked)
        first = positions[0] if positions else None
        hits += 1 if first else 0
        reciprocal_ranks.append(1 / first if first else 0.0)
        recalls.append(len(positions) / len(relevant))
        details.append({"query": query, "relevant": sorted(relevant), "ranked": ranked, "first_relevant_rank": first})
    metrics = {"cases": len(cases), "k": k, "ranker": ranker,
               "hit_rate_at_k": hits / len(cases),
               "mean_reciprocal_rank": sum(reciprocal_ranks) / len(cases),
               "mean_recall_at_k": sum(recalls) / len(cases)}
    minimums = payload.get("minimums", {})
    failures = [f"{name}={metrics[name]:.3f} is below {minimum}" for name, minimum in minimums.items()
                if metrics.get(name, 0) < minimum]
    return {"metrics": metrics, "minimums": minimums, "pass": not failures, "failures": failures, "details": details}
