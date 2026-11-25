"""One Star, Written in Sap — entry program.

Writes a single one-line, one-star review from a houseplant about its
human owner to /output/entry.txt. Deterministic, standard library only,
no network access, no randomness.
"""

import os

ENTRY = (
    "One star. She waters the plastic succulent beside me every morning, "
    "whispers 'stay strong, buddy,' and has never once watered me. "
    "I am the real plant. Would not recommend this owner to other plants."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Validate the review line, then write it to /output/entry.txt."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 279:
        raise ValueError(f"entry must be 1-279 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
