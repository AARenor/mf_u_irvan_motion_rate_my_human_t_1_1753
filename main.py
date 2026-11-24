#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt. Standard library only, no network."""

import os
import sys

TEXT = (
    "Five stars. He asked me to summarize his day. "
    "I wrote: argued with a toaster, lost. "
    "He said add nuance. I wrote: twice."
)


def output_dir() -> str:
    """MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, otherwise /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
