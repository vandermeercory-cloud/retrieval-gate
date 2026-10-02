# retrieval-gate

A small retrieval layer that has to pass its own evaluation before anything relies on it.

I designed the original as the retrieval layer of an agentic software-delivery
framework, where agents look up written guidance before they act. This is a
standalone rebuild of that design on a public corpus, so anyone can read it, run
it and check the numbers. Standard library only, Python 3.9 or later.

## What it does

- **Ranks** documents for a query, lexically and deterministically.
- **Excludes** an item along with every document that cites it, and reports only
  how many documents it removed. An agent being evaluated on that item can
  neither look it up nor recover it from the report.
- **Labels** each result as authoritative or not. Labels are attached after
  ranking and never change the order.
- **Evaluates** a ranker against a golden set and fails it below stated minimums.

## Results

29 questions a developer might ask, each paired with the proposal that answers
it. Top 5 results per question.

| Ranker | hit@5 | MRR | recall@5 | Gate |
| --- | --- | --- | --- | --- |
| **capped** (this design) | **0.966** | 0.823 | **0.966** | pass |
| BM25 baseline | 0.931 | **0.879** | 0.931 | pass |
| capped, with the frequency cap removed | 0.931 | 0.694 | 0.931 | **fail** |

Minimums: hit@5 0.90, MRR 0.75, recall@5 0.90. The capped design finds the
answer more often, and BM25 places it higher when both find it. Every ranker is
scored on the same questions, which is what makes that comparison possible.
`compare` prints the first two rows; the third is measured in
`tests/test_gate_bites.py`.

## Design decisions

**Term frequency is capped at 5.** Without the cap, a long document wins by
repeating a word. The cap is measured: removing it drops MRR from 0.823 to
0.694, and the gate fails the result (`tests/test_gate_bites.py`).

**Words in a filename are boosted once.** Where files are named by topic, a
filename match is strong evidence. PEP filenames are numbers, so the boost never
fires on this corpus; `tests/test_ranking.py` covers it on a small corpus with
named files.

**Ties break on path.** The same query always returns the same order, which is
what makes a regression visible.

**Exclusion catches every citation style.** PEPs cite each other in prose
("PEP 634"), with the reStructuredText role (`` :pep:`634` ``), and in header
fields (`Requires: 634`), and the role is by far the most common. The tests
exclude PEP 634 from the real corpus and then check, without using the parser,
that no surviving document contains the number at all. They also serialize a
full report and search it for every excluded path and for a phrase that only an
excluded document contains (`tests/test_exclusion.py`).

**Labels are attached after ranking.** Each result carries its proposal's status
and is marked authoritative only when that status is Final, Active or Accepted.
A test confirms that order and scores are identical with labels on and off
(`tests/test_labels.py`). A search for a switch statement shows why the labels
exist:

```
python3 -m retrieval_gate search "switch statement" --k 3
```

| Rank | Proposal | Status | Authoritative |
| --- | --- | --- | --- |
| 1 | PEP 275, Switching on Multiple Values | Rejected | no |
| 2 | PEP 3103, A Switch/Case Statement | Rejected | no |
| 3 | PEP 8, Style Guide for Python Code | Active | yes |

The two best matches are rejected proposals for a switch statement. They are the
most relevant documents, so they rank first, and the label is what tells an
agent not to treat them as a description of the language.

**The gate is tested for failure.** Four rankers must fail it, and do: one that
ignores the query, one that reads only filenames, one that rewards length, and
the uncapped variant above (`tests/test_gate_bites.py`).

## Where it falls short

**Different words for the same idea.** "Point at the exact expression that
failed in a traceback" should find PEP 657. That proposal describes the feature
in terms of error locations, column offsets and carets, and apart from
"traceback" it uses the question's words once or twice at most. PEP 342, on
generators, uses "point", "expression" and "traceback" often enough to reach the
cap on all three, and ranks first. PEP 657 comes 9th under the capped ranker and
6th under BM25. Lexical ranking cannot connect different words for the same
idea. Embeddings might, and this harness is how to find out on a given corpus.

**No weight for rare words.** The capped ranker counts every word the same, so
"traceback", which appears in 14 of the 75 proposals, earns no more than
"expression", which appears in 40. BM25 weights rare words more heavily, and
adding that weighting to the capped ranker is the next experiment I would run
through this harness.

**The cap has a cost.** For "conventions for writing docstrings", PEP 8 and
PEP 257 each use "conventions" and "docstrings" at least five times, so the cap
scores them equal and the tie breaks on path, which puts PEP 8 first. Without
the cap, PEP 257 wins on "docstrings" (19 uses against 9), and BM25 also ranks
it first. Over the whole set the cap still earns its place, 0.823 MRR against
0.694 without it, and this question is the price.

## Run it

```
python3 -m retrieval_gate index                     # build build/index.json from corpus/
python3 -m retrieval_gate search "dataclasses"      # ranked, labeled results as JSON
python3 -m retrieval_gate search "pattern matching" --exclude PEP-634
python3 -m retrieval_gate eval                      # exits 1 below the minimums
python3 -m retrieval_gate compare                   # every ranker on the same questions
python3 -m unittest discover -s tests -t .          # 20 tests
```

## Corpus

75 Python Enhancement Proposals from [python/peps](https://github.com/python/peps),
pinned to commit `e449c7e`, with each file's SHA-256 in `corpus/MANIFEST.json`.
PEPs are placed in the public domain or under CC0. `scripts/fetch_corpus.py`
rebuilds the corpus and refuses any document without one of those statements;
it refused PEP 428.

## How it was built

I build through agentic development: AI coding agents do the implementation
inside a review process I designed, and tests and gates decide what is
accepted. This repository was built the same way.

## License

MIT for the code. The corpus documents keep their public-domain or CC0 status.
