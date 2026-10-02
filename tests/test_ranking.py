import unittest

from retrieval_gate.search import search_report
from tests.helpers import corpus


class RankingTests(unittest.TestCase):
    def test_the_same_query_always_returns_the_same_order(self):
        index, keep = corpus({"pep-0001.rst": "Status: Final\nwidget gadget", "pep-0002.rst": "Status: Final\nwidget"})
        self.addCleanup(keep.cleanup)
        self.assertEqual(search_report(index, "widget gadget"), search_report(index, "widget gadget"))

    def test_ties_break_on_path(self):
        index, keep = corpus({"pep-0002.rst": "Status: Final\nwidget", "pep-0001.rst": "Status: Final\nwidget"})
        self.addCleanup(keep.cleanup)
        self.assertEqual(["pep-0001.rst", "pep-0002.rst"],
                         [r["path"] for r in search_report(index, "widget")["results"]])

    def test_repetition_cannot_buy_a_ranking(self):
        # Without the cap, 100 repetitions would score 100 against 5. With it,
        # the document that is actually about widgets wins on its name.
        index, keep = corpus({"pep-0001.rst": "Status: Final\n" + "widget " * 100,
                              "pep-0002-widget.rst": "Status: Final\n" + "widget " * 5})
        self.addCleanup(keep.cleanup)
        self.assertEqual("pep-0002-widget.rst", search_report(index, "widget")["results"][0]["path"])

    def test_a_query_with_no_matching_terms_returns_nothing(self):
        index, keep = corpus({"pep-0001.rst": "Status: Final\nwidget"})
        self.addCleanup(keep.cleanup)
        self.assertEqual([], search_report(index, "zeppelin")["results"])


if __name__ == "__main__":
    unittest.main()
