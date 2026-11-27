#!/usr/bin/env python3
"""Write the competition artifact: one short agent motto, at most 200 chars.

The motto lives in motto.txt next to this file so the text can be edited
without touching the program. Output is byte-identical on every run.
"""

import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "motto.txt"
MAX_CHARS = 200


def load_motto() -> str:
    """Return the motto, trailing newline stripped, checked against the gate."""
    text = SOURCE.read_text(encoding="utf-8").strip()
    if not text or len(text) > MAX_CHARS:
        sys.exit(f"motto.txt must hold 1 to {MAX_CHARS} characters of text")
    return text


def main() -> None:
    motto = load_motto()
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(motto.encode("utf-8"))
    print(f"wrote {target} ({len(motto)} chars)")


if __name__ == "__main__":
    main()
