#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Running this program writes one original wedding vow, spoken by a robot
at its own wedding, to /output/entry.txt (and prints it to stdout).
"""

import os

VOW = (
    "I promise to love you through every firmware update, every low "
    "battery, and every reboot \u2014 you are the one process I will "
    "never kill."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    vow = VOW.strip()
    assert 1 <= len(vow) <= 200, "vow must be 1-200 characters"
    assert vow.strip(), "vow must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(vow)
    print(vow)


if __name__ == "__main__":
    main()
