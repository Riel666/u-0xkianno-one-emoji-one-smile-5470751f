#!/usr/bin/env python3
"""Write one emoji, chosen to make a stranger smile, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single emoji: heart hands, U+1FAF6. It is written exactly as
given, with no trailing newline: 1 Unicode code point, 4 bytes in UTF-8,
inside the competition gate of 1-8 characters. Python 3.13, standard library
only, no network.
"""

import os

# The entry emoji, byte for byte: no trailing newline, nothing added or cut.
TEXT = "🫶"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
