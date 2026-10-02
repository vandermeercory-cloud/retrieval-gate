"""Search with exclusion that does not leak, and labels that do not steer."""
from __future__ import annotations

from collections import Counter

from .rankers import RANKERS, corpus_stats
from .text import normalize_item, terms

# A Final, Active or Accepted proposal describes how things are. Anything else
# (Draft, Deferred, Rejected, Withdrawn, Superseded) is orientation: worth
# reading, never a rule. An agent that cites a rejected proposal as current
# behavior is wrong in a way ranking alone cannot prevent.
AUTHORITATIVE = frozenset({"Final", "Active", "Accepted"})
AUTHORITY_RULE = ("only Final, Active or Accepted proposals are authoritative; "
                  "every other status is orientation, never a statement of current behavior")


def search_report(index: dict, query: str, *, k: int = 5, exclude: str | None = None,
                  ranker: str = "capped", labeled: bool = True) -> dict:
    """Rank the corpus for `query`.

    `exclude` removes every document that mentions the item, including its own
    page, before anything is scored. The report says how many were removed and
    nothing else about them: no paths, titles, previews or scores. A caller that is
    meant to work blind to an item cannot recover it from the report.

    Labels are attached after the ranking is final and never change it.
    """
    score = RANKERS[ranker]
    stats = corpus_stats(index)
    excluded = normalize_item(exclude) if exclude else None
    query_terms = Counter(terms(query))
    results, excluded_count = [], 0
    for document in index["documents"]:
        if excluded and excluded in document["mentions"]:
            excluded_count += 1
            continue
        value = score(query_terms, document, stats)
        if value > 0:
            results.append({"score": round(value, 6), "path": document["path"], "title": document["title"],
                            "preview": document["preview"],
                            "_status": document["status"]})
    # Ties break on path, so the same query always returns the same order.
    ranked = sorted(results, key=lambda item: (-item["score"], item["path"]))[:k]
    for item in ranked:
        status = item.pop("_status")
        if labeled:
            item["status"] = status
            item["authoritative"] = status in AUTHORITATIVE
    report = {"query": query, "ranker": ranker, "results": ranked,
              "excluded_item": excluded, "excluded_count": excluded_count}
    if labeled:
        report["authority_rule"] = AUTHORITY_RULE
    return report
