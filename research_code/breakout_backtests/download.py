"""Download daily OHLCV (auto_adjust=True) from Yahoo for both universes + SPY.
Start 2003-01-01 (warm-up for 252-day lookbacks), end 2026-10-30 exclusive -> last bar 2026-10-29
(the 2026-10-30 bar was still an intraday partial bar at run time)."""
import json, pickle, time, pandas as pd, yfinance as yf

D = str(__import__("pathlib").Path(__file__).resolve().parent / "data")
START, END = "2003-01-01", "2026-10-30"


def fetch(tickers, batch=100):
    out, failed = {}, []
    for i in range(0, len(tickers), batch):
        b = tickers[i:i + batch]
        for attempt in range(3):
            try:
                df = yf.download(b, start=START, end=END, auto_adjust=True, progress=False,
                                 group_by='ticker', threads=True)
                break
            except Exception as e:
                print('retry', e); time.sleep(5)
        for t in b:
            try:
                x = df[t].dropna(how='all')
                x = x[['Open', 'High', 'Low', 'Close', 'Volume']].dropna(subset=['Open', 'Close'])
                if len(x) < 300:
                    failed.append((t, f'only {len(x)} rows')); continue
                out[t] = x
            except Exception as e:
                failed.append((t, str(e)[:60]))
        print(i + len(b), 'done', len(out), 'ok', len(failed), 'failed', flush=True)
    return out, failed


if __name__ == '__main__':
    u = json.load(open(f"{D}/universe.json"))
    t0 = time.time()
    spy, _ = fetch(['SPY'])
    large, fl = fetch(u['large'])
    small, fs = fetch(u['small'])
    pickle.dump(dict(spy=spy['SPY'], large=large, small=small, failed_large=fl, failed_small=fs),
                open(f"{D}/prices.pkl", 'wb'))
    print('failed large', fl)
    print('failed small', fs)
    print('secs', time.time() - t0)
