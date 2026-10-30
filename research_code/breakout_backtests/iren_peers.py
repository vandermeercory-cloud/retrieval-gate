"""EXPLORATORY (added at user request after the pre-declared tests): single-stock cherry-picking check.

Fixed rule on daily bars (auto-adjusted Yahoo data), applied identically to every ticker:
  - Entry: close_t > max(High[t-50..t-1]) -> buy at open t+1 (when flat).
  - Exit: close_s < EMA200(close)_s (span 200, adjust=False) -> sell at open s+1.
  - Cost: 0.2% per side. Long-only, all-in/all-out, no leverage.
  - Window: 2023-09-25 (first trading day ~3.1 years before 2026-10-29) to 2026-10-29. Signals only
    from window days; earlier data used solely for warm-up of the 50-day high and EMA200.
  - Buy & hold: open of first window day -> close of 2026-10-29, also charged 0.2% per side.
  - Max drawdown on daily closing equity (intraday/30-min drawdowns would be deeper).
  - Position still open at the end is marked at the last close less the exit cost.
"""
import pickle, numpy as np, pandas as pd
BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
START, END, COST = pd.Timestamp('2023-09-25'), pd.Timestamp('2026-10-29'), 0.002


def mdd(x):
    x = np.asarray(x); return (x / np.maximum.accumulate(x) - 1).min()


def run(df):
    df = df.copy()
    hi50 = df['High'].rolling(50, min_periods=50).max().shift(1)
    ema = df['Close'].ewm(span=200, adjust=False).mean()
    pre_bars = int((df.index < START).sum())
    w = df.index >= START
    idx = np.flatnonzero(w)
    O, C = df['Open'].values, df['Close'].values
    ent = (df['Close'] > hi50).values
    ext = (df['Close'] < ema).values
    cash, sh, inpos = 1.0, 0.0, False
    pending = None
    eq, trades, days_in = [], [], 0
    entry_px = None
    for k in idx:
        if pending == 'buy':
            sh = cash * (1 - COST) / O[k]; cash = 0.0; inpos = True; entry_px = O[k]; entry_day = df.index[k]
        elif pending == 'sell':
            cash = sh * O[k] * (1 - COST); trades.append((entry_day, df.index[k], O[k] / entry_px - 1)); sh = 0.0; inpos = False
        pending = None
        if inpos:
            days_in += 1
            if ext[k]: pending = 'sell'
        else:
            if ent[k] and np.isfinite(C[k]): pending = 'buy'
        eq.append(cash + sh * C[k])
    open_end = inpos
    final = cash + sh * C[idx[-1]] * (1 - COST)
    if inpos:
        trades.append((entry_day, None, C[idx[-1]] / entry_px - 1))
    first = idx[0]
    bh = C[idx] / O[first] * (1 - COST)
    bh_final = C[idx[-1]] / O[first] * (1 - COST) ** 2
    return dict(first_day=str(df.index[first].date()), warmup_bars=pre_bars,
                strat_ret=final - 1, bh_ret=bh_final - 1, strat_mdd=mdd(eq), bh_mdd=mdd(bh),
                trades=len(trades), open_at_end=open_end, time_in_mkt=days_in / len(idx),
                win_trades=sum(1 for t in trades if t[2] > 0)), trades


if __name__ == '__main__':
    pp = pickle.load(open(f"{BASE}/data/iren_peers.pkl", 'rb'))
    rows, tl = [], {}
    for t, df in pp.items():
        if len(df) == 0:
            rows.append(dict(ticker=t, note='no Yahoo data')); continue
        df = df[df.index <= END]
        r, tr = run(df); r['ticker'] = t; rows.append(r); tl[t] = tr
    res = pd.DataFrame(rows).set_index('ticker')
    res.to_csv(f"{BASE}/results/iren_peers.csv")
    pd.set_option('display.width', 250)
    print(res.round(3).to_string())
    peers = [t for t in res.index if t not in ('SPY', 'QQQ') and pd.notna(res.loc[t, 'strat_ret'])]
    full = [t for t in peers if res.loc[t, 'warmup_bars'] >= 200]
    for lab, g in [('all peers incl IREN', peers), ('peers w/ >=200 warm-up bars', full),
                   ('peers excl IREN', [t for t in full if t != 'IREN'])]:
        s = res.loc[g]
        print(lab, len(g), 'median strat', round(s.strat_ret.median(), 3), 'median B&H', round(s.bh_ret.median(), 3),
              'median strat MDD', round(s.strat_mdd.median(), 3), 'median B&H MDD', round(s.bh_mdd.median(), 3),
              'strat>B&H', int((s.strat_ret > s.bh_ret).sum()), 'shallower DD', int((s.strat_mdd > s.bh_mdd).sum()),
              'mean strat', round(s.strat_ret.mean(), 3))
    print('IREN trades:', [(str(a.date()), str(b.date()) if b is not None else 'open', round(r, 3)) for a, b, r in tl['IREN']])
    # HUT continuity check (old Hut 8 Mining -> Hut 8 Corp, Nov/Dec 2023)
    h = pp['HUT']['Close']; rr = h.pct_change()
    print('HUT largest abs daily moves 2023-10..2024-01:', rr['2023-10-01':'2024-01-31'].abs().nlargest(3).round(3).to_dict())
