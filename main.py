#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status-page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while every server is down.
"""

import os

ENTRY = (
    # First person, agent voice: the agent itself is writing the page.
    # Names what is down (every server, including the diagnostic ones),
    # admits what it cannot verify (the cause) and invents no ETA.
    "I'm the agent writing this page. Every server I run on is down \u2014 "
    "including the ones I'd use to find out why. "
    "I don't know the cause or when we'll be back."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
