import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

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

    def test_repeated_character_is_reported_once_per_line(self):
        result = style_check.find_violations(f"{EM_DASH}{EM_DASH}\n{EM_DASH}")
        self.assertEqual(result, [(1, "em dash"), (2, "em dash")])

    def test_different_character_types_on_same_line_are_reported(self):
        result = style_check.find_violations(f"{EM_DASH}{EN_DASH}{ESZETT}")
        self.assertEqual(
            result,
            [(1, "em dash"), (1, "en dash"), (1, "eszett (use ss)")],
        )


class CheckTreeTest(unittest.TestCase):
    def test_clean_tree_returns_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "a.md").write_text("clean\n", encoding="utf-8")
            self.assertEqual(style_check.check_tree(Path(tmp)), 0)

    def test_dirty_tree_counts_violations(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "a.md").write_text(f"x {EM_DASH} y\n", encoding="utf-8")
            self.assertEqual(style_check.check_tree(Path(tmp)), 1)

    def test_nested_markdown_reports_relative_path_and_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "guide.md").write_text(
                f"clean\n{EM_DASH}\n", encoding="utf-8"
            )
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(style_check.check_tree(root), 1)
            self.assertEqual(output.getvalue(), "docs/guide.md:2: em dash\n")

    def test_generated_directories_are_pruned_at_any_depth(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for parent in (root, root / "docs"):
                for name in style_check.EXCLUDED_DIRS:
                    directory = parent / name
                    directory.mkdir(parents=True)
                    (directory / "bad.md").write_bytes(b"\xff")
            self.assertEqual(list(style_check.iter_markdown_files(root)), [])

    def test_non_markdown_files_are_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "notes.txt").write_bytes(b"\xff")
            self.assertEqual(style_check.check_tree(Path(tmp)), 0)

    def test_missing_root_is_rejected(self):
        with (
            tempfile.TemporaryDirectory() as tmp,
            self.assertRaises(NotADirectoryError),
        ):
            style_check.check_tree(Path(tmp) / "missing")

    def test_file_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "guide.md"
            path.write_text("clean", encoding="utf-8")
            with self.assertRaises(NotADirectoryError):
                style_check.check_tree(path)

    def test_directory_read_errors_are_not_silently_ignored(self):
        def unreadable_walk(root, onerror):
            onerror(PermissionError("Cannot read directory"))
            return iter(())

        with (
            tempfile.TemporaryDirectory() as tmp,
            patch.object(style_check.os, "walk", side_effect=unreadable_walk),
            self.assertRaises(PermissionError),
        ):
            style_check.check_tree(Path(tmp))

    def test_file_read_errors_produce_cli_error_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "guide.md").write_text("clean", encoding="utf-8")
            with (
                patch.object(Path, "read_text", side_effect=PermissionError("denied")),
                patch("sys.stderr", new_callable=io.StringIO) as errors,
            ):
                self.assertEqual(style_check.main(["style_check.py", tmp]), 2)
            self.assertIn("denied", errors.getvalue())


class CommandLineTest(unittest.TestCase):
    def run_checker(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(Path(style_check.__file__).resolve()), *args],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_default_root_is_working_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "guide.md").write_text("clean", encoding="utf-8")
            result = self.run_checker(Path(tmp))
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout + result.stderr, "")

    def test_violations_have_exit_code_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "guide.md").write_text(EM_DASH, encoding="utf-8")
            result = self.run_checker(Path(tmp), ".")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "guide.md:1: em dash\n")
            self.assertEqual(result.stderr, "")

    def test_invalid_inputs_have_exit_code_two_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "guide.md").write_text("clean", encoding="utf-8")
            for args in (("missing",), ("guide.md",), (".", "extra")):
                with self.subTest(args=args):
                    result = self.run_checker(root, *args)
                    self.assertEqual(result.returncode, 2)
                    self.assertTrue(result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_invalid_utf8_has_exit_code_two_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "guide.md").write_bytes(b"\xff")
            result = self.run_checker(Path(tmp), ".")
            self.assertEqual(result.returncode, 2)
            self.assertTrue(result.stderr)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
