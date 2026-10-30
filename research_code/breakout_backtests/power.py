# Usage: python power.py results   (reads results/events_large_D_h20.csv and _h60.csv)
import sys, math
import pandas as pd
R = sys.argv[1]
for h in (20, 60):
    d = pd.read_csv(f"{R}/events_large_D_h{h}.csv", parse_dates=["date"])
    d["vsew"] = d["ret"] - d["ew"]
    yrs = (d["date"].max() - d["date"].min()).days / 365.25
    print(f"h={h} N={len(d)} years={yrs:.1f} events/yr={len(d)/yrs:.0f}")
    for col in ("exc", "vsew"):
        m, s = d[col].mean()*100, d[col].std()*100
        print(f"  {col}: mean={m:.2f}% sd={s:.1f}% median={d[col].median()*100:.2f}%")
        for edge in (0.5, 1.0, 2.0):
            n = (2*s/edge)**2
            print(f"    trades for t=2 at true edge {edge}%: {n:,.0f}")
    # events per recent year
    print("  events by year (last 5):", d.groupby(d.date.dt.year).size().tail(6).to_dict())
