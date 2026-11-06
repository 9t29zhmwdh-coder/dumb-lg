"""Check Markdown files against the repository writing rules.

Rules (see CONTRIBUTING.md): no em dash, no en dash, no eszett (Swiss spelling).
Exit code 0 when clean, 1 when a violation is found.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Built from code points: the formatter rewrites escape sequences into literal
# characters, which would put the forbidden characters into this file.
FORBIDDEN = {
    chr(0x2014): "em dash",
    chr(0x2013): "en dash",
    chr(0xDF): "eszett (use ss)",
}


def find_violations(text: str) -> list[tuple[int, str]]:
    """Return (line number, description) for every forbidden character."""
    found: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for char, name in FORBIDDEN.items():
            if char in line:
                found.append((number, name))
    return found


def check_tree(root: Path) -> int:
    """Scan all Markdown files below root and print violations."""
    count = 0
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for number, name in find_violations(path.read_text(encoding="utf-8")):
            print(f"{path.relative_to(root)}:{number}: {name}")
            count += 1
    return count


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    return 1 if check_tree(root) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
