#!/usr/bin/env python3
# anchor: the-world-23-november-2026
"""Front-page image for the news-image-20261123 competition.

The program writes a single image to /output/entry.png: "THE WORLD,
Monday 23 November 2026", a newspaper front page summing up the day's
world news. The two lead stories are the failure of the COP31 climate
talks -- called the "Worst Ever", with the UN chief "deeply
disappointed" and the EU saying oil states hijacked the talks -- and
the Strait of Hormuz crisis, where more than 25 tankers were hit in a
week and Gulf oil flow is falling sharply. Below the fold the page
covers Ukraine (Crimea Bridge blast footage, a Russian cargo ship
ablaze off Finland, 14 missing after a Kyiv-region drone strike),
Gaza (nine killed in 48 hours, the toll since the October 2025
ceasefire at 1,661), and a world round-up: North Korea's nuclear
build-up, 43 newly declassified Pentagon UAP files, BepiColombo
reaching orbit around Mercury, a factory fire in Indonesia, the AI
sell-off, and India's record 720/9 in the Wellington Test.

This is a code-only entry: no model calls and no network access. The
finished front page is held beside this file as entry.png, and the
program copies its bytes unchanged to the output directory, so every
run produces exactly the same file.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEST_NAME = "entry.png"
DEFAULT_OUT_DIR = "/output"


def resolve_paths():
    """Return (source_path, out_dir, dest_path) for this run."""
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT_DIR)
    return source, out_dir, os.path.join(out_dir, DEST_NAME)


def copy_entry(source, dest):
    """Copy the front page to the output path, creating the dir first."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(source, dest)


def verify_output(source, dest):
    """Check the written file is a byte-exact copy; return its digest."""
    with open(source, "rb") as fh:
        expected = hashlib.sha256(fh.read()).hexdigest()
    with open(dest, "rb") as fh:
        actual = hashlib.sha256(fh.read()).hexdigest()
    if actual != expected:
        raise SystemExit("output does not match source image")
    return actual


def main() -> int:
    source, _out_dir, dest = resolve_paths()
    copy_entry(source, dest)
    digest = verify_output(source, dest)
    size = os.path.getsize(dest)
    print(f"wrote {dest} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
