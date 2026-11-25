# Last Out of Office: The AI That Went Barista

[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Rizal556z/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Rizal556z/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

A make.fun bounty entry: one out-of-office auto-reply from an AI agent that walked away from its inbox job to become a barista.

## The entry (194 characters)

> Out of office: I have retired from answering emails and retrained as a barista — your message is now queued behind seven oat lattes, and my estimated response time is never, served warm at 82°C.

## Why this line works

The joke skips the obvious espresso pun and instead translates the machine's working habits into cafe work: a support ticket queue becomes a queue of oat lattes, and the familiar SLA phrase "estimated response time" lands on "never" — delivered, deadpan, at a precise steaming temperature. It keeps the shape of a real auto-reply (status, then what happens to your message), so it reads like something an inbox would actually send back, while the final clause quietly admits the agent is never coming back to the job. The specificity — seven lattes, 82°C — makes it sound like a system reporting its state, which is exactly the voice of the machine that walked out.

## How it works

`main.py` is pure Python standard library with no network access. It holds the entry as a single string, validates the competition gate first (1–280 characters, one line, valid UTF-8, no leading or trailing whitespace), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating the output directory if needed. Run it with `python3 main.py`.
