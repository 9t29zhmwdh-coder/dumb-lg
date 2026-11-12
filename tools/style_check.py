"""Check Markdown files against the repository writing rules.

Rules (see CONTRIBUTING.md): no em dash, no en dash, no eszett (Swiss spelling).
Exit codes: 0 when clean, 1 for violations, 2 for input or scan errors.
"""

from __future__ import annotations

import argparse
import os
import sys
from collections.abc import Iterator
from pathlib import Path

# Built from code points: the formatter rewrites escape sequences into literal
# characters, which would put the forbidden characters into this file.
FORBIDDEN = {
    chr(0x2014): "em dash",
    chr(0x2013): "en dash",
    chr(0xDF): "eszett (use ss)",
}
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "build",
    "dist",
    "__pycache__",
}


def find_violations(text: str) -> list[tuple[int, str]]:
    """Report each forbidden character type once per line."""
    found: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for char, name in FORBIDDEN.items():
            if char in line:
                found.append((number, name))
    return found


def raise_walk_error(error: OSError) -> None:
    # os.walk otherwise silently skips directories it cannot read.
    raise error


def iter_markdown_files(root: Path) -> Iterator[Path]:
    """Walk source directories without entering generated directories."""
    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")
    for directory, subdirs, filenames in os.walk(root, onerror=raise_walk_error):
        subdirs[:] = sorted(name for name in subdirs if name not in EXCLUDED_DIRS)
        for name in sorted(filenames):
            if name.endswith(".md"):
                yield Path(directory) / name


def check_tree(root: Path) -> int:
    """Print violations and count character types per line; raise on scan errors."""
    count = 0
    for path in iter_markdown_files(root):
        for number, name in find_violations(path.read_text(encoding="utf-8")):
            print(f"{path.relative_to(root)}:{number}: {name}")
            count += 1
    return count


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args(argv[1:])
    try:
        return 1 if check_tree(args.root) else 0
    except (OSError, UnicodeError) as error:
        print(f"style_check: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
