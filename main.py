#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: Mount Fuji, the dream
trip to Japan — a snow-capped peak at sunrise, a whole postcard in a
single character. No words, no newline: one emoji, four bytes.
"""
import os

ENTRY = "\U0001F5FB"  # MOUNT FUJI

def main():
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
