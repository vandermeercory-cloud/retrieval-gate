"""Data-error check: for every signal-D event with adjusted gap > 25%, compare with the gap computed
from Yahoo's unadjusted (auto_adjust=False) Open/Close. A large mismatch flags an adjustment artifact
(e.g. spin-off / split mis-adjustment)."""
import pandas as pd, yfinance as yf, numpy as np
BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
out = []
for uni in ['large', 'small']:
    d = pd.read_csv(f"{BASE}/results/events_{uni}_D_dayt.csv", parse_dates=['date'])
    big = d[d.gap > 0.25]
    raw = yf.download(sorted(big.ticker.unique()), start="2004-06-01", end="2026-10-30", auto_adjust=False,
                      progress=False, group_by='ticker', threads=True)
    for r in big.itertuples():
        x = raw[r.ticker][['Open', 'Close']].dropna()
        k = x.index.get_loc(r.date)
        rg = x['Open'].iloc[k] / x['Close'].iloc[k - 1] - 1
        out.append(dict(universe=uni, ticker=r.ticker, date=r.date.date(), adj_gap=r.gap, raw_gap=rg,
                        exc60_na=np.nan, exc1=r.exc))
o = pd.DataFrame(out)
o['mismatch'] = (o.adj_gap - o.raw_gap).abs() > 0.05
o.to_csv(f"{BASE}/results/gap_check.csv", index=False)
print(o.groupby('universe').mismatch.agg(['sum', 'count']))
print(o[o.mismatch].round(3).to_string(index=False))
