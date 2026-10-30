"""Fragility checks on the A-D event files (run after event_study.py)."""
import numpy as np, pandas as pd
from event_study import cl_t
BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
rows = []
for uni in ['large', 'small']:
    for s in 'ABCD':
        for h in [5, 20, 60]:
            e = pd.read_csv(f"{BASE}/results/events_{uni}_{s}_h{h}.csv", parse_dates=['date'])
            e['vs'] = e['ret'] - e['ew']
            e['yr'] = e.date.dt.year
            yr = e.groupby('yr')['vs'].mean()
            ex = e[~e.yr.isin([2008, 2009, 2020])]
            cnt = e.groupby('date').size().sort_values(ascending=False)
            top = cnt.iloc[:max(1, int(len(cnt) * 0.01))].sum() / len(e)
            # drop the 10 most crowded dates
            crowded = set(cnt.index[:10])
            d10 = e[~e.date.isin(crowded)]
            # top-decile contribution: mean excess after removing best 1% of events
            q = e.exc.quantile(0.99)
            rows.append(dict(universe=uni, signal=s, h=h, N=len(e), dates=len(cnt),
                             share_events_top1pct_dates=top, vsEW_mean=e.vs.mean(),
                             years_pos=f"{(yr > 0).sum()}/{len(yr)}",
                             vsEW_ex_2008_09_2020=ex.vs.mean(), t_ex=cl_t(ex.vs.values, ex.date),
                             vsEW_drop10dates=d10.vs.mean(),
                             exc_mean=e.exc.mean(), exc_mean_drop_top1pct=e.exc[e.exc < q].mean(),
                             n_abs_exc_gt100pct=int((e.exc.abs() > 1).sum())))
f = pd.DataFrame(rows); f.to_csv(f"{BASE}/results/fragility.csv", index=False)
pd.set_option('display.width', 250)
print(f.round(4).to_string(index=False))
for uni in ['large', 'small']:
    d = pd.read_csv(f"{BASE}/results/events_{uni}_D_dayt.csv", parse_dates=['date'])
    print(uni, 'D gaps >25%:', (d.gap > .25).sum(), 'of', len(d), '; gaps >50%:', (d.gap > .5).sum())
    print(d.nlargest(8, 'gap')[['ticker', 'date', 'gap', 'oc', 'ret', 'exc']].round(3).to_string(index=False))
