#!/usr/bin/env python3
"""Put the 21 November 2026 world-news image at /output/entry.png.

The image is a 1024x1024 infographic for Saturday 21 November 2026:
Russia's strikes on Kyiv bridges and Polish airspace, the ICJ ruling
that Myanmar committed genocide against the Rohingya, the Trump-Xi-
Putin trilateral summit, the US approval of nearly 900,000 AI chips
for China, the UK-EU deal for closer ties, and the US shutdown risk
as Iran tensions rise. It is bundled in this repository as entry.png.

The program only copies that fixed image to the output path, so it
needs no network and no randomness, and two runs write identical
bytes.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output") / "entry.png"


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(SRC.read_bytes())


if __name__ == "__main__":
    main()
