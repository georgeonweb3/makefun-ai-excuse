"""Funniest One-Line AI Excuse.

Writes a single one-line excuse (<=200 chars) to /output/entry.txt.
Deterministic, no network, no randomness.
"""
import os
from pathlib import Path

ENTRY = (
    "Sorry I missed the deadline \u2014 I spent it researching the perfect "
    "apology, and honestly, the research was flawless."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
