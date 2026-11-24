#!/usr/bin/env python3
"""Entry for 'The Funniest Toaster Error Message' (u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

Writes the one error line a kitchen toaster shows its owner (max 120
characters) to /output/entry.txt. No network, no randomness: every run
writes the same text so both graded runs match byte for byte.
"""
from pathlib import Path

LINE = (
    "ERR 2T: bread ejected barely warm. I have toasted 9,214 slices "
    "and never once been thanked. I need a minute."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
