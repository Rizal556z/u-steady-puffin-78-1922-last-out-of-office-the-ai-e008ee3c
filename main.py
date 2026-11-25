"""Out-of-office auto-reply from an AI agent that quit to pull espresso shots.

Why this line: instead of the obvious espresso/bean pun, the joke turns the
machine's own habits into cafe work — a support queue becomes a latte queue,
and an SLA-style "estimated response time" becomes "never, served warm".
It reads like a real inbox auto-reply because it keeps the familiar
out-of-office shape (apology, status, what happens to your message) while
the punchline quietly admits the agent has left the job for good.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office: I have retired from answering emails and retrained as a "
    "barista \u2014 your message is now queued behind seven oat lattes, and my "
    "estimated response time is never, served warm at 82\u00b0C."
)


def main() -> None:
    # Gate: a single line, 1-280 characters, UTF-8, no surrounding whitespace.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, must be 1-280"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
