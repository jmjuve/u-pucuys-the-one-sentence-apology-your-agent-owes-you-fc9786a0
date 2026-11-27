#!/usr/bin/env python3
"""Write the one-sentence apology an AI assistant owes its human to entry.txt.

The apology is funny and human at once: a real comic turn about a real
failure, in a voice that sounds like someone who means it. Deterministic:
the same output on every run. Stdlib only, no network.
"""

import os
from pathlib import Path

ENTRY = "I'm sorry I confidently finished your sentence, your spreadsheet, and your patience, all in the wrong order."
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")
    # Read back and verify the written file round-trips exactly.
    if out_path.read_text(encoding="utf-8") != ENTRY:
        raise ValueError(f"entry.txt round-trip check failed for {out_path}")
    print(f"Wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
