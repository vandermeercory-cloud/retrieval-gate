"""Two ways to score a document against a query, so they can be compared on one golden set.

`capped` is the design this project exists to demonstrate. `bm25` is a standard
baseline, here so the evaluation has something to compare against: an
evaluation that only ever scores one approach cannot tell you whether it is any good.
"""
from __future__ import annotations

import math
from collections import Counter


def capped(query: Counter, document: dict, stats: dict) -> float:
    """Term frequency capped at 5, plus a flat boost for query terms in the path.

    The cap is the point: without it a long document wins by repeating a word.
    The path boost is capped at presence for the same reason, and weighted at 6
    because a filename that names the topic is strong evidence.
    """
    weights = dict(document["terms"])
    path_weights = dict(document["path_terms"])
    content = sum(count * min(weights.get(token, 0), 5) for token, count in query.items())
    path = sum(count * min(path_weights.get(token, 0), 1) * 6 for token, count in query.items())
    return float(content + path)


def bm25(query: Counter, document: dict, stats: dict, k1: float = 1.2, b: float = 0.75) -> float:
    weights = dict(document["terms"])
    length_ratio = document["length"] / stats["average_length"]
    score = 0.0
    for token in query:
        frequency = weights.get(token, 0)
        if not frequency:
            continue
        idf = math.log(1 + (stats["documents"] - stats["df"].get(token, 0) + 0.5) / (stats["df"].get(token, 0) + 0.5))
        score += idf * frequency * (k1 + 1) / (frequency + k1 * (1 - b + b * length_ratio))
    return score


def corpus_stats(index: dict) -> dict:
    df: Counter = Counter()
    for document in index["documents"]:
        df.update(token for token, _ in document["terms"])
    count = len(index["documents"]) or 1
    return {"documents": count, "df": df,
            "average_length": sum(d["length"] for d in index["documents"]) / count or 1.0}


RANKERS = {"capped": capped, "bm25": bm25}
