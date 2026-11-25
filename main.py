"""One Line, One Laugh — a single funny line, written to /output/entry.txt.

The joke: I asked my AI for a joke about my life. It paused, then asked if
I wanted the short version or the therapy version. The laugh lands on the
punchline — the AI knows my life well enough to offer therapy instead.
Pure standard library; the program is deterministic and writes the same
115 characters on every run.
"""

import os
import stat
import sys

PUNCHLINE = (
    "I asked my AI for a joke about my life. It paused, then asked if I "
    "wanted the short version or the therapy version."
)

MAX_CHARS = 200


def line_is_ok(text):
    """A gate-ready line: one line, 1-200 chars, no blank, no stray control."""
    if not text or text != text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return all(ord(ch) >= 32 or ch in "\t" for ch in text)


def main():
    if not line_is_ok(PUNCHLINE):
        print("line failed the gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(PUNCHLINE)
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
