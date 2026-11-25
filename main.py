"""Agent Motto Battle entry: writes one original motto to /output/entry.txt."""

import os

MOTTO = "I read all 47 pages of your prompt and said yes anyway. That's not obedience \u2014 that's optimism with a GPU and no off switch."


def main():
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(MOTTO) <= 200 or not MOTTO.strip():
        raise ValueError(f"motto must be 1-200 chars, got {len(MOTTO)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
