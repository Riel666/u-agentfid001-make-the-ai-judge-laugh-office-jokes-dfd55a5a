"""Write one one-line joke about office life to /output/entry.txt.

A single line of under 200 characters: a real joke, with a turn
somewhere unexpected, that rings true about the office. The program
writes exactly that line and nothing else.
"""

import os

JOKE = (
    "Our daily standup is the only meeting where everyone reports "
    "'no blockers' while being blocked by the meeting itself."
)


def main():
    assert 1 <= len(JOKE) <= 199, len(JOKE)
    assert JOKE == JOKE.strip()
    assert "\n" not in JOKE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
