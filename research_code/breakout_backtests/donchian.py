"""Signal E: Donchian 55/20 trend trade, trade-level stats + capped equal-weight portfolio.

Pre-declared:
 - Entry: close_t > max(High[t-55..t-1]) (and liquidity eligibility), signal dates >= 2005-01-03;
   buy at open t+1 if not already in a trade for that ticker.
 - Exit: first day s >= entry day with close_s < min(Low[s-20..s-1]); sell at open s+1.
   Trades still open at the data end (2026-10-29) are closed at the last close (flagged).
 - Cost: 10 bps (large) / 50 bps (small) round trip, subtracted from each trade's return.
 - Portfolio: start equity 1.0 on 2005-01-03; at most K simultaneous positions (K=20 main;
   K=10, K=5 sensitivity). Each new position gets equity(prev close)/K (or remaining cash if less).
   Uninvested cash earns 0. When more entries than free slots occur on a day, they are taken in a
   random order; 20 random seeds are run and the median / range reported. A trade skipped for lack
   of a slot is dropped entirely (that ticker is not re-entered until the skipped trade would have
   exited).
"""
import math, numpy as np, pandas as pd
from engine import BASE, load, matrices, clean, signals
from event_study import nw_t

COST = dict(large=0.0010, small=0.0050)


def trades_for(M, S, spyO, spyC, cal, bull):
    O, C = M['Open'].values, M['Close'].values
    En, Ex = S['E_entry'].values, S['E_exit'].values
    T, N = En.shape
    rows = []
    for j in range(N):
        last_valid = np.flatnonzero(np.isfinite(C[:, j]))
        if len(last_valid) == 0: continue
        lastv = last_valid[-1]
        t = 0
        entries = np.flatnonzero(En[:, j])
        k = 0
        while k < len(entries):
            t = entries[k]
            e = t + 1
            while e <= lastv and not np.isfinite(O[e, j]): e += 1
            if e > lastv: break
            exits = np.flatnonzero(Ex[e:lastv + 1, j])
            if len(exits):
                s = e + exits[0]
                x = s + 1
                while x <= lastv and not np.isfinite(O[x, j]): x += 1
                if x <= lastv:
                    px, open_end = O[x, j], False
                else:
                    x, px, open_end = lastv, C[lastv, j], True
            else:
                x, px, open_end = lastv, C[lastv, j], True
            spy_r = (spyO[x] if not open_end else spyC[x]) / spyO[e] - 1
            rows.append(dict(j=j, sig=t, entry=e, exit=x, ret=px / O[e, j] - 1, spy=spy_r,
                             open_end=open_end, bull=bull[t], exit_at_close=open_end))
            # next entry signal must be on/after the exit day (position flat from open of x)
            k = np.searchsorted(entries, x)
    df = pd.DataFrame(rows)
    df['date'] = cal[df['sig'].values]
    df['hold'] = df['exit'] - df['entry']
    df['ticker'] = np.array(M['Close'].columns)[df['j'].values]
    return df


def trade_stats(df, cost, label):
    r = df['ret'] - cost
    w, l = r[r > 0], r[r <= 0]
    exc = df['ret'] - df['spy'] - cost
    mo = exc.groupby(df['date'].dt.to_period('M')).mean()
    return dict(subset=label, trades=len(df), win_rate=(r > 0).mean(), avg_win=w.mean(), avg_loss=l.mean(),
                profit_factor=w.sum() / -l.sum(), mean_net=r.mean(), median_net=r.median(),
                avg_hold_days=df['hold'].mean(), median_hold=df['hold'].median(),
                mean_net_excess=exc.mean(), median_net_excess=exc.median(), excess_hit=(exc > 0).mean(),
                t_excess_month=nw_t(mo.values, 3), open_at_end=int(df['open_end'].sum()))


def mdd(eq):
    eq = np.asarray(eq)
    peak = np.maximum.accumulate(eq)
    return (eq / peak - 1).min()


def portfolio(df, M, cal, K, cost, seed):
    O = M['Open'].values
    Cf = M['Close'].ffill().values
    start = np.searchsorted(cal, pd.Timestamp('2005-01-03'))
    T = len(cal)
    rng = np.random.default_rng(seed)
    df = df.assign(pr=rng.random(len(df))).sort_values(['entry', 'pr'])
    by_entry = {e: g for e, g in df.groupby('entry')}
    cash, eq_prev = 1.0, 1.0
    pos = {}  # id -> (j, shares, exit_idx, exit_at_close)
    busy_until = {}
    curve, npos = [], []
    for d in range(start, T):
        # exits at open
        for pid in [p for p, v in pos.items() if v[2] == d and not v[3]]:
            j, sh, _, _ = pos.pop(pid)
            cash += sh * O[d, j] * (1 - cost / 2)
        # entries at open
        if d in by_entry:
            for r in by_entry[d].itertuples():
                if len(pos) >= K: break
                if busy_until.get(r.j, -1) > d: continue
                alloc = min(eq_prev / K, cash)
                if alloc <= 1e-9: break
                sh = alloc * (1 - cost / 2) / O[d, r.j]
                cash -= alloc
                pos[r.Index] = (r.j, sh, r.exit, r.exit_at_close)
                busy_until[r.j] = r.exit
        # exits at close (trades open at data end)
        for pid in [p for p, v in pos.items() if v[2] == d and v[3]]:
            j, sh, _, _ = pos.pop(pid)
            cash += sh * Cf[d, j] * (1 - cost / 2)
        eq = cash + sum(sh * Cf[d, j] for j, sh, _, _ in pos.values())
        curve.append(eq); npos.append(len(pos)); eq_prev = eq
    curve = np.array(curve)
    yrs = (cal[T - 1] - cal[start]).days / 365.25
    return dict(CAGR=curve[-1] ** (1 / yrs) - 1, MaxDD=mdd(curve), avg_positions=np.mean(npos), final=curve[-1]), curve


def bench(spy, M, elig, cal):
    start = np.searchsorted(cal, pd.Timestamp('2005-01-03'))
    yrs = (cal[-1] - cal[start]).days / 365.25
    s = spy['Close'].values[start - 1:]
    s = s / s[0]
    C = M['Close']
    r = (C / C.shift(1) - 1).where(elig.shift(1).fillna(False).astype(bool))
    ew = (1 + r.mean(axis=1).fillna(0).values[start:]).cumprod()
    return dict(SPY_CAGR=s[-1] ** (1 / yrs) - 1, SPY_MaxDD=mdd(s), EW_CAGR=ew[-1] ** (1 / yrs) - 1, EW_MaxDD=mdd(ew))


def main():
    P, spy, cal = load()
    spyO, spyC = spy['Open'].values, spy['Close'].values
    bull = (spy['Close'] > spy['Close'].rolling(200).mean()).values
    tstats, prows, brows = [], [], []
    for uni in ['large', 'small']:
        M, _ = clean(matrices(P[uni], cal))
        S = signals(M)
        df = trades_for(M, S, spyO, spyC, cal, bull)
        df.to_csv(f"{BASE}/results/donchian_trades_{uni}.csv", index=False)
        c = COST[uni]
        for lab, d in [('all', df), ('2005-15', df[df.date <= '2015-12-31']), ('2016-26', df[df.date >= '2016-01-01']),
                       ('SPY>200d', df[df.bull]), ('SPY<200d', df[~df.bull])]:
            x = trade_stats(d, c, lab); x['universe'] = uni; tstats.append(x)
        b = bench(spy, M, S['elig'], cal); b['universe'] = uni; brows.append(b)
        for K in [20, 10, 5]:
            res = []
            for seed in range(20):
                r, curve = portfolio(df, M, cal, K, c, seed)
                res.append(r)
                if seed == 0 and K == 20:
                    pd.Series(curve, index=cal[np.searchsorted(cal, pd.Timestamp('2005-01-03')):]).to_csv(
                        f"{BASE}/results/donchian_equity_{uni}_K20_seed0.csv")
            rr = pd.DataFrame(res)
            prows.append(dict(universe=uni, K=K, CAGR_median=rr.CAGR.median(), CAGR_min=rr.CAGR.min(),
                              CAGR_max=rr.CAGR.max(), MaxDD_median=rr.MaxDD.median(), MaxDD_worst=rr.MaxDD.min(),
                              MaxDD_best=rr.MaxDD.max(), avg_positions=rr.avg_positions.median()))
            print(uni, K, prows[-1], flush=True)
    pd.DataFrame(tstats).to_csv(f"{BASE}/results/donchian_trade_stats.csv", index=False)
    pd.DataFrame(prows).to_csv(f"{BASE}/results/donchian_portfolio.csv", index=False)
    pd.DataFrame(brows).to_csv(f"{BASE}/results/benchmarks.csv", index=False)
    print(pd.DataFrame(tstats).round(4).to_string())
    print(pd.DataFrame(brows).round(4).to_string())


if __name__ == '__main__':
    main()
