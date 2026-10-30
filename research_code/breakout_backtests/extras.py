"""Extra fragility numbers: trimmed means vs trimmed baseline, ticker concentration, universe coverage."""
import numpy as np, pandas as pd, pickle
from engine import BASE, load, matrices, clean, signals
from event_study import cl_t
P, spy, cal = load()
spyO, spyC = spy['Open'].values, spy['Close'].values
for uni in ['large', 'small']:
    n = {y: sum(1 for t, d in P[uni].items() if d.index.min() <= pd.Timestamp(f'{y}-01-05')) for y in [2005, 2010, 2016, 2021]}
    print(uni, 'tickers', len(P[uni]), 'with data by Jan of year:', n)
for uni in ['large', 'small']:
    M, _ = clean(matrices(P[uni], cal)); S = signals(M); elig = S['elig']
    for h in [20, 60]:
        R = M['Close'].shift(-h) / M['Open'].shift(-1) - 1
        spyr = pd.Series(spyC, index=cal).shift(-h) / pd.Series(spyO, index=cal).shift(-1) - 1
        X = R.sub(spyr, axis=0).where(elig)
        ew = R.where(elig).mean(axis=1)
        XE = R.sub(ew, axis=0).where(elig)
        v = X.values[np.isfinite(X.values)]; ve = XE.values[np.isfinite(XE.values)]
        q = np.quantile(v, .99); qe = np.quantile(ve, .99)
        print(f"{uni} h={h} BASELINE mean exc {v.mean()*100:.2f} trimmed(top1% dropped) {v[v<q].mean()*100:.2f} | vsEW mean {ve.mean()*100:.2f} trimmed {ve[ve<qe].mean()*100:.2f}")
        for s in 'ABCD':
            e = pd.read_csv(f"{BASE}/results/events_{uni}_{s}_h{h}.csv", parse_dates=['date'])
            x = e.exc.values; xe = (e.ret - e.ew).values
            tq, tqe = np.quantile(x, .99), np.quantile(xe, .99)
            g = e.assign(vs=xe).groupby('ticker').vs.sum().sort_values(ascending=False)
            share_top10 = g.iloc[:10].sum() / g.sum() if g.sum() > 0 else np.nan
            print(f"   {s}: exc {x.mean()*100:.2f} trimmed {x[x<tq].mean()*100:.2f} | vsEW {xe.mean()*100:.2f} trimmed {xe[xe<tqe].mean()*100:.2f} (t {cl_t(xe[xe<tqe], e.date[xe<tqe]):.2f}) | tickers {e.ticker.nunique()} | top10 tickers share of summed vsEW {share_top10:.2f}")

# ticker concentration of large-cap B and D (h=60)
for s in ['D', 'B']:
    e = pd.read_csv(f"{BASE}/results/events_large_{s}_h60.csv", parse_dates=['date']); e['vs'] = e.ret - e.ew
    g = e.groupby('ticker').agg(n=('vs', 'size'), sum_vs=('vs', 'sum'), mean_vs=('vs', 'mean')).sort_values('sum_vs', ascending=False)
    print(s, 'h60 total summed vsEW', round(e.vs.sum(), 2)); print(g.head(10).round(3).to_string())
    x = e[~e.ticker.isin(set(g.index[:10]))]
    print(s, 'excl top10 tickers: N', len(x), 'mean vsEW %.3f%%' % (x.vs.mean() * 100), 't %.2f' % cl_t(x.vs.values, x.date), 'mean exc %.3f%%' % (x.exc.mean() * 100))
# data checks: HOOD spike bar removed by R3; source of open-outside-range bars in small caps
print(P['large']['HOOD'].loc['2021-08-02':'2021-08-06'].round(2).to_string())
Ms = matrices(P['small'], cal)
oo = ((Ms['Open'] > Ms['High'] * 1.001) | (Ms['Open'] < Ms['Low'] * 0.999)).stack()
oo = oo[oo]
print('small open-outside-range bars by ticker:', pd.Series([t for _, t in oo.index]).value_counts().to_dict())
print('by year:', pd.Series([d.year for d, _ in oo.index]).value_counts().sort_index().to_dict())
