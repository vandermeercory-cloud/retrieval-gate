"""Build the two ticker universes.

Universe 1 (LARGE): approximate current S&P 500 membership written out from model
knowledge (as of ~2025/2026; index changes after that may be missing). Tickers that
Yahoo cannot serve are dropped later in download.py.

Universe 2 (SMALL): Yahoo Finance custom screener (yfinance EquityQuery):
  region == 'us' AND exchange in {NMS, NYQ, NGM, NCM, ASE}
  AND 300M <= intradaymarketcap <= 2B  (market cap as of the run date, 2026-10-30)
Pre-declared filters applied to the screener output:
  - quoteType == 'EQUITY', currency USD
  - drop names containing 'Acquisition' (SPAC shells)
  - drop names containing ' Fund' / 'Municipal' / 'Closed-End' (closed-end funds)
  - current price >= $2 and current 3-month avg dollar volume >= $1M
  - first trade date on or before 2021-12-31 (at least ~5 years of history)
  - not in the LARGE list
  then a random sample of 300 with numpy seed 42.
"""
import json, re, numpy as np, pandas as pd, yfinance as yf
from yfinance import EquityQuery as EQ

OUT = str(__import__("pathlib").Path(__file__).resolve().parent / "data")

SP500 = """
A AAPL ABBV ABNB ABT ACGL ACN ADBE ADI ADM ADP ADSK AEE AEP AES AFL AIG AIZ AJG AKAM ALB
ALGN ALL ALLE AMAT AMCR AMD AME AMGN AMP AMT AMZN ANET AON AOS APA APD APH APO APP APTV
ARE ATO AVB AVGO AVY AWK AXON AXP AZO BA BAC BALL BAX BBY BDX BEN BF-B BG BIIB BK BKNG
BKR BLDR BLK BMY BR BRK-B BRO BSX BX BXP C CAG CAH CARR CAT CB CBOE CBRE CCI CCL CDNS
CDW CEG CF CFG CHD CHRW CHTR CI CINF CL CLX CMCSA CME CMG CMI CMS CNC CNP COF COIN COO
COP COR COST CPAY CPB CPRT CPT CRL CRM CRWD CSCO CSGP CSX CTAS CTRA CTSH CTVA CVNA CVS CVX
D DAL DASH DAY DD DDOG DE DECK DELL DG DGX DHI DHR DIS DLR DLTR DOC DOV DOW DPZ DRI DTE
DUK DVA DVN DXCM EA EBAY ECL ED EFX EG EIX EL ELV EME EMN EMR ENPH EOG EPAM EQIX EQR EQT
ERIE ES ESS ETN ETR EVRG EW EXC EXE EXPD EXPE EXR F FANG FAST FCX FDS FDX FE FFIV FISV
FICO FIS FITB FOX FOXA FRT FSLR FTNT FTV GD GDDY GE GEHC GEN GEV GILD GIS GL GLW GM GNRC
GOOG GOOGL GPC GPN GRMN GS GWW HAL HAS HBAN HCA HD HIG HII HLT HOLX HON HOOD HPE HPQ HRL
HSIC HST HSY HUBB HUM HWM IBKR IBM ICE IDXX IEX IFF INCY INTC INTU INVH IP IQV IR IRM
ISRG IT ITW IVZ J JBHT JBL JCI JKHY JNJ JPM KDP KEY KEYS KHC KIM KKR KLAC KMB KMI KO
KR KVUE L LDOS LEN LH LHX LII LIN LKQ LLY LMT LNT LOW LRCX LULU LUV LVS LW LYB LYV MA
MAA MAR MAS MCD MCHP MCK MCO MDLZ MDT MET META MGM MHK MKC MKTX MLM MMC MMM MNST MO MOH
MOS MPC MPWR MRK MRNA MS MSCI MSFT MSI MTB MTCH MTD MU NCLH NDAQ NDSN NEE NEM NFLX NI NKE
NOC NOW NRG NSC NTAP NTRS NUE NVDA NVR NWS NWSA NXPI O ODFL OKE OMC ON ORCL ORLY OTIS OXY
PANW PAYC PAYX PCAR PCG PEG PEP PFE PFG PG PGR PH PHM PKG PLD PLTR PM PNC PNR PNW PODD
POOL PPG PPL PRU PSA PSKY PSX PTC PWR PYPL QCOM RCL REG REGN RF RJF RL RMD ROK ROL ROP ROST
RSG RTX RVTY SBAC SBUX SCHW SHW SJM SLB SMCI SNA SNPS SO SOLV SPG SPGI SRE STE STLD STT
STX STZ SW SWK SWKS SYF SYK SYY T TAP TDG TDY TECH TEL TER TFC TGT TJX TKO TMO TMUS TPL
TPR TRGP TRMB TROW TRV TSCO TSLA TSN TT TTD TTWO TXN TXT TYL UAL UBER UDR UHS ULTA UNH UNP
UPS URI USB V VICI VLO VLTO VMC VRSK VRSN VRTX VST VTR VTRS VZ WAB WAT WBD WDAY WDC WEC
WELL WFC WM WMB WMT WRB WSM WST WTW WY WYNN XEL XOM XYL XYZ YUM ZBH ZBRA ZTS
""".split()


def build_small():
    q = EQ('and', [EQ('eq', ['region', 'us']),
                   EQ('is-in', ['exchange', 'NMS', 'NYQ', 'NGM', 'NCM', 'ASE']),
                   EQ('btwn', ['intradaymarketcap', 300_000_000, 2_000_000_000])])
    quotes, off = [], 0
    while True:
        r = yf.screen(q, size=250, offset=off, sortField='ticker', sortAsc=True)
        quotes += r['quotes']
        off += 250
        if off >= r['total'] or not r['quotes']:
            break
    rows = []
    for x in quotes:
        rows.append(dict(symbol=x.get('symbol'), name=x.get('longName') or x.get('shortName') or '',
                         quoteType=x.get('quoteType'), exchange=x.get('exchange'), currency=x.get('currency'),
                         mcap=x.get('marketCap'), price=x.get('regularMarketPrice'),
                         adv3m=x.get('averageDailyVolume3Month'), first=x.get('firstTradeDateMilliseconds')))
    df = pd.DataFrame(rows).drop_duplicates('symbol')
    df.to_csv(f"{OUT}/small_screener_raw.csv", index=False)
    n0 = len(df)
    f = df[(df.quoteType == 'EQUITY') & (df.currency == 'USD')]
    f = f[~f.name.str.contains('Acquisition', case=False, na=False)]
    f = f[~f.name.str.contains(r' Fund|Municipal|Closed-End', case=False, na=False, regex=True)]
    f = f[(f.price >= 2) & (f.price * f.adv3m >= 1e6)]
    f = f[pd.to_datetime(f['first'], unit='ms') <= '2021-12-31']
    f = f[~f.symbol.isin(SP500)]
    rng = np.random.default_rng(42)
    sample = sorted(rng.choice(f.symbol.values, size=min(300, len(f)), replace=False).tolist())
    log = dict(screener_total=n0, after_filters=len(f), sampled=len(sample))
    print(log)
    return sample, log


if __name__ == '__main__':
    small, log = build_small()
    json.dump(dict(large=sorted(set(SP500)), small=small, small_log=log), open(f"{OUT}/universe.json", 'w'), indent=1)
    print('large', len(set(SP500)), 'small', len(small))


def add_price_excluded(n_pool_v1=1011, n_sample_v1=300):
    """User clarification (after first run): no share-price filter. Add a stratified random draw
    (same sampling rate 300/1011, seed 42) from names that the v1 filters excluded ONLY because
    current price < $2. Result = uniform-rate sample of the price-unfiltered pool."""
    df = pd.read_csv(f"{OUT}/small_screener_raw.csv")
    f = df[(df.quoteType == 'EQUITY') & (df.currency == 'USD')]
    f = f[~f.name.str.contains('Acquisition', case=False, na=False)]
    f = f[~f.name.str.contains(r' Fund|Municipal|Closed-End', case=False, na=False, regex=True)]
    f = f[pd.to_datetime(f['first'], unit='ms') <= '2021-12-31']
    f = f[~f.symbol.isin(SP500)]
    f = f[(f.price * f.adv3m >= 1e6) & (f.price < 2)]
    k = round(len(f) * n_sample_v1 / n_pool_v1)
    rng = np.random.default_rng(42)
    return sorted(rng.choice(sorted(f.symbol.values), size=k, replace=False).tolist()), len(f)
