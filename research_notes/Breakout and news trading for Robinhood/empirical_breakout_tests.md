# Empirical breakout tests: US stocks, 2005–2026 (own backtests, Yahoo daily data)

All numbers below come from my own backtests run on 2026-10-30. Every source link points to a script or result file in `/tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/`, where `run_all.sh` gives the run order. All returns are in percent. Unless stated otherwise, "excess" means stock return minus SPY return over the identical open(t+1)→close(t+h) window.

**READ FIRST: both universes have survivorship bias and look-ahead in membership.** The large-cap universe is today's S&P 500, which includes stocks that became large because of the very breakouts tested (CVNA, SMCI, TSLA, NVDA, APP, COIN). The small-cap universe is today's listed $300M–$2B stocks: delisted losers are missing, which flatters results, and past small caps that broke out and graduated to large caps are also missing, which handicaps breakout signals. A random-entry baseline in the large-cap universe beat SPY by +1.03% per 60 days with no signal at all. Excess-vs-SPY figures should therefore be judged against that baseline or against the vs-EW (equal-weight universe) measure, not against zero.

## 1. How were the tests built, and which biases matter most?

### Takeaway
The design was fixed in code before any results were seen: 493 current S&P 500 stocks plus 311 current small caps, daily Yahoo bars from 2003 to 2026-10-29, signals from 2005-01-03, next-open entry, and per-horizon no-overlap blackouts. Two pre-declared survivorship controls were run: a random-entry baseline and a same-window equal-weight universe return. They matter more than any individual signal result, because random large-cap entries beat SPY by +0.34% per 20 days and +1.03% per 60 days.

### Cited Findings
**Universe construction**
- **Large caps:** 503 tickers, an approximate current S&P 500 list written from model knowledge (no index membership source was reachable). Yahoo served 493. The 10 that returned no data were AVB, BK, CTRA, DAY, EA, EQR, HOLX, MMC and WBD (0 rows), and PSKY (15 rows). I did not investigate why they were missing. 382 of the 493 have data back to January 2005, 460 to January 2016. — [build_universe.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/build_universe.py); [extras.txt](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/extras.txt)
- **Small caps, source:** the Yahoo custom screener (`yfinance.EquityQuery`) with region = us, exchange in {NMS, NYQ, NGM, NCM, ASE}, and intraday market cap between $300M and $2B as of 2026-10-30. It returned 1,616 names.
- **Small caps, filters:** equity only and USD only; names containing "Acquisition" (SPACs) dropped; names containing " Fund", "Municipal" or "Closed-End" dropped; current price ≥ $2; current 3-month average dollar volume ≥ $1M; first trade on or before 2021-12-31; not in the large list. 1,011 names passed, and 300 were drawn at random (numpy seed 42).
- **Small caps, price-filter correction:** after the user clarified that there should be no share-price filter, I added a draw at the same sampling rate (11 of 36, seed 42) from the 36 names excluded only by the $2 rule. This makes the final 311 equivalent to a uniform random sample of the price-unfiltered pool. Only 128 of the 311 have data back to January 2005; 210 have data back to January 2016. — [build_universe.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/build_universe.py); [universe.json](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/data/universe.json); [small_screener_raw.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/data/small_screener_raw.csv)
- **Effect of the price-filter correction:** removing the $2 filter barely changed small-cap results. For example, A at 60 days moved from −1.56% (N 2,984) to −1.48% (N 3,080), and D at 60 days from −0.32% to −0.36%. — [v1 event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results_smallv1_price2filter/event_stats.csv); [v2 event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv)

**Data**
- `yf.download(..., auto_adjust=True)` from 2003-01-01 with an end date of 2026-10-30 (exclusive). The 2026-10-30 bar was a partial intraday bar at run time and was excluded. All tickers are aligned to SPY's trading calendar. — [download.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/download.py); [engine.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/engine.py)

**Signal definitions, fixed before results** — [engine.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/engine.py)
- 50-day average volume is the mean over t−50..t−1, so day t is excluded.
- **A:** close_t > max(High over t−252..t−1).
- **B:** A, and Volume_t ≥ 2× the 50-day average.
- **C:** the 20-day (max High − min Low)/Close is at or below the 10th percentile of its trailing 252 values as of t−1; close_t > max(High over t−20..t−1); Volume_t ≥ 1.5× the average.
- **D:** Open_t ≥ 1.04 × Close_{t−1}, and Volume_t ≥ 3× the average.
- **E:** buy at the open after close > prior 55-day high; sell at the open after close < prior 20-day low.
- **Eligibility for every signal:** prior-50-day average dollar volume of at least $1M. This is a liquidity filter, not a price filter.

**Measurement, fixed before results** — [event_study.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/event_study.py)
- Entry at open t+1, exit at close t+h, for h ∈ {1, 5, 20, 60}. h = 1 is a same-day round trip.
- Per-ticker, per-horizon blackout: a new event is accepted only once the previous holding window has ended, so N differs by horizon.
- Two t-statistics: SEs clustered by signal date, and monthly-averaged returns with Newey-West SEs (lag = ceil(h/21)).
- Costs: 10 bps round trip for large caps, 50 bps for small caps.
- Two survivorship controls: the unconditional mean over all eligible stock-days ("baseline"), and the event return minus the same-window equal-weight return of all eligible universe members ("vs-EW").

**Survivorship controls**
- **Random-entry baseline vs SPY, large caps:** +0.09% (5d), +0.34% (20d), +1.03% (60d). By period: +1.68% per 60 days in 2005–15 and +0.44% in 2016–26.
- **Random-entry baseline vs SPY, small caps:** −0.09% (5d), −0.31% (20d), −0.87% (60d). By period: −0.42% per 60 days in 2005–15 and −1.07% in 2016–26. — [baseline.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/baseline.csv)
- **Buy-and-hold over 2005-01-03 to 2026-10-29:** SPY returned 10.8% CAGR (max drawdown −55.2%). A daily-rebalanced equal-weight portfolio of the large universe returned 16.3% (MaxDD −50.5%); for the small universe, 8.7% (MaxDD −62.5%). — [benchmarks.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/benchmarks.csv)

**Data quality, with cleaning rules fixed before results** — [data_quality.json](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/data_quality.json); [extras.txt](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/extras.txt); [gap_check.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/gap_check.csv)
- **Large caps (2,666,164 bars):**
  - 4,250 zero-volume bars, treated as missing volume.
  - 1 bar with inconsistent OHLC.
  - 1 bar removed by the one-day spike-reversal rule (HOOD 2021-08-04). This was a real meme spike (175.8M shares) and therefore a false positive of the rule, but HOOD had too little history on that date for any signal, so results are unaffected.
- **Small caps (1,265,848 bars):**
  - 21,760 zero-volume bars.
  - 2,189 bars with the open outside the day's high–low range. All of them come from one ticker, CBIO (2014–2022). The rule rejecting D events with such bars rejected 0 D candidates.
  - 15 spike-reversal bars removed (for example UVE 2003-08-19, MITK 2009, ASTH 2012–2016, FDUS/GIII/TCPC on 2020-03-18).
  - 52 moves of more than 3x in a day that did not revert (ASTH, OGG, UVE, MITK, RIGL, ANIP, mostly 2005–2015, when these were illiquid). They were left in, and median and winsorized statistics are reported alongside means.
- **Gap check (D events):** every D event with an adjusted gap above 25% (74 large, 178 small) was re-checked against Yahoo's unadjusted (`auto_adjust=False`) open and close. Exactly one is an adjustment artifact: DHR on 2016-07-05, where the adjusted series jumps from 41.9 to 67.6 at the Fortive spin-off while the unadjusted gap is −0.2%. It also creates fake A/B events. It is left in the pre-declared results (1 of 3,539 D events at 60 days) and excluded in the exploratory sensitivity.
- **Other large gaps:** most correspond to real news on recognizable dates (C 2008-11-24, MS 2008-10-13, BLDR 2015-04-13, VRTX 2013-04-19; small caps SBET 2025-05-27, NVAX 2024-05-10). Others (DMRA 2025-10-07 at +571%, MRNA 2026-08-19 at +84%) show matching huge volume, but I could not verify them.

**Runtime:** the download took about 2 minutes, the A–D event study about 15 seconds, and the Donchian portfolio simulations (120 runs) about 5.4 minutes. Total compute was about 10 minutes.

### Inferences
- Because random large-cap entries beat SPY by about 1% per 60 days (more in 2005–15), large-cap excess returns of +0.2% to +1.4% for A, B and C are mostly universe drift, not signal. The vs-EW column is the honest test.
- The current-size selection for small caps biases in both directions. For breakout signals specifically, removing stocks that graduated to large cap is probably the larger effect: those graduates would have produced many successful breakouts. The negative small-cap baseline, −0.87% per 60 days despite survivorship, is consistent with that. Small-cap results are therefore not a clean test either way.
- Yahoo daily data was clean enough for this purpose in large caps. In small caps the problems are concentrated in a few tickers during illiquid periods, and the $1M dollar-volume eligibility filter keeps most of them out of events.

### Gaps
- No point-in-time index membership or delisted-stock data was available, because Wikipedia and CRSP-type sources were not reachable. The size of the survivorship bias cannot be measured, only bounded indirectly with the baseline and vs-EW controls.
- The large-cap list is from model knowledge and may be off by a few names. Reasons for the 10 download failures (renames, acquisitions or Yahoo outages) were not verified.
- Market caps are current, not historical. A 2005 "small cap" in this sample may have been a microcap or a mid cap at the time.
- Actual bid-ask spreads were not measured. The 10 bps and 50 bps cost assumptions are assumptions.

## 2. Which of the event signals A–D predicted excess returns?

### Takeaway
- **Large caps:**
  - **A (plain 52-week high):** no edge. It underperformed the random-entry baseline, and vs-EW it is negative at 60 days: −0.14% event-weighted, and −0.76% month-weighted (NW t −1.96).
  - **B (52-week high with 2× volume):** positive vs SPY (+1.38% at 60 days), but under the conservative test the gain over the equal-weight universe is +0.14% with t = 0.33.
  - **C (volatility contraction):** worked only in 2005–2015.
  - **D (gap of at least 4% on at least 3× volume):** the strongest result, at +2.31% vs SPY and +1.23% vs-EW over 60 days. Under conservative monthly NW SEs its vs-EW t is only about 1.9, and it is concentrated in a few later-famous winners.
- **Small caps:** nothing beat the equal-weight universe significantly, and after 50 bps costs every signal is negative vs SPY.

### Cited Findings
Source for both main tables: [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv); [baseline.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/baseline.csv); rendered in [tables.md](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/tables.md).

#### Main table, large caps (493 current S&P 500 names). Excess vs SPY in %; net = after 10 bps round trip; h = 1 is a same-day trade

| Sig | h | N | Mean | Median | Hit % | t (date-cl) | t (monthly NW) | Net mean | Net hit % | Winsor. 1/99 mean | vs-EW mean (date-cl t) | Random-entry baseline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1 | 85412 | -0.03 | -0.02 | 48.9 | -2.97 | -2.88 | -0.13 | 44.5 | -0.03 | -0.03 (-4.01) | 0.02 |
| A | 5 | 44515 | -0.00 | -0.02 | 49.5 | -0.11 | -1.33 | -0.10 | 47.8 | -0.02 | -0.07 (-3.19) | 0.09 |
| A | 20 | 24699 | 0.21 | 0.07 | 50.5 | 3.95 | 0.46 | 0.11 | 49.7 | 0.17 | -0.06 (-1.23) | 0.34 |
| A | 60 | 14142 | 0.71 | 0.25 | 51.1 | 5.91 | 0.47 | 0.61 | 50.7 | 0.57 | -0.14 (-1.25) | 1.03 |
| B | 1 | 9019 | 0.03 | 0.00 | 50.1 | 1.18 | -0.11 | -0.07 | 47.2 | 0.03 | 0.02 (0.75) | 0.02 |
| B | 5 | 7580 | 0.12 | -0.01 | 49.9 | 2.26 | 1.07 | 0.02 | 48.7 | 0.09 | 0.04 (0.70) | 0.09 |
| B | 20 | 6788 | 0.56 | 0.22 | 51.9 | 5.40 | 1.52 | 0.46 | 51.1 | 0.51 | 0.24 (2.33) | 0.34 |
| B | 60 | 5796 | 1.38 | 0.73 | 53.2 | 7.10 | 2.43 | 1.28 | 52.8 | 1.24 | 0.52 (2.77) | 1.03 |
| C | 1 | 5895 | 0.08 | 0.01 | 50.4 | 2.83 | 1.03 | -0.02 | 46.7 | 0.07 | 0.08 (2.84) | 0.02 |
| C | 5 | 5542 | 0.19 | 0.04 | 50.5 | 3.33 | 1.40 | 0.09 | 49.3 | 0.16 | 0.14 (2.40) | 0.09 |
| C | 20 | 5382 | 0.52 | 0.25 | 51.6 | 4.45 | 2.04 | 0.42 | 51.0 | 0.47 | 0.21 (1.87) | 0.34 |
| C | 60 | 4745 | 1.03 | 0.34 | 51.4 | 4.60 | 3.03 | 0.93 | 51.0 | 0.83 | 0.15 (0.70) | 1.03 |
| D | 1 | 4000 | 0.09 | 0.04 | 50.8 | 1.38 | 1.94 | -0.01 | 48.9 | 0.06 | 0.07 (1.19) | 0.02 |
| D | 5 | 3887 | 0.26 | 0.12 | 51.4 | 1.77 | 3.30 | 0.16 | 50.4 | 0.17 | 0.15 (1.13) | 0.09 |
| D | 20 | 3783 | 0.88 | 0.41 | 52.8 | 4.75 | 3.47 | 0.78 | 52.0 | 0.74 | 0.46 (2.62) | 0.34 |
| D | 60 | 3539 | 2.31 | 0.78 | 53.0 | 6.42 | 3.67 | 2.21 | 52.4 | 1.90 | 1.23 (3.59) | 1.03 |

#### Main table, small caps (311 current $300M–$2B names). Excess vs SPY in %; net = after 50 bps round trip

| Sig | h | N | Mean | Median | Hit % | t (date-cl) | t (monthly NW) | Net mean | Net hit % | Winsor. mean | vs-EW mean (date-cl t) | Random-entry baseline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1 | 15177 | -0.14 | -0.10 | 47.4 | -4.39 | -5.50 | -0.64 | 33.9 | -0.15 | -0.08 (-2.88) | -0.04 |
| A | 5 | 8210 | -0.24 | -0.34 | 45.9 | -3.01 | -2.40 | -0.74 | 40.2 | -0.29 | -0.10 (-1.37) | -0.09 |
| A | 20 | 4924 | -0.77 | -0.94 | 45.1 | -3.89 | -1.66 | -1.27 | 42.4 | -0.91 | -0.15 (-0.83) | -0.31 |
| A | 60 | 3080 | -1.48 | -2.85 | 42.1 | -3.36 | -1.09 | -1.98 | 40.6 | -1.86 | 0.17 (0.40) | -0.87 |
| B | 1 | 3513 | -0.25 | -0.23 | 46.5 | -3.18 | -4.75 | -0.75 | 38.1 | -0.24 | -0.20 (-2.71) | -0.04 |
| B | 5 | 2630 | -0.25 | -0.51 | 46.0 | -1.50 | -0.98 | -0.75 | 41.3 | -0.29 | -0.10 (-0.60) | -0.09 |
| B | 20 | 2177 | -0.26 | -1.06 | 45.7 | -0.74 | -0.97 | -0.76 | 43.8 | -0.44 | 0.28 (0.86) | -0.31 |
| B | 60 | 1755 | -0.84 | -2.55 | 42.7 | -1.35 | -0.25 | -1.34 | 41.5 | -1.28 | 0.57 (0.96) | -0.87 |
| C | 1 | 2314 | 0.00 | -0.12 | 47.8 | 0.03 | 0.50 | -0.50 | 37.8 | -0.00 | 0.07 (0.94) | -0.04 |
| C | 5 | 2139 | -0.02 | -0.31 | 46.8 | -0.14 | 0.05 | -0.52 | 42.6 | -0.05 | 0.07 (0.49) | -0.09 |
| C | 20 | 2046 | -0.79 | -1.45 | 44.0 | -2.30 | -0.99 | -1.29 | 42.0 | -0.85 | -0.18 (-0.57) | -0.31 |
| C | 60 | 1746 | -2.03 | -3.75 | 41.4 | -3.25 | -1.19 | -2.53 | 40.1 | -2.24 | -0.12 (-0.21) | -0.87 |
| D | 1 | 2453 | -0.23 | -0.39 | 46.0 | -1.61 | -1.88 | -0.73 | 40.8 | -0.24 | -0.14 (-1.01) | -0.04 |
| D | 5 | 2229 | -0.10 | -0.69 | 46.4 | -0.37 | 0.32 | -0.60 | 43.5 | -0.25 | 0.05 (0.19) | -0.09 |
| D | 20 | 2075 | -0.23 | -1.57 | 44.5 | -0.51 | 0.54 | -0.73 | 42.6 | -0.39 | 0.07 (0.17) | -0.31 |
| D | 60 | 1825 | -0.36 | -4.06 | 42.0 | -0.44 | -0.75 | -0.86 | 40.6 | -0.88 | 0.23 (0.30) | -0.87 |

#### vs-EW with conservative SEs (post-hoc diagnostic, added after seeing the table above)
Each cell is the monthly-averaged vs-EW mean in % (Newey-West t). — [vsew_monthly.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/vsew_monthly.csv)

| Universe | Sig | 5d | 20d | 60d |
|---|---|---|---|---|
| large | A | -0.12 (-2.35) | -0.21 (-1.53) | -0.76 (-1.96) |
| large | B | 0.05 (0.53) | 0.03 (0.14) | 0.14 (0.33) |
| large | C | 0.09 (0.84) | 0.11 (0.62) | 0.19 (0.49) |
| large | D | 0.30 (2.50) | 0.43 (1.90) | 0.82 (1.91) |
| small | A | -0.03 (-0.28) | 0.07 (0.25) | 0.31 (0.51) |
| small | B | 0.07 (0.32) | 0.11 (0.26) | 0.74 (0.98) |
| small | C | 0.13 (0.53) | -0.20 (-0.38) | -0.43 (-0.52) |
| small | D | 0.23 (0.88) | 0.60 (1.26) | -0.13 (-0.16) |

**Per-signal results**
- **A, large caps:** the excess vs SPY at 20 and 60 days looks highly significant with date clustering (t 3.95 and 5.91), but the monthly NW t is only 0.46 and 0.47. The means (+0.21% and +0.71%) sit below the random-entry baseline (+0.34% and +1.03%). — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv)
- **B, large caps:** vs-EW is +0.24% (20d) and +0.52% (60d) per event with date-clustered t of 2.33 and 2.77. Equal-weighting months shrinks this to +0.03% and +0.14% (t 0.14 and 0.33), so the event-weighted gain comes from months crowded with B events. — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv); [vsew_monthly.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/vsew_monthly.csv)
- **D, large caps:** the 60-day mean of +2.31% compares with a median of +0.78% and a hit rate of 53.0%. The return distribution is right-skewed, and 11 of 3,539 events had more than 100% excess in 60 days. — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv); [fragility.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/fragility.csv)
- **All small-cap signals:** the 1-day excess (open to close of t+1) is negative: A −0.14% (t −4.39), B −0.25% (t −3.18), D −0.23% (t −1.61). — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv)

### Inferences
- Date-clustered t-statistics overstate significance for 20- and 60-day horizons. Events on neighbouring dates share most of their holding windows, and date clustering does not account for that. The monthly NW t is the more credible number, and under it only large-cap D, and A in the negative direction, come near |t| ≈ 2 against the equal-weight universe.
- The classic "buy the new 52-week high" (A) shows no measurable edge in liquid US large caps over 2005–2026 once universe drift is removed. Adding volume (B) improves the raw numbers, but not robustly.
- Large-cap D behaves like a delayed reaction to news (gap-ups on heavy volume are often earnings or deal news). This is an interpretation: the data contain no earnings dates. The remaining drift after entry is modest (about +0.4% to +0.8% vs EW over 20–60 days) and noisy.
- Small-cap breakouts tended to give back a little the next day and showed no reliable follow-through. With 50 bps costs, none would have made money relative to SPY in this sample.

### Gaps
- There are no earnings or news timestamps, so D cannot be separated into earnings and non-earnings gaps.
- Signal definitions were not varied (by design). Whether nearby parameter choices behave similarly is untested, apart from the one exploratory D sensitivity in section 3.

## 3. Signal D: how much of the move happened before a next-day entry, and is D driven by giant gaps?

### Takeaway
By the next morning, most of the measurable move is already gone. Large-cap D events had gapped up a mean of +8.97% and then added +1.07% from open to close on day t, which is +1.01% above SPY with t 8.76. The next-day open-to-close excess is only +0.09%. The large-cap 60-day drift holds up when gaps above 25% are excluded (exploratory). Small-cap D shows +2.03% excess on day t and nothing afterward.

### Cited Findings
Source: [D_dayt.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/D_dayt.csv)

| Universe | Subset | N | Gap mean | Gap median | Day-t open→close mean | Day-t O→C median | Day-t O→C excess vs SPY | Day-t hit % | t (date-cl) | Next-day 'go' (t+1 O→C) excess | Gaps > 25% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| large | all | 4000 | 8.97 | 7.27 | 1.07 | 0.92 | 1.01 | 59.5 | 8.76 | 0.09 | 74 |
| large | 2005-15 | 1976 | 8.50 | 6.89 | 1.35 | 0.90 | 1.25 | 61.0 | 8.52 | 0.16 | 32 |
| large | 2016-26 | 2024 | 9.44 | 7.76 | 0.81 | 0.96 | 0.78 | 58.0 | 4.38 | 0.01 | 42 |
| small | all | 2453 | 12.38 | 8.45 | 2.06 | 1.72 | 2.03 | 60.0 | 8.60 | -0.23 | 178 |
| small | 2005-15 | 633 | 9.67 | 7.52 | 1.63 | 1.18 | 1.60 | 59.9 | 5.02 | -0.31 | 22 |
| small | 2016-26 | 1820 | 13.33 | 8.86 | 2.21 | 2.01 | 2.17 | 60.1 | 7.32 | -0.20 | 156 |

#### Exploratory sensitivity: D excluding gaps above 25% and the DHR spin-off artifact
Source: [tables.md](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/tables.md)

| Universe | h | N | Mean excess % | Median | t (date-cl) | vs-EW % (t) |
|---|---|---|---|---|---|---|
| large | 5 | 3820 | 0.25 | 0.13 | 1.75 | 0.15 (1.11) |
| large | 20 | 3719 | 0.83 | 0.41 | 4.69 | 0.41 (2.46) |
| large | 60 | 3485 | 2.14 | 0.77 | 6.40 | 1.06 (3.34) |
| small | 5 | 2075 | -0.06 | -0.65 | -0.22 | 0.10 (0.37) |
| small | 20 | 1933 | -0.03 | -1.49 | -0.06 | 0.26 (0.62) |
| small | 60 | 1716 | -0.40 | -4.15 | -0.49 | 0.17 (0.22) |

### Inferences
- The day-t open-to-close gain is not a tradable "go" result. The 3× volume condition is only known at the close, so buying at the day-t open uses information that wasn't available yet, and selling the same day would be a day trade. The only rule tradable without day trading is the next-open entry, and it captures roughly nothing in the first day.
- What a next-open entry can capture in large caps is the slower post-event drift, worth about +0.4% to +0.8% vs EW over 20–60 days, with roughly 52–53% of trades beating SPY. In small caps that drift is not measurable.

### Gaps
- Pre-market and after-hours prices are not in daily bars, so I could not measure how much of the "gap" was tradable pre-market.

## 4. How did the Donchian 55/20 trend trade (E) perform?

### Takeaway
In large caps, trades look attractive in isolation: profit factor 1.65, average win +13.1% against average loss −6.4%. But the excess vs SPY per trade is only +0.54% (t 1.17), and close to zero in 2016–26. A 20-slot equal-weight portfolio compounded at 9.7% vs 10.8% for SPY, with a smaller max drawdown (−44% vs −55%). It lagged far behind the survivorship-inflated equal-weight universe (16.3%). In small caps the trade is break-even before benchmarking (profit factor 1.00), −1.94% per trade vs SPY, and the portfolio compounded at about 1% with drawdowns of −64% to −80%.

### Cited Findings
Source: [donchian_trade_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/donchian_trade_stats.csv); [donchian.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/donchian.py)

#### E trade-level statistics, net of costs (10 / 50 bps). Trades still open on 2026-10-29 are closed at the last close: 150 large, 65 small

| Universe | Subset | Trades | Win % | Avg win % | Avg loss % | Profit factor | Mean net % | Median net % | Avg hold (days) | Mean net excess vs SPY % | Excess hit % | t (monthly NW) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| large | all | 20565 | 44.4 | 13.14 | -6.39 | 1.65 | 2.29 | -1.27 | 50.4 | 0.54 | 40.0 | 1.17 |
| large | 2005-15 | 9597 | 45.2 | 12.73 | -6.23 | 1.68 | 2.34 | -1.09 | 52.2 | 1.05 | 42.7 | 1.83 |
| large | 2016-26 | 10968 | 43.8 | 13.51 | -6.52 | 1.62 | 2.26 | -1.48 | 49.0 | 0.08 | 37.7 | -0.43 |
| large | SPY>200d | 17768 | 45.0 | 13.03 | -6.07 | 1.76 | 2.53 | -1.13 | 50.7 | 0.66 | 39.9 | 2.75 |
| large | SPY<200d | 2797 | 40.7 | 13.92 | -8.26 | 1.16 | 0.78 | -2.47 | 48.6 | -0.24 | 40.8 | -1.32 |
| small | all | 6094 | 34.4 | 20.02 | -10.52 | 1.00 | -0.00 | -4.55 | 45.1 | -1.94 | 29.7 | -3.80 |
| small | 2005-15 | 1783 | 36.3 | 16.94 | -9.45 | 1.02 | 0.14 | -3.96 | 46.8 | -0.84 | 33.2 | -1.70 |
| small | 2016-26 | 4311 | 33.7 | 21.39 | -10.95 | 0.99 | -0.06 | -4.81 | 44.5 | -2.40 | 28.3 | -3.60 |
| small | SPY>200d | 5353 | 34.8 | 19.45 | -10.40 | 1.00 | 0.00 | -4.47 | 45.3 | -2.03 | 29.5 | -4.04 |
| small | SPY<200d | 741 | 31.6 | 24.55 | -11.38 | 1.00 | -0.04 | -5.39 | 44.2 | -1.31 | 31.3 | -0.75 |

#### E portfolio, 2005-01-03 to 2026-10-29
Rules: equity divided by K at each entry; idle cash earns 0%; same-day entries are ordered randomly, with 20 seeds per row. — [donchian_portfolio.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/donchian_portfolio.csv); [benchmarks.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/benchmarks.csv)

| Universe | Max positions K | CAGR median % | CAGR range across seeds % | MaxDD median % | MaxDD range % | Avg positions held |
|---|---|---|---|---|---|---|
| large | 20 | 9.7 | 8.1 to 11.6 | -44.3 | -46.3 to -38.7 | 18.8 |
| large | 10 | 10.0 | 7.6 to 11.0 | -45.4 | -51.0 to -40.8 | 9.6 |
| large | 5 | 8.4 | 4.8 to 9.7 | -53.8 | -64.5 to -46.9 | 4.8 |
| small | 20 | 0.9 | -0.5 to 2.1 | -63.7 | -69.6 to -58.8 | 16.8 |
| small | 10 | -0.1 | -4.6 to 4.9 | -69.4 | -77.8 to -57.5 | 8.9 |
| small | 5 | -2.6 | -8.5 to 2.7 | -80.5 | -89.4 to -72.4 | 4.6 |
| benchmark | SPY buy and hold | 10.8 | – | -55.2 | – | – |
| benchmark | EW large universe, daily rebalanced (survivorship-inflated) | 16.3 | – | -50.5 | – | – |
| benchmark | EW small universe, daily rebalanced (survivorship-inflated) | 8.7 | – | -62.5 | – | – |

### Inferences
- E's high profit factor comes from riding the general upward drift of surviving large caps. It does not beat SPY or a random selection of the same stocks. Its real benefit is a somewhat smaller drawdown than SPY at K = 10–20, which disappears at K = 5.
- The spread of CAGR across random tie-break seeds is wide: 4.8–9.7% at K = 5 in large caps, and −8.5% to +2.7% in small caps. Which signals happened to get a slot matters about as much as the rule itself, and that gets worse with fewer positions.

### Gaps
- Cash was assumed to earn 0%, so CAGR is understated by the T-bill yield times the average idle share. With an average of 18.8 of 20 slots filled in large caps, that idle share is small.
- No volatility-based position sizing (the classic turtle approach) was tested. Equal-weight sizing was declared in advance.

## 5. How fragile are the results (period, regime, size, outliers, concentration, data errors)?

### Takeaway
- **Period:** A, C and the Donchian trade (E) showed their large-cap excess vs SPY only in 2005–2015 and were roughly zero in 2016–2026 (E per trade: +1.05% then +0.08%). Large-cap B and D are positive in both periods vs SPY and vs EW.
- **Regime:** bear-regime (SPY below its 200-day average) samples are small.
- **Outliers and concentration:** large-cap D and B depend heavily on a handful of tickers whose S&P 500 membership is itself a consequence of the runs measured. Without the top 10 tickers, D's vs-EW falls to +0.45% (t 1.57) and B's to +0.18% (t 1.06).

### Cited Findings
#### Robustness splits, mean excess vs SPY % (date-clustered t) [N]
The base rows are the random-entry baseline for each subset. — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv); [baseline.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/baseline.csv)

Large caps:

| Sig | h | 2005-15 | 2016-26 | SPY>200d | SPY<200d |
|---|---|---|---|---|---|
| A | 5 | -0.01 (-0.2) [21450] | 0.00 (0.0) [23065] | 0.01 (0.4) [42430] | -0.25 (-1.6) [2085] |
| A | 20 | 0.39 (6.2) [11970] | 0.05 (0.6) [12729] | 0.24 (4.4) [23374] | -0.29 (-1.1) [1325] |
| A | 60 | 1.41 (9.9) [6798] | 0.06 (0.3) [7344] | 0.74 (6.0) [13314] | 0.13 (0.3) [828] |
| B | 5 | 0.03 (0.5) [4061] | 0.23 (2.4) [3519] | 0.13 (2.4) [7205] | 0.03 (0.1) [375] |
| B | 20 | 0.65 (5.7) [3577] | 0.47 (2.6) [3211] | 0.56 (5.2) [6451] | 0.62 (1.3) [337] |
| B | 60 | 1.91 (8.6) [2987] | 0.82 (2.5) [2809] | 1.35 (6.8) [5508] | 2.09 (2.2) [288] |
| C | 5 | 0.31 (4.2) [3063] | 0.05 (0.6) [2479] | 0.20 (3.3) [5361] | 0.10 (0.3) [181] |
| C | 20 | 0.83 (5.8) [2961] | 0.14 (0.7) [2421] | 0.53 (4.5) [5203] | 0.21 (0.3) [179] |
| C | 60 | 1.84 (6.9) [2558] | 0.08 (0.2) [2187] | 1.04 (4.6) [4576] | 0.64 (0.6) [169] |
| D | 5 | 0.37 (2.4) [1935] | 0.14 (0.6) [1952] | 0.19 (2.2) [3207] | 0.57 (0.8) [680] |
| D | 20 | 1.00 (4.5) [1886] | 0.75 (2.6) [1897] | 0.83 (5.0) [3140] | 1.11 (1.5) [643] |
| D | 60 | 2.62 (6.2) [1761] | 2.00 (3.4) [1778] | 1.79 (5.1) [2931] | 4.78 (4.0) [608] |
| base | 5 | 0.15 | 0.04 | 0.07 | 0.19 |
| base | 20 | 0.57 | 0.14 | 0.27 | 0.63 |
| base | 60 | 1.68 | 0.44 | 0.83 | 1.84 |

Small caps:

| Sig | h | 2005-15 | 2016-26 | SPY>200d | SPY<200d |
|---|---|---|---|---|---|
| A | 5 | -0.08 (-0.8) [2831] | -0.33 (-3.0) [5379] | -0.22 (-2.7) [7799] | -0.66 (-1.8) [411] |
| A | 20 | -0.16 (-0.6) [1665] | -1.08 (-4.0) [3259] | -0.74 (-3.7) [4658] | -1.32 (-1.4) [266] |
| A | 60 | -0.14 (-0.3) [1021] | -2.15 (-3.6) [2059] | -1.56 (-3.6) [2895] | -0.21 (-0.1) [185] |
| B | 5 | 0.29 (1.4) [897] | -0.53 (-2.3) [1733] | -0.18 (-1.1) [2468] | -1.27 (-1.8) [162] |
| B | 20 | 0.38 (1.0) [738] | -0.58 (-1.2) [1439] | -0.22 (-0.6) [2041] | -0.81 (-0.7) [136] |
| B | 60 | 0.61 (0.8) [593] | -1.58 (-1.8) [1162] | -0.98 (-1.6) [1640] | 1.20 (0.4) [115] |
| C | 5 | 0.55 (2.6) [699] | -0.30 (-1.4) [1440] | 0.02 (0.1) [2049] | -0.89 (-1.0) [90] |
| C | 20 | 0.16 (0.3) [667] | -1.24 (-2.8) [1379] | -0.76 (-2.2) [1960] | -1.29 (-0.8) [86] |
| C | 60 | -0.00 (-0.0) [558] | -2.98 (-3.6) [1188] | -1.91 (-3.0) [1666] | -4.48 (-1.9) [80] |
| D | 5 | 0.06 (0.2) [601] | -0.16 (-0.5) [1628] | -0.21 (-0.8) [1894] | 0.50 (0.5) [335] |
| D | 20 | 0.33 (0.6) [566] | -0.44 (-0.8) [1509] | -0.55 (-1.2) [1767] | 1.60 (1.2) [308] |
| D | 60 | -0.84 (-0.8) [511] | -0.17 (-0.2) [1314] | -0.78 (-0.9) [1548] | 1.97 (0.9) [277] |
| base | 5 | -0.03 | -0.12 | -0.11 | 0.01 |
| base | 20 | -0.15 | -0.38 | -0.43 | 0.21 |
| base | 60 | -0.42 | -1.07 | -1.28 | 0.95 |

#### vs-EW by split, mean % (date-clustered t)
Source: [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv)

| Univ | Sig | h | 2005-15 | 2016-26 | SPY>200d | SPY<200d |
|---|---|---|---|---|---|---|
| large | A | 60 | -0.08 (-0.6) | -0.20 (-1.1) | -0.07 (-0.6) | -1.31 (-2.6) |
| large | B | 60 | 0.45 (2.1) | 0.59 (1.9) | 0.51 (2.7) | 0.61 (0.7) |
| large | C | 60 | 0.12 (0.4) | 0.19 (0.5) | 0.19 (0.9) | -0.93 (-0.9) |
| large | D | 20 | 0.43 (2.0) | 0.48 (1.7) | 0.45 (2.8) | 0.49 (0.7) |
| large | D | 60 | 0.92 (2.3) | 1.54 (2.8) | 0.99 (2.9) | 2.41 (2.2) |
| small | B | 60 | 1.35 (1.9) | 0.17 (0.2) | 0.49 (0.8) | 1.64 (0.6) |
| small | D | 60 | -0.50 (-0.5) | 0.51 (0.5) | 0.13 (0.2) | 0.78 (0.4) |

The monthly-NW versions of the period splits (post-hoc) for large D at 60 days are +0.86% (t 1.65) in 2005–15 and +0.79% (t 1.15) in 2016–26. — [vsew_monthly.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/vsew_monthly.csv)

#### Outliers, years and crowded dates (post-hoc diagnostics)
Source: [fragility.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/fragility.csv); [extras.txt](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/extras.txt)

| Large caps | Years with vs-EW > 0 | vs-EW excl. 2008, 2009, 2020 (t) | vs-EW excl. 10 most crowded dates | Mean exc vs SPY → after dropping best 1% of events | vs-EW excl. top-10 tickers (t) |
|---|---|---|---|---|---|
| A 60d | 11/22 | -0.14 (-1.21) | -0.16 | 0.71 → 0.14 | – |
| B 20d | 15/22 | 0.24 (2.35) | 0.23 | 0.56 → 0.23 | – |
| B 60d | 16/22 | 0.59 (3.13) | 0.55 | 1.38 → 0.74 | 0.18 (1.06) |
| C 60d | 11/22 | 0.19 (0.85) | 0.16 | 1.03 → 0.31 | – |
| D 20d | 17/22 | 0.45 (2.83) | 0.48 | 0.88 → 0.34 | – |
| D 60d | 15/22 | 0.77 (2.33) | 1.15 | 2.31 → 1.18 | 0.45 (1.57) |

- **Trimming the baseline the same way:** dropping the best 1% of random stock-days cuts the large-cap baseline from +1.03% to +0.37% per 60 days, and from +0.34% to −0.00% per 20 days. On a like-for-like basis, D (60d) stays about 0.8 percentage points above baseline (1.18 vs 0.37), B about 0.4 (0.74 vs 0.37), and A and C are at or below baseline (0.14 and 0.31). — [extras.txt](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/extras.txt)
- **Ticker concentration:** in large-cap D at 60 days, the top 10 of 454 tickers contribute 65% of summed vs-EW excess. CVNA alone contributes 8.99 of 43.54 (about 21%), followed by SMCI, TSLA, AIG, MNST, FSLR, MRNA, FANG, NVDA and COIN. In B at 60 days the top 10 contribute 67%: APP, AMD, SMCI, MRNA, TSLA, NVDA, MU, NFLX, AXON, MNST. — [extras.txt](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/extras.txt)
- **Clustering by date:** about 5–7% of events in each large-cap signal fall on the 1% busiest signal dates. Removing the 10 most crowded dates barely changes the means (table above). — [fragility.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/fragility.csv)
- **Bear-regime samples are small:** large-cap C has only 169–181 events below SPY's 200-day average, and B has 288–375. The bear-regime D figure (+4.78% vs SPY at 60 days, N 608) compares with a bear-regime baseline of +1.84%. — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv); [baseline.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/baseline.csv)
- **Data errors:** the DHR spin-off artifact is 1 event, and the exploratory exclusion of gaps above 25% leaves large-cap D essentially unchanged (vs-EW at 60 days +1.06%, t 3.34). — [gap_check.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/gap_check.csv); [tables.md](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/tables.md)

### Inferences
- **Most robust:** large-cap D at 20–60 days. It is positive in both periods, both regimes, 15–17 of 22 years, after excluding giant gaps, and with crisis years removed. But its strength depends on the test: monthly NW t ≈ 1.9 vs EW, and it falls to t ≈ 1.6 without the top 10 tickers. Several of those tickers (CVNA, SMCI, COIN, APP) entered the S&P 500 only after the runs measured here, so a point-in-time universe would very likely show a smaller effect.
- **Weakest:** A (no edge anywhere) and C (an early-period effect that disappeared after 2015). B is in between: robust across years and periods by event-weighted measures, but not by month-weighted ones, and concentrated in a few winners.
- **Small caps:** none of the small-cap results is distinguishable from zero against the equal-weight universe, and after 50 bps costs none is positive. Survivorship bias flatters these numbers, and they are still not positive. Better small-cap data would be unlikely to show a profitable signal.

### Gaps
- No point-in-time S&P membership, so the look-ahead contribution of names like CVNA, SMCI, APP and COIN cannot be removed cleanly. Dropping the top 10 tickers is only a crude stand-in.
- No sector or industry adjustment. Part of the vs-EW result could be sector momentum (semiconductors, crypto-linked stocks).

## 6. What carries over to a $100 account that cannot day trade? (constraint added by the user)

### Takeaway
Only the 5, 20 and 60-day horizons and the Donchian holds (median 38 days) are usable, because the 1-day horizon and D's day-t move are same-day trades. On those horizons the only candidate with a credible edge is large-cap D. It has a hit rate of about 52–53% vs SPY and a right-skewed payoff, so a $100 account holding a handful of positions would see mostly noise. A 5-slot Donchian portfolio in large caps compounded below SPY with deeper drawdowns, and in small caps it lost money.

### Cited Findings
- In this design, h = 1 means buying at the open of t+1 and selling at that day's close, so it is a same-day round trip. — [event_study.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/event_study.py)
- **Large-cap D, net of 10 bps vs SPY:** 5d +0.16% (net hit 50.4%), 20d +0.78% (52.0%), 60d +2.21% (52.4%). The 60-day median gross is +0.78%. — [event_stats.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/event_stats.csv)
- **Donchian with K = 5 (about $20 per position on a $100 account):**
  - Large caps: median CAGR 8.4% (range 4.8–9.7% across seeds) and median MaxDD −53.8% (worst −64.5%), against SPY at 10.8% and −55.2%.
  - Small caps: median CAGR −2.6% and median MaxDD −80.5% (worst −89.4%). — [donchian_portfolio.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/donchian_portfolio.csv)
- **Price filter:** following the user's clarification, no share-price filter is applied anywhere in the signal rules. The universe-level $2 filter was removed, which changed small-cap results only marginally (see section 1). — [build_universe.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/build_universe.py)

### Inferences
- For a small, non-day-trading account, these tests support at best "next-open entry after a large-cap gap-up on very heavy volume, held for 1–3 months" as a weak, noisy tilt. They do not support plain 52-week-high or volatility-contraction breakouts, or any small-cap breakout rule. A broad index fund beat every portfolio-level breakout implementation tested here on CAGR.
- With 5 or fewer concurrent positions, the luck of which signals get funded (a CAGR spread of about 5 points across seeds in large caps and 11 points in small caps) is as large as any edge measured.

### Gaps
- Real Robinhood execution costs (spreads on fractional-share orders, opening-auction fills) were not measured, so the 10 and 50 bps assumptions are untested for this account type.
- Whether the no-day-trading constraint is a regulatory one (and its current thresholds) was not researched here. It is taken as given from the user.

## 7. EXPLORATORY: Single-stock cherry-picking check (IREN and peers, user-requested)

### Takeaway
On daily bars, one simple fixed trend rule turned IREN's +616% buy-and-hold into +142%. Across the 11 crypto-miner and AI-hosting peers with data, the same rule had a median return of −19%, against a median buy-and-hold of +159%. It beat buy-and-hold only on CORZ, a short-history name. IREN was the second-best buy-and-hold performer in the group. A marketing claim built on IREN alone therefore mostly reflects having picked one of the biggest ex-post winners. This test does not reproduce the claimed 30-minute strategy.

### Cited Findings
- **The claim** (as relayed in the assignment, not independently verified): an AI-built strategy on IREN using 30-minute bars made 18 trades over about 3.1 years to late October 2026 and returned +725% vs +643% buy-and-hold, with max drawdown −38.6% vs −68.2%, exiting on a close below the 200-period EMA. Yahoo serves only about 60 days of 30-minute data (per the assignment), so the original cannot be replicated here.
- **Rule tested:** buy at the next open after a close above the prior 50-day high; sell at the next open after a close below the 200-day EMA of closes; 0.2% cost per side.
- **Window and accounting:** 2023-09-25 to 2026-10-29. Earlier data is used only to warm up the indicators. Buy-and-hold also pays 0.2% per side, and drawdowns are measured on daily closes. — [iren_peers.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/iren_peers.py)

Source for the table: [iren_peers.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/iren_peers.csv)

| Ticker | Window start | Strategy return % | Buy-and-hold return % | Strategy MaxDD % | B&H MaxDD % | Trades | Time in market % | Note |
|---|---|---|---|---|---|---|---|---|
| IREN | 2023-09-25 | 142 | 616 | -62.1 | -67.4 | 6 | 53 | |
| MARA | 2023-09-25 | -48 | -16 | -82.2 | -78.3 | 9 | 29 | |
| RIOT | 2023-09-25 | -23 | 52 | -56.1 | -66.2 | 9 | 32 | |
| CLSK | 2023-09-25 | -22 | 114 | -82.7 | -71.3 | 7 | 38 | |
| HUT | 2023-09-25 | 115 | 604 | -61.3 | -65.1 | 7 | 57 | Yahoo series spans the Dec-2023 Hut 8 merger; no discontinuity found (largest daily move 23%) |
| CIFR | 2023-09-25 | -19 | 235 | -75.1 | -73.6 | 7 | 55 | |
| WULF | 2023-09-25 | 113 | 855 | -55.6 | -74.6 | 7 | 57 | |
| BTDR | 2023-09-25 | -67 | -37 | -80.1 | -73.9 | 8 | 30 | |
| CORZ | 2024-01-24 | 214 | 159 | -53.6 | -64.9 | 4 | 57 | Yahoo history starts 2024-01-24; no EMA warm-up |
| APLD | 2023-09-25 | -9 | 272 | -59.4 | -71.9 | 6 | 48 | |
| BITF | – | – | – | – | – | – | – | Yahoo returned no data |
| HIVE | 2023-09-25 | -62 | -30 | -69.2 | -77.1 | 11 | 24 | |
| SPY | 2023-09-25 | 54 | 85 | -11.0 | -18.8 | 3 | 87 | reference |
| QQQ | 2023-09-25 | 61 | 103 | -13.6 | -22.8 | 3 | 87 | reference |

- **Medians across peers** — [iren_peers.py output](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/iren_peers.csv):
  - All 11 with data (including IREN and CORZ): strategy −18.6%, buy-and-hold +159%; strategy MaxDD −62.1%, buy-and-hold MaxDD −71.9%. The strategy beat buy-and-hold in 1 of 11 cases and had a shallower drawdown in 7 of 11.
  - The 9 full-history peers excluding IREN: strategy median −21.5% (mean −2.3%), buy-and-hold median +114%. The strategy beat buy-and-hold in 0 of 9 and had a shallower drawdown in 5 of 9.
- **IREN's trades:** of its 6 trades, one (2025-06-09 to 2026-03-09, +254.7%) produced the entire gain. The other five returned −5.9%, −3.2%, −5.9%, +2.1% and −20.1%. — [iren_peers.py](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/iren_peers.py)
- **Buy-and-hold ranking:** WULF +855%, IREN +616%, HUT +604%, APLD +272%, CIFR +235%, CORZ +159% (short window), CLSK +114%, RIOT +52%, MARA −16%, HIVE −30%, BTDR −37%. — [iren_peers.csv](file:///tmp/claude-0/-home-user-retrieval-gate/66298893-a742-58b6-8192-0ee407c352f9/scratchpad/breakout/results/iren_peers.csv)

### Inferences
- A trend rule's absolute return on one stock mostly tracks that stock's buy-and-hold path. The same rule lost money on 7 of 11 peers. A headline built on the second-best performer in a sector that boomed after the fact tells you little about how the rule will perform going forward.
- The drawdown reduction is real but modest and inconsistent: 7 of 11 peers, about 5–20 points. A 200-period EMA on 30-minute bars spans about 15 trading days (13 regular-session bars per day), so the marketed rule exits much faster than the daily 200-EMA tested here. Its smaller drawdown could come from that faster exit, but the same peer-group test would be needed before believing it.

### Gaps
- The marketed rule's entry condition, its exact window, and its 30-minute data could not be obtained, so its +725% and −38.6% figures could not be checked.
- BITF had no Yahoo data, and CORZ's post-bankruptcy listing starts in January 2024. The peer group is therefore 11 names, not 12.
- Only one fixed rule was tested, deliberately. Testing many rules on the same peers would bring back the selection problem this section is meant to expose.
