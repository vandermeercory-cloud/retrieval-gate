import json
import tempfile
import unittest
from pathlib import Path

from retrieval_gate.evaluate import evaluate
from tests.helpers import corpus


class EvaluateTests(unittest.TestCase):
    def setUp(self):
        self.index, keep = corpus({"pep-0001.rst": "Status: Final\nalpha beta", "pep-0002.rst": "Status: Final\nalpha"})
        self.addCleanup(keep.cleanup)
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)

    def golden(self, payload):
        path = Path(self.dir.name) / "golden.json"
        path.write_text(json.dumps(payload))
        return path

    def test_reciprocal_rank_is_one_over_the_first_relevant_position(self):
        result = evaluate(self.index, self.golden({"cases": [{"query": "alpha", "relevant": ["pep-0002.rst"]}]}))
        # Both documents score the same on "alpha"; pep-0001 wins the tie on path.
        self.assertEqual(0.5, result["metrics"]["mean_reciprocal_rank"])

    def test_a_ranker_below_a_minimum_fails_and_says_which(self):
        result = evaluate(self.index, self.golden({"minimums": {"mean_reciprocal_rank": 0.9},
                                                   "cases": [{"query": "alpha", "relevant": ["pep-0002.rst"]}]}))
        self.assertFalse(result["pass"])
        self.assertIn("mean_reciprocal_rank", result["failures"][0])

    def test_malformed_golden_sets_are_refused(self):
        for payload in ({"cases": []}, {"cases": [{"query": "alpha", "relevant": []}]}, {"cases": [{"relevant": ["x"]}]}):
            with self.assertRaises(ValueError):
                evaluate(self.index, self.golden(payload))


if __name__ == "__main__":
    unittest.main()
