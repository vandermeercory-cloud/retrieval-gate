"""Shared data preparation: aligned OHLCV matrices, data-quality cleaning, signal matrices.

PRE-DECLARED cleaning rules (fixed before looking at any signal results):
 R1  Volume <= 0 is treated as missing (cannot satisfy or feed volume averages).
 R2  Bars with High < max(Open,Close) or Low > min(Open,Close) (0.1% tolerance) are counted as
     inconsistent. For signal D the event is rejected if the day-t Open lies outside the day's reported
     [Low, High] range (likely bad open print producing a fake gap). For range computations High/Low
     are repaired to max/min(O,H,L,C).
 R3  One-day spike: close-to-close move > +50% or < -33% that reverses next day to within 10% of the
     pre-spike close. All OHLCV on the spike day is set to NaN (removed).
 R4  Liquidity eligibility for every signal: prior-50-day average dollar volume (Close*Volume, using
     adjusted prices) >= $1M.
"""
import pickle, numpy as np, pandas as pd

BASE = str(__import__("pathlib").Path(__file__).resolve().parent)
SIG_START, SIG_END = pd.Timestamp("2005-01-03"), pd.Timestamp("2026-10-29")


def load():
    P = pickle.load(open(f"{BASE}/data/prices.pkl", "rb"))
    spy = P['spy']
    cal = spy.index
    return P, spy, cal


def matrices(dct, cal):
    tick = sorted(dct)
    M = {}
    for f in ['Open', 'High', 'Low', 'Close', 'Volume']:
        M[f] = pd.DataFrame({t: dct[t][f].reindex(cal) for t in tick}, index=cal).astype(float)
    return M


def clean(M):
    O, H, L, C, V = (M[k] for k in ['Open', 'High', 'Low', 'Close', 'Volume'])
    log = {}
    log['bars'] = int(C.notna().sum().sum())
    zv = (V <= 0) & C.notna()
    log['R1_zero_volume_bars'] = int(zv.sum().sum())
    V = V.mask(V <= 0)
    bad_hl = ((H < np.maximum(O, C) * 0.999) | (L > np.minimum(O, C) * 1.001)) & C.notna()
    log['R2_inconsistent_ohlc_bars'] = int(bad_hl.sum().sum())
    open_outside = (O > H * 1.001) | (O < L * 0.999)
    log['R2_open_outside_range_bars'] = int(open_outside.sum().sum())
    # R3 spike reversal
    Cp = C.ffill()
    r0 = C / Cp.shift(1)
    nxt = Cp.shift(-1) / Cp.shift(1)
    spike = ((r0 > 1.5) | (r0 < 1 / 1.5)) & (nxt.sub(1).abs() < 0.10)
    log['R3_spike_reversal_bars_removed'] = int(spike.sum().sum())
    log['R3_examples'] = [(str(d.date()), t) for t, d in
                          list(spike.stack()[lambda s: s].index.map(lambda x: (x[1], x[0])))[:15]]
    # extreme moves (possible split errors) just counted
    ext = ((r0 > 3) | (r0 < 1 / 3)) & ~spike
    log['extreme_moves_gt3x_not_reverting'] = int(ext.sum().sum())
    log['extreme_examples'] = [(str(d.date()), t, round(float(r0.loc[d, t]), 2)) for d, t in
                               ext.stack()[lambda s: s].index[:15]]
    for X in (O, H, L, C, V):
        X[spike] = np.nan
    Hr = np.maximum(np.maximum(H, O), C).where(H.notna())
    Lr = np.minimum(np.minimum(L, O), C).where(L.notna())
    return dict(Open=O, High=Hr, Low=Lr, Close=C, Volume=V, open_outside=open_outside), log


def signals(M):
    O, H, L, C, V = (M[k] for k in ['Open', 'High', 'Low', 'Close', 'Volume'])
    avgV50 = V.rolling(50, min_periods=40).mean().shift(1)
    dv50 = (C * V).rolling(50, min_periods=40).mean().shift(1)
    elig = (dv50 >= 1e6) & C.notna() & O.notna()
    elig &= (C.index >= SIG_START)[:, None] & (C.index <= SIG_END)[:, None]
    hi252 = H.rolling(252, min_periods=252).max().shift(1)
    A = (C > hi252) & elig
    B = A & (V >= 2 * avgV50)
    rng20 = (H.rolling(20, min_periods=20).max() - L.rolling(20, min_periods=20).min()) / C
    pct = rng20.rolling(252, min_periods=252).rank(pct=True)   # rank of R_s within R_{s-251..s}
    tight_prev = pct.shift(1) <= 0.10                          # as of day t-1
    hi20 = H.rolling(20, min_periods=20).max().shift(1)
    Csig = tight_prev & (C > hi20) & (V >= 1.5 * avgV50) & elig
    Cprev = C.shift(1)
    D = (O >= 1.04 * Cprev) & (V >= 3 * avgV50) & elig & ~M['open_outside']
    hi55 = H.rolling(55, min_periods=55).max().shift(1)
    lo20 = L.rolling(20, min_periods=20).min().shift(1)
    E_entry = (C > hi55) & elig
    E_exit = (C < lo20)
    return dict(A=A, B=B, C=Csig, D=D, E_entry=E_entry, E_exit=E_exit, elig=elig)
