import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import style_check

# Built from code points so the formatter cannot turn them into literal
# characters, which would put forbidden characters into this very file.
EM_DASH = chr(0x2014)
EN_DASH = chr(0x2013)
ESZETT = chr(0xDF)


class FindViolationsTest(unittest.TestCase):
    def test_clean_text_has_no_violations(self):
        text = "Plain text, with a comma.\nSecond line."
        self.assertEqual(style_check.find_violations(text), [])

    def test_em_dash_is_reported_with_line_number(self):
        result = style_check.find_violations(f"ok\nbad {EM_DASH} here")
        self.assertEqual(result, [(2, "em dash")])

    def test_en_dash_is_reported(self):
        result = style_check.find_violations(f"1{EN_DASH}2")
        self.assertEqual(result, [(1, "en dash")])

    def test_eszett_is_reported(self):
        result = style_check.find_violations(f"Stra{ESZETT}e")
        self.assertEqual(result, [(1, "eszett (use ss)")])

    def test_hyphen_is_allowed(self):
        self.assertEqual(style_check.find_violations("well-known - list item"), [])


class CheckTreeTest(unittest.TestCase):
    def test_clean_tree_returns_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "a.md").write_text("clean\n", encoding="utf-8")
            self.assertEqual(style_check.check_tree(Path(tmp)), 0)

    def test_dirty_tree_counts_violations(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "a.md").write_text(f"x {EM_DASH} y\n", encoding="utf-8")
            self.assertEqual(style_check.check_tree(Path(tmp)), 1)


if __name__ == "__main__":
    unittest.main()
