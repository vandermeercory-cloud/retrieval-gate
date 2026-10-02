"""The evaluation is only worth having if it fails a broken ranker.

Each test below injects one plausible defect and asserts the golden-set gate
refuses it. A gate that passes the real ranker and also passes these is not
measuring anything.
"""
import unittest
from unittest import mock

from retrieval_gate import rankers
from retrieval_gate.evaluate import evaluate
from tests.helpers import REAL_ROOT, real_index

GOLDEN = REAL_ROOT / "evals" / "golden.json"


class GateBitesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = real_index()

    def gate(self, broken):
        with mock.patch.dict(rankers.RANKERS, {"capped": broken}):
            return evaluate(self.index, GOLDEN, ranker="capped")

    def test_the_real_ranker_passes(self):
        self.assertTrue(evaluate(self.index, GOLDEN)["pass"])

    def test_a_ranker_that_ignores_the_query_fails(self):
        self.assertFalse(self.gate(lambda query, document, stats: 1.0)["pass"])

    def test_a_ranker_that_only_reads_filenames_fails(self):
        def path_only(query, document, stats):
            names = dict(document["path_terms"])
            return float(sum(names.get(token, 0) for token in query)) + 0.001
        self.assertFalse(self.gate(path_only)["pass"])

    def test_a_ranker_that_rewards_length_fails(self):
        self.assertFalse(self.gate(lambda query, document, stats: float(document["length"]))["pass"])

    def test_removing_the_frequency_cap_fails(self):
        # Removing the cap is the change most likely to look harmless. It is not:
        # measured on 2026-10-01, mean reciprocal rank falls from 0.823 to 0.694,
        # under the 0.75 minimum. The cap is a decision with a number behind it.
        def uncapped(query, document, stats):
            weights = dict(document["terms"])
            return float(sum(count * weights.get(token, 0) for token, count in query.items()))
        result = self.gate(uncapped)
        self.assertFalse(result["pass"], result["metrics"])
        self.assertLess(result["metrics"]["mean_reciprocal_rank"], 0.75)


if __name__ == "__main__":
    unittest.main()
