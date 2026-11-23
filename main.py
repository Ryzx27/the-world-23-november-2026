#!/usr/bin/env python3
# anchor: the-world-23-november-2026
"""news-image-20261123 entry: a program that writes one image to /output/entry.png.

The entry is a code-only program (no model calls, no network): it copies
the front-page image held beside this file -- "THE WORLD, Monday
23 November 2026" -- to the output directory. The image sums up the day's
world news in two lead stories plus a world round-up:

  1. COP31 -- the climate talks fail, labelled "Worst Ever"; UN chief
     Guterres "deeply disappointed"; the EU says the talks were
     "hijacked by oil states"; the final draft avoided the words
     "fossil fuels".
  2. THE GULF -- 25+ tankers hit in and around the Strait of Hormuz in
     seven days; Gulf oil flow falls; the UAE shuttles oil under US
     military protection; Houthis strike Riyadh for a third straight day.
  3. UKRAINE -- a Russian cargo ship still ablaze off Finland; new
     footage of the Crimea Bridge blast; Poland says three Russian
     cruise missiles hit on Friday; 14 missing after a Kyiv-region
     drone strike.
  4. GAZA -- Israeli strikes kill nine in 48 hours; the death toll
     since the October 2025 ceasefire reaches 1,661; Netanyahu-Eisenkot
     unity talks end without a deal.
  ALSO -- North Korea keeps building nukes; the Pentagon releases 43
  more UAP files; BepiColombo enters orbit around Mercury; an
  Indonesia factory fire leaves seven dead and 50 missing; the AI
  sell-off deepens; India post a record 720/9 in Wellington.

Determinism: the program reads only the image held beside it and copies
its bytes unchanged, so two runs write identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
