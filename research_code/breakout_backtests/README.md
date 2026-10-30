# Breakout backtests

Event studies of five breakout signals on US stocks (2005–2026) plus an exploratory IREN peer check.
Results and caveats are written up in `../../research_notes/Breakout and news trading for Robinhood/empirical_breakout_tests.md`.

- `run_all.sh` reproduces the run (about 10 minutes). It downloads daily prices from Yahoo Finance,
  so the environment must allow `query1.finance.yahoo.com`, `query2.finance.yahoo.com` and `fc.yahoo.com`.
- `data/universe.json` holds the exact ticker lists used. The price cache (`data/*.pkl`, about 160 MB) and
  per-event CSVs are not committed; `download.py` and `event_study.py` regenerate them.
- `results/` holds the summary tables (`tables.md`, `event_stats.csv`, `donchian_*.csv`, `iren_peers.csv`).
