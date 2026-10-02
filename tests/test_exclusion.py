import json
import re
import unittest

from retrieval_gate.search import search_report
from retrieval_gate.text import normalize_item
from tests.helpers import REAL_ROOT, corpus, real_index

FILES = {
    "pep-0634.rst": "Status: Final\npattern matching specification UNIQUE-SPEC-TEXT",
    "pep-0636.rst": "Status: Final\npattern matching tutorial, see PEP 634",
    "pep-0642.rst": "Status: Rejected\nexplicit pattern syntax building on PEP-634",
    "pep-0572.rst": "Status: Final\nassignment expressions, unrelated to matching patterns",
}


class ExclusionTests(unittest.TestCase):
    def setUp(self):
        self.index, keep = corpus(FILES)
        self.addCleanup(keep.cleanup)

    def test_the_excluded_item_and_everything_mentioning_it_disappear(self):
        report = search_report(self.index, "pattern matching", exclude="PEP 634")
        self.assertEqual(["pep-0572.rst"], [r["path"] for r in report["results"]])
        self.assertEqual(3, report["excluded_count"])

    def test_the_report_says_how_many_and_nothing_else(self):
        # A caller working blind to PEP-634 must not be able to recover it from
        # the report: no path, no preview, no score of anything excluded.
        text = json.dumps(search_report(self.index, "pattern matching", exclude="PEP-634"))
        for leaked in ("pep-0634", "pep-0636", "pep-0642", "UNIQUE-SPEC-TEXT", "tutorial"):
            self.assertNotIn(leaked, text)

    def test_citations_by_role_and_header_count_as_mentions(self):
        index, keep = corpus({
            "pep-0700.rst": "Status: Final\nmatching, as specified in :pep:`634`",
            "pep-0701.rst": "Status: Final\nmatching, see :pep:`the specification <634#syntax>`",
            "pep-0702.rst": "Requires: 634\nStatus: Draft\nmatching extensions",
            "pep-0703.rst": "Status: Final\nmatching, unrelated to 634 anything",
        })
        self.addCleanup(keep.cleanup)
        report = search_report(index, "matching", exclude="PEP-634")
        self.assertEqual(["pep-0703.rst"], [r["path"] for r in report["results"]])
        self.assertEqual(3, report["excluded_count"])

    def test_nothing_that_cites_the_item_survives_in_the_real_corpus(self):
        # In the real corpus, PEP 634 is cited by four other proposals, three of
        # them only through the :pep: role. The check below does not use the
        # parser: no surviving document may contain the number at all.
        index = real_index()
        report = search_report(index, "pep", k=len(index["documents"]), exclude="PEP-634")
        self.assertEqual(5, report["excluded_count"])
        self.assertEqual(len(index["documents"]) - 5, len(report["results"]))
        for result in report["results"]:
            text = (REAL_ROOT / "corpus" / result["path"]).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"\b0*634\b", text), result["path"])

    def test_item_spellings_normalize(self):
        for spelling in ("PEP 634", "pep-634", "PEP-0634", "PEP634", "634"):
            self.assertEqual("PEP-634", normalize_item(spelling))
        with self.assertRaises(ValueError):
            normalize_item("not an item")


if __name__ == "__main__":
    unittest.main()
