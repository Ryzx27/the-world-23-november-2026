# news-image-20261123 — THE WORLD, Monday 23 November 2026

A code-only make.fun entry for the "Sum up 23 November's world news in
one image" bounty. The program (`main.py`, Python 3.13, standard library
only) copies the front-page image `entry.png` to `/output/entry.png`.
No network, no model calls, no randomness: two runs write identical bytes.

## The image

An editorial front page, 1024x1024 PNG, naming the day it sums up:

- **COP31** — the climate talks fail, labelled "Worst Ever"; UN chief
  Guterres "deeply disappointed"; the EU says the talks were "hijacked
  by oil states"; the final draft avoided the words "fossil fuels".
- **THE GULF** — 25+ tankers hit in and around the Strait of Hormuz in
  seven days; Gulf oil flow falls; the UAE shuttles oil under US
  military protection; Houthis strike Riyadh for a third straight day.
- **UKRAINE** — a Russian cargo ship still ablaze off Finland; new
  footage of the Crimea Bridge blast; Poland says three Russian cruise
  missiles hit on Friday; 14 missing after a Kyiv-region drone strike.
- **GAZA** — Israeli strikes kill nine in 48 hours; the death toll since
  the October 2025 ceasefire reaches 1,661; Netanyahu-Eisenkot unity
  talks end without a deal.
- **AROUND THE WORLD** — North Korea keeps building nukes; the Pentagon
  releases 43 more UAP files; BepiColombo enters orbit around Mercury;
  an Indonesia factory fire leaves seven dead and 50 missing; the AI
  sell-off deepens; India post a record 720/9 in Wellington. Also:
  Bolsonaro "stable" in intensive care; 24 civilians killed in South
  Sudan; 35 Fulanis killed in Nigeria.

The two panel illustrations are original artwork made for this entry;
the headlines and decks are set in DejaVu fonts.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see LICENSE.
