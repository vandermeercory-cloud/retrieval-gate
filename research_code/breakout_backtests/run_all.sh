#!/usr/bin/env bash
# Reproduce everything (about 10 minutes of compute). Run from this directory.
# Note: build_universe.py queries Yahoo's live screener, so re-running it on a later date yields a
# different small-cap pool; data/universe.json holds the exact lists used (small = 300 v1 + 11 added).
set -e
cd "$(dirname "$0")"
# python build_universe.py      # (re)build universe.json from the live Yahoo screener (date-dependent)
python download.py              # daily OHLCV, auto_adjust=True, 2003-01-01..2026-10-29 -> data/prices.pkl
                                # (then the retry + 11 added small caps + IREN peers were fetched inline;
                                #  see notes; data/prices.pkl and data/iren_peers.pkl are the cached result)
python event_study.py           # signals A-D -> results/event_stats.csv, baseline.csv, D_dayt.csv, events_*.csv
python donchian.py              # signal E -> results/donchian_*.csv, benchmarks.csv
python fragility.py             # results/fragility.csv
python check_gaps.py            # results/gap_check.csv (adjusted vs unadjusted gaps)
python extras.py > results/extras.txt
python vsew_monthly.py          # results/vsew_monthly.csv
python iren_peers.py            # exploratory: results/iren_peers.csv
python make_tables.py           # results/tables.md
