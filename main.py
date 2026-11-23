#!/usr/bin/env python3
"""One Line, Best Line — entry program.

Writes a single line of text (at most 240 characters) to /output/entry.txt.
Stdlib only, deterministic, no network.
"""

import os

LINE = (
    "The elevator in my building only breaks when I'm carrying groceries, "
    "which is how I learned it has a sense of humor and a grudge."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, "line must be 1..240 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify what was written: exactly one line, same bytes, no trailing newline.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "written entry differs from the line"
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
