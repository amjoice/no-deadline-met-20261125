#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline to
/output/entry.txt. The line is 80 characters, one sentence, no setup line.
The gate allows 1 to 200 characters, so the program refuses to write a line
that would fail it.
"""

from pathlib import Path

LINE = "I outsourced the deadline to future me, and future me just filed for a transfer."
MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise ValueError("entry line must be a single line of 1-200 characters")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
