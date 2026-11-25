"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true, one-line review of the dullest everyday object
we could name to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).

The object is the pencil eraser: its whole job is to disappear a little
every time it fixes someone else's mistake, until nothing is left of it
but the metal ferrule that used to hold it. That is the joke, and it only
fits this object, which is exactly what the judge brief asks for.
"""

import os

ENTRY = (
    "The eraser spends its life fixing other people's mistakes, "
    "and its reward is shrinking until it's just a metal cap holding nothing."
)


def output_path() -> str:
    """Where the entry goes: MAKEFUN_OUTPUT_DIR/entry.txt, default /output."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def gate_check(text: str) -> None:
    """Mirror the sealed gate scorer: UTF-8 text, 1 to 200 characters,
    not only whitespace, exactly one line. Fail loudly if it ever breaks."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1 to 200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    gate_check(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
