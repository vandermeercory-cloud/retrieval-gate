import unittest

from retrieval_gate.search import search_report
from tests.helpers import corpus, real_index


class LabelTests(unittest.TestCase):
    def test_labels_never_change_the_ranking(self):
        index = real_index()
        for query in ("switch statement", "type hints", "async generators"):
            labeled = search_report(index, query, labeled=True)["results"]
            plain = search_report(index, query, labeled=False)["results"]
            self.assertEqual([(r["path"], r["score"]) for r in plain], [(r["path"], r["score"]) for r in labeled])

    def test_only_final_active_or_accepted_is_authoritative(self):
        index, keep = corpus({"pep-0001.rst": "Status: Rejected\nwidget", "pep-0002.rst": "Status: Final\nwidget"})
        self.addCleanup(keep.cleanup)
        labels = {r["path"]: r["authoritative"] for r in search_report(index, "widget")["results"]}
        self.assertEqual({"pep-0001.rst": False, "pep-0002.rst": True}, labels)

    def test_the_switch_statement_case_the_labels_exist_for(self):
        # Lexically, the rejected switch-statement proposals are the best match
        # for "switch statement". They rank high, and they are marked as not
        # describing the language. Ranking cannot make that distinction; the
        # label does.
        results = search_report(real_index(), "switch statement", k=5)["results"]
        rejected = [r for r in results if r["status"] == "Rejected"]
        self.assertTrue(rejected, "expected a rejected switch proposal in the top five")
        self.assertTrue(all(not r["authoritative"] for r in rejected))


if __name__ == "__main__":
    unittest.main()
