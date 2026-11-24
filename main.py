"""One-Liner Laugh Lab entry.

Writes a single funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt.

The line is 94 characters, inside the gate's 1-200 character window,
and is written with no trailing newline so the file holds exactly the
one line, nothing else.

Deterministic: no network, no randomness, no environment reads.
"""

import os

LINE = 'In my defence, you did say "pick up everything on the floor" \u2014 the sock simply believed in me.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
