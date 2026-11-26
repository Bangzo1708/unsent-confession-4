#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — round 4 entry.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, then the unsent message
itself, one line written exactly as it was typed, with no
explanation after it.

Deterministic, no network, no arguments, no side effects beyond
writing that one file.
"""

ENTRY = (
    "To: Alex, my ex\n"
    "i kept the key to your apartment for a year after we broke up. "
    "i told myself it was an accident, but i checked the drawer "
    "every night hoping you'd ask for it back"
)


def main() -> None:
    # encoding + newline pinned so the bytes on disk are exactly
    # ENTRY on every platform (no locale encoding, no \n translation).
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
