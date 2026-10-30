"""Event study for signals A-D.

Pre-declared design:
 - Signal at close of day t; entry at open of t+1; exit at close of t+h, h in {1,5,20,60}
   (h=1 means open->close of day t+1, i.e. a same-day round trip / day trade).
 - Excess = stock return - SPY return over the identical open(t+1)->close(t+h) window.
 - Per-ticker, per-horizon blackout: a new event for the same ticker+signal is accepted only if
   t_new >= t_prev + h (its entry would fall after the prior holding window ended).
 - Costs: 10 bps round trip (large), 50 bps (small) subtracted from each event's excess return.
 - t-stats: (1) SEs clustered by signal date; (2) monthly-averaged excess returns with Newey-West
   SE, lag = ceil(h/21).
 - Controls (survivorship check): (a) unconditional mean excess of ALL eligible stock-days in the same
   universe/subset (random-entry baseline); (b) event return minus same-window equal-weight return of
   all eligible universe members ("vs-EW").
 - Splits: 2005-2015 vs 2016-2026 (signal date); SPY close above/below its 200-day SMA on day t.
"""
import json, math, numpy as np, pandas as pd
from engine import BASE, load, matrices, clean, signals

H = [1, 5, 20, 60]
COST = dict(large=0.0010, small=0.0050)


def cl_t(x, g):
    x = np.asarray(x, float); n = len(x)
    if n < 3: return np.nan
    e = x - x.mean()
    s = pd.Series(e).groupby(np.asarray(g)).sum().values
    G = len(s)
    if G < 2: return np.nan
    v = (G / (G - 1)) * (s ** 2).sum() / n ** 2
    return x.mean() / math.sqrt(v) if v > 0 else np.nan


def nw_t(x, lag):
    x = np.asarray(x, float); n = len(x)
    if n < 6: return np.nan
    e = x - x.mean()
    v = (e @ e) / n
    for l in range(1, lag + 1):
        w = 1 - l / (lag + 1)
        v += 2 * w * (e[l:] @ e[:-l]) / n
    se = math.sqrt(v / n) if v > 0 else np.nan
    return x.mean() / se


def build_events(sig, M, spyO, spyC, h, elig, ew):
    O, C = M['Open'].values, M['Close'].values
    S = sig.values
    T, N = S.shape
    rows = []
    for j in range(N):
        idx = np.flatnonzero(S[:, j])
        last = -10 ** 9
        for i in idx:
            if i < last + h: continue
            if i + h >= T: break
            eo, xc = O[i + 1, j], C[i + h, j]
            if not (np.isfinite(eo) and np.isfinite(xc)) or eo <= 0: continue
            last = i
            r = xc / eo - 1
            rs = spyC[i + h] / spyO[i + 1] - 1
            rows.append((i, j, r, rs, ew[i]))
    return pd.DataFrame(rows, columns=['i', 'j', 'ret', 'spy', 'ew'])


def ew_matrix(M, elig, h):
    O, C = M['Open'], M['Close']
    R = C.shift(-h) / O.shift(-1) - 1
    R = R.where(elig)
    return R, R.mean(axis=1).values


def summarize(ev, cost, h, label):
    x = ev['exc'].values
    if len(x) == 0:
        return dict(subset=label, N=0)
    lo, hi = np.percentile(x, [1, 99])
    mo = ev.groupby('month')['exc'].mean()
    return dict(subset=label, N=len(x), mean=x.mean(), median=np.median(x), hit=(x > 0).mean(),
                t_date=cl_t(x, ev['date']), t_month=nw_t(mo.values, math.ceil(h / 21)),
                net_mean=x.mean() - cost, net_hit=((x - cost) > 0).mean(),
                wins_mean=np.clip(x, lo, hi).mean(),
                vsEW_mean=(ev['ret'] - ev['ew']).mean(), vsEW_t=cl_t((ev['ret'] - ev['ew']).values, ev['date']),
                raw_mean=ev['ret'].mean())


def main():
    P, spy, cal = load()
    spyO, spyC = spy['Open'].values, spy['Close'].values
    bull = (spy['Close'] > spy['Close'].rolling(200).mean()).values
    out, base_rows, dq, dstats = [], [], {}, []
    for uni in ['large', 'small']:
        M = matrices(P[uni], cal)
        M, log = clean(M)
        dq[uni] = log
        S = signals(M)
        elig = S['elig']
        dates = cal
        for h in H:
            R, ew = ew_matrix(M, elig, h)
            # unconditional baseline: all eligible stock-days
            X = (R.values - (spyC[np.minimum(np.arange(len(cal)) + h, len(cal) - 1)] /
                             np.r_[spyO[1:], np.nan] - 1)[:, None])
            valid = np.isfinite(X)
            valid[len(cal) - h - 1:, :] = False
            early = (dates <= '2015-12-31')[:, None]
            for lab, m in [('all', valid), ('2005-15', valid & early), ('2016-26', valid & ~early),
                           ('SPY>200d', valid & bull[:, None]), ('SPY<200d', valid & ~bull[:, None])]:
                v = X[m]
                base_rows.append(dict(universe=uni, h=h, subset=lab, N=len(v), mean=v.mean(),
                                      median=np.median(v), hit=(v > 0).mean()))
            for s in ['A', 'B', 'C', 'D']:
                ev = build_events(S[s], M, spyO, spyC, h, elig, ew)
                ev['date'] = dates[ev['i'].values]
                ev['month'] = ev['date'].dt.to_period('M')
                ev['exc'] = ev['ret'] - ev['spy']
                ev['bull'] = bull[ev['i'].values]
                ev['ticker'] = np.array(M['Close'].columns)[ev['j'].values]
                ev.to_csv(f"{BASE}/results/events_{uni}_{s}_h{h}.csv", index=False)
                subsets = [('all', ev), ('2005-15', ev[ev.date <= '2015-12-31']),
                           ('2016-26', ev[ev.date >= '2016-01-01']),
                           ('SPY>200d', ev[ev.bull]), ('SPY<200d', ev[~ev.bull])]
                for lab, e in subsets:
                    d = summarize(e, COST[uni], h, lab)
                    d.update(universe=uni, signal=s, h=h)
                    out.append(d)
                if s == 'D' and h == 1:
                    # day-t open->close and gap size, same events (h=1 blackout = every event)
                    O, C = M['Open'].values, M['Close'].values
                    i, j = ev['i'].values, ev['j'].values
                    oc = C[i, j] / O[i, j] - 1
                    oc_spy = spyC[i] / spyO[i] - 1
                    gap = O[i, j] / C[i - 1, j] - 1
                    ev2 = ev.assign(oc=oc, oc_exc=oc - oc_spy, gap=gap)
                    ev2.to_csv(f"{BASE}/results/events_{uni}_D_dayt.csv", index=False)
                    for lab, e in [('all', ev2), ('2005-15', ev2[ev2.date <= '2015-12-31']),
                                   ('2016-26', ev2[ev2.date >= '2016-01-01'])]:
                        dstats.append(dict(universe=uni, subset=lab, N=len(e),
                                           gap_mean=e.gap.mean(), gap_median=e.gap.median(),
                                           dayt_oc_mean=e.oc.mean(), dayt_oc_median=e.oc.median(),
                                           dayt_oc_exc_mean=e.oc_exc.mean(), dayt_oc_exc_hit=(e.oc_exc > 0).mean(),
                                           dayt_t_date=cl_t(e.oc_exc.values, e.date),
                                           next_oc_exc_mean=e.exc.mean(),
                                           gap_gt_25pct=(e.gap > 0.25).sum()))
            print(uni, h, 'done', flush=True)
    res = pd.DataFrame(out)
    res.to_csv(f"{BASE}/results/event_stats.csv", index=False)
    pd.DataFrame(base_rows).to_csv(f"{BASE}/results/baseline.csv", index=False)
    pd.DataFrame(dstats).to_csv(f"{BASE}/results/D_dayt.csv", index=False)
    json.dump(dq, open(f"{BASE}/results/data_quality.json", 'w'), indent=1, default=str)
    print(json.dumps(dq, indent=1, default=str))


if __name__ == '__main__':
    main()
