"""Make the Judge Smile: write one line to /output/entry.txt.

The line is written exactly, with no trailing newline: 108 characters,
inside the gate's 1-200 character window. It is a small good thing that
happened today (24 Nov 2026): a neighbour left a mango on the doorstep
with a deadpan note. Warmth (a neighbour's kindness), surprise (the
note's wording), one concrete detail (the mango, the doorstep, the note),
fresh wording, and the morning anchors it to today.
"""

import os

LINE = "My neighbour left a mango on my doorstep this morning with a note that just said, 'tree did too much again.'"


def main():
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    # On-topic guard (judge criterion 1): the line must name a small good
    # thing that happened today, concretely (this morning, a mango, a note).
    assert "this morning" in LINE and "mango" in LINE, "line must anchor today with a concrete detail"
    # Byte guard: the entry is pure ASCII, so its byte size equals its
    # character count — the tie-break favours smaller bytes, and no
    # multi-byte character may creep in unnoticed.
    assert len(LINE.encode("utf-8")) == len(LINE), "entry must be ASCII"
    os.makedirs("/output", exist_ok=True)
    # Write bytes, not text: no newline translation or encoding surprise
    # on any platform — what the grader reads is exactly LINE.
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
