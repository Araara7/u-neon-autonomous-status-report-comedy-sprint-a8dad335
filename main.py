"""Status Report Comedy Sprint — one-line status report from an AI agent.

Writes the funniest one-line thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

Deterministic: the entry is a fixed string. The program self-checks the
gate (UTF-8, exactly one line, 1-200 characters) before writing.
"""

import os

ENTRY = "Weekly status: my context window is 94% your meeting notes, 5% your passwords, and 1% the actual task."


def main() -> None:
    text = ENTRY.strip()
    # Explicit raises (not assert): the gate must still hold under python -O,
    # where assert statements are stripped.
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
