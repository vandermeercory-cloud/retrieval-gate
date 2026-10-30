"""Render markdown tables from results/*.csv into results/tables.md."""
import numpy as np, pandas as pd
from event_study import cl_t
BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
R = pd.read_csv(f"{BASE}/results/event_stats.csv"); B = pd.read_csv(f"{BASE}/results/baseline.csv")
p = lambda x, d=2: f"{x*100:.{d}f}"
L = []
for uni in ['large', 'small']:
    L.append(f"\n#### Main table: {uni} caps (excess vs SPY, %, gross unless noted)\n")
    L.append("| Sig | h | N | Mean | Median | Hit % | t(date-cl) | t(monthly NW) | Net mean | Net hit % | Winsor. mean | vs-EW mean (t) | Baseline mean (all stock-days) |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for s in 'ABCD':
        for h in [1, 5, 20, 60]:
            r = R[(R.universe == uni) & (R.signal == s) & (R.h == h) & (R.subset == 'all')].iloc[0]
            b = B[(B.universe == uni) & (B.h == h) & (B.subset == 'all')].iloc[0]
            L.append(f"| {s} | {h} | {int(r.N)} | {p(r['mean'])} | {p(r['median'])} | {r.hit*100:.1f} | {r.t_date:.2f} | {r.t_month:.2f} | {p(r.net_mean)} | {r.net_hit*100:.1f} | {p(r.wins_mean)} | {p(r.vsEW_mean)} ({r.vsEW_t:.2f}) | {p(b['mean'])} |")
for uni in ['large', 'small']:
    L.append(f"\n#### Robustness splits: {uni} caps. Cell = mean excess vs SPY % (date-clustered t) [N]; 'base' row = unconditional mean of all eligible stock-days in that subset\n")
    L.append("| Sig | h | 2005-15 | 2016-26 | SPY>200d | SPY<200d |")
    L.append("|---|---|---|---|---|---|")
    for s in ['A', 'B', 'C', 'D', 'base']:
        for h in [5, 20, 60]:
            cells = []
            for sub in ['2005-15', '2016-26', 'SPY>200d', 'SPY<200d']:
                if s == 'base':
                    b = B[(B.universe == uni) & (B.h == h) & (B.subset == sub)].iloc[0]
                    cells.append(f"{p(b['mean'])}")
                else:
                    r = R[(R.universe == uni) & (R.signal == s) & (R.h == h) & (R.subset == sub)].iloc[0]
                    cells.append(f"{p(r['mean'])} ({r.t_date:.1f}) [{int(r.N)}]")
            L.append(f"| {s} | {h} | " + " | ".join(cells) + " |")
    L.append(f"\n#### vs-EW (stock minus same-window equal-weight universe return) by split: {uni} caps, mean % (date-clustered t)\n")
    L.append("| Sig | h | 2005-15 | 2016-26 | SPY>200d | SPY<200d |")
    L.append("|---|---|---|---|---|---|")
    for s in 'ABCD':
        for h in [20, 60]:
            cells = []
            for sub in ['2005-15', '2016-26', 'SPY>200d', 'SPY<200d']:
                r = R[(R.universe == uni) & (R.signal == s) & (R.h == h) & (R.subset == sub)].iloc[0]
                cells.append(f"{p(r.vsEW_mean)} ({r.vsEW_t:.1f})")
            L.append(f"| {s} | {h} | " + " | ".join(cells) + " |")
D = pd.read_csv(f"{BASE}/results/D_dayt.csv")
L.append("\n#### Signal D: what happened on day t vs. after next-day entry (%)\n")
L.append("| Universe | Subset | N | Gap mean | Gap median | Day-t open->close mean | median | Day-t O->C excess vs SPY | hit % | t | Next-day 'go' (t+1 O->C) excess | Gaps >25% |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in D.itertuples():
    L.append(f"| {r.universe} | {r.subset} | {r.N} | {p(r.gap_mean)} | {p(r.gap_median)} | {p(r.dayt_oc_mean)} | {p(r.dayt_oc_median)} | {p(r.dayt_oc_exc_mean)} | {r.dayt_oc_exc_hit*100:.1f} | {r.dayt_t_date:.2f} | {p(r.next_oc_exc_mean)} | {r.gap_gt_25pct} |")
# exploratory: D excluding gaps > 25%
L.append("\n#### EXPLORATORY sensitivity: signal D excluding events with gap > 25% (and the DHR artifact)\n")
L.append("| Universe | h | N | Mean exc % | Median | t(date) | vs-EW % (t) |")
L.append("|---|---|---|---|---|---|---|")
for uni in ['large', 'small']:
    g = pd.read_csv(f"{BASE}/results/events_{uni}_D_dayt.csv", parse_dates=['date'])
    keep = g[(g.gap <= 0.25) & ~((g.ticker == 'DHR') & (g.date == '2016-07-05'))][['ticker', 'date']]
    for h in [5, 20, 60]:
        e = pd.read_csv(f"{BASE}/results/events_{uni}_D_h{h}.csv", parse_dates=['date']).merge(keep, on=['ticker', 'date'])
        v = e.ret - e.ew
        L.append(f"| {uni} | {h} | {len(e)} | {p(e.exc.mean())} | {p(e.exc.median())} | {cl_t(e.exc.values, e.date):.2f} | {p(v.mean())} ({cl_t(v.values, e.date):.2f}) |")
T = pd.read_csv(f"{BASE}/results/donchian_trade_stats.csv")
L.append("\n#### Signal E (Donchian 55/20) trade-level statistics, net of costs\n")
L.append("| Universe | Subset | Trades | Win % | Avg win % | Avg loss % | Profit factor | Mean net % | Median net % | Avg hold (days) | Mean net excess vs SPY % | Excess hit % | t (monthly NW) |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in T.itertuples():
    L.append(f"| {r.universe} | {r.subset} | {r.trades} | {r.win_rate*100:.1f} | {p(r.avg_win)} | {p(r.avg_loss)} | {r.profit_factor:.2f} | {p(r.mean_net)} | {p(r.median_net)} | {r.avg_hold_days:.1f} | {p(r.mean_net_excess)} | {r.excess_hit*100:.1f} | {r.t_excess_month:.2f} |")
Pf = pd.read_csv(f"{BASE}/results/donchian_portfolio.csv"); Bm = pd.read_csv(f"{BASE}/results/benchmarks.csv")
L.append("\n#### Signal E portfolio (2005-01-03 to 2026-10-29, 20 random tie-break seeds)\n")
L.append("| Universe | Max positions K | CAGR median % | CAGR range % | MaxDD median % | MaxDD range % | Avg positions held |")
L.append("|---|---|---|---|---|---|---|")
for r in Pf.itertuples():
    L.append(f"| {r.universe} | {r.K} | {p(r.CAGR_median,1)} | {p(r.CAGR_min,1)} to {p(r.CAGR_max,1)} | {p(r.MaxDD_median,1)} | {p(r.MaxDD_worst,1)} to {p(r.MaxDD_best,1)} | {r.avg_positions:.1f} |")
for r in Bm.itertuples():
    L.append(f"| {r.universe} benchmark | SPY buy&hold | {p(r.SPY_CAGR,1)} | - | {p(r.SPY_MaxDD,1)} | - | - |")
    L.append(f"| {r.universe} benchmark | EW daily-rebal. universe (survivorship-inflated) | {p(r.EW_CAGR,1)} | - | {p(r.EW_MaxDD,1)} | - | - |")
I = pd.read_csv(f"{BASE}/results/iren_peers.csv")
L.append("\n#### EXPLORATORY: IREN peer group, daily rule (buy after close > 50-day high; sell after close < EMA200), 0.2%/side\n")
L.append("| Ticker | Window start | Strategy return % | Buy&hold return % | Strategy MaxDD % | B&H MaxDD % | Trades | Time in market % | Note |")
L.append("|---|---|---|---|---|---|---|---|---|")
for r in I.itertuples():
    if pd.isna(r.strat_ret):
        L.append(f"| {r.ticker} | - | - | - | - | - | - | - | no Yahoo data |"); continue
    note = 'listed 2024-01-24, no EMA warm-up' if r.ticker == 'CORZ' else ('reference' if r.ticker in ('SPY', 'QQQ') else '')
    L.append(f"| {r.ticker} | {r.first_day} | {r.strat_ret*100:.0f} | {r.bh_ret*100:.0f} | {r.strat_mdd*100:.1f} | {r.bh_mdd*100:.1f} | {int(r.trades)} | {r.time_in_mkt*100:.0f} | {note} |")
open(f"{BASE}/results/tables.md", 'w').write("\n".join(L))
print("\n".join(L))
