"""Monthly-averaged Newey-West t-stats for the vs-EW measure (conservative companion to date-clustered t)."""
import math, pandas as pd
from event_study import nw_t
BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
rows = []
for uni in ['large', 'small']:
    for s in 'ABCD':
        for h in [5, 20, 60]:
            e = pd.read_csv(f"{BASE}/results/events_{uni}_{s}_h{h}.csv", parse_dates=['date'])
            e['vs'] = e.ret - e.ew
            for lab, g in [('all', e), ('2005-15', e[e.date <= '2015-12-31']), ('2016-26', e[e.date >= '2016-01-01'])]:
                mo = g.groupby(g.date.dt.to_period('M')).vs.mean()
                rows.append(dict(universe=uni, signal=s, h=h, subset=lab, vsEW_monthly_mean=mo.mean(), vsEW_t_month=nw_t(mo.values, math.ceil(h / 21))))
r = pd.DataFrame(rows); r.to_csv(f"{BASE}/results/vsew_monthly.csv", index=False)
p = r.pivot_table(index=['universe', 'signal', 'h'], columns='subset', values=['vsEW_monthly_mean', 'vsEW_t_month'])
p['vsEW_monthly_mean'] *= 100
print(p.round(2).to_string())
