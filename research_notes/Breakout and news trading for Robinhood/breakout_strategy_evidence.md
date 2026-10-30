# Evidence on Breakout and Momentum-Style Trading Strategies for US Stocks (as of October 2026)

Method note for the report writer: this cloud session's network allowlist blocked direct page fetches (WebFetch failed with ENOTFOUND on concretumgroup.com and danfin.net, so no further fetches were tried). Every finding below comes from web-search result snippets and search-engine summaries of the linked pages, not from reading full papers. Treat exact figures as "reported by the linked source". Where two sources disagree, both are given. Source-quality tags used below: [PEER-REVIEWED] = journal article; [WORKING PAPER] = SSRN/NBER/institute series, not yet peer-reviewed; [PRACTITIONER] = practitioner/vendor research with some disclosed method; [ANECDOTAL] = blog/forum/marketing with unclear method.

## 1. Academic evidence on price breakouts: 52-week high, channel/trend following, time-series vs cross-sectional momentum, and decay

### Takeaway
"Breakout" signals measured slowly (nearness to the 52-week high, all-time-high entries, 12-month time-series and cross-sectional momentum) have the strongest long-sample evidence. Their net-of-cost edge is much smaller than the gross edge, it is concentrated in a few large winners, it suffers sharp crashes, and it has weakened since publication (after 2000 for stock momentum, after 2009 for trend following). Generic public technical rules (moving-average and channel rules) do not beat transaction costs once data snooping is controlled for.

### Cited Findings
**52-week-high effect (George & Hwang 2004 and follow-ups)**
- [PEER-REVIEWED] George & Hwang (2004, Journal of Finance): stocks near their 52-week high outperform stocks far from it, and nearness to the 52-week high accounts for much of the profit from price momentum. — [Marquette paper summarizing it](https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1168&context=fin_fac)
- [PEER-REVIEWED] George & Hwang argue that the returns predicted by the 52-week-high strategy are permanent: unlike ordinary momentum, they do not reverse over the long run. — [George & Hwang paper, UH Bauer copy](https://www.bauer.uh.edu/tgeorge/papers/gh4-paper.pdf)
- Barroso & Wang (2021) argue that the 52-week-high effect is limited to small stocks and that price momentum explains its predictability. This challenges the original result. — [Marquette paper citing Barroso & Wang](https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1168&context=fin_fac)
- Barroso & Wang (seminar summary): most momentum profits are predictable and occur after periods of low volatility. Standard models fit well most of the time but not when the profits are produced. Stocks near the 52-week high are significantly more liquid than stocks far from it. — [University of Liverpool seminar page](https://liverpool.ac.uk/management/conferences-and-events/what-explains-price-momentum-and-52-week-high-momentum-when-they-really-work-seminar)
- International evidence is mixed. One study finds the 52-week-high strategy does not dominate traditional momentum in international stock markets — [ScienceDirect, J. Int. Money & Finance](https://www.sciencedirect.com/science/article/abs/pii/S0261560610001099). A 20-market index study finds short-run momentum alongside long-run reversals, which departs from the US "no reversal" result — [ScienceDirect, Global Finance Journal](https://www.sciencedirect.com/science/article/abs/pii/S106297690700021X). Another index study finds the 52-week-high effect "not as reliable or as robust as the momentum effect" — [Griffith University repository](https://research-repository.griffith.edu.au/items/7519d620-c8d2-55df-984d-4293560ba0f8)
- The evidence on liquidity conflicts. A Louisiana Tech dissertation reports that profits from 52-week high/low strategies "come largely from small stocks" — [Louisiana Tech Digital Commons](https://digitalcommons.latech.edu/dissertations/122). An Australian study instead finds significantly positive raw returns among the more liquid stocks and significantly negative returns among illiquid stocks — [ANU research portal, "The impact of liquidity and transaction costs on the 52 week high"](https://researchportalplus.anu.edu.au/en/publications/the-impact-of-liquidity-and-transaction-costs-on-the-52-week-high/)

**Cross-sectional momentum: decay and crashes**
- A summary of a 1926–2005 US study reports that momentum is strong from 1939 to 2000 but "much weaker before 1939 and after 2000". This is secondhand; the underlying paper is not named in the snippet. — [CXO Advisory](https://www.cxoadvisory.com/?p=1158)
- [PEER-REVIEWED] Daniel & Moskowitz, "Momentum Crashes": in a 1927–2010 sample, July and August 1932 were the two worst consecutive months for long-short momentum. In March–May 2009, past losers rose about 163% while past winners rose only about 8%. — [NBER w20439](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf); [Columbia draft](https://business.columbia.edu/sites/default/files-efs/pubfiles/4607/mom11.pdf)
- Secondary sources put the 1932 momentum loss at about -91% (June–August) and the 2009 Fama-French momentum return at about -52.6%. — [Alpha Architect](https://alphaarchitect.com/avoiding-momentum-crashes/); [ETF.com / Swedroe](https://www.etf.com/node/94406.md)
- Crashes come from momentum's time-varying market beta, which turns very negative after market declines. A dynamic, volatility-scaled version of the strategy improves results significantly. — [ETF.com / Swedroe](https://www.etf.com/node/94015.md)

**Time-series momentum / trend following**
- [PEER-REVIEWED/PRACTITIONER, AQR] Hurst, Ooi & Pedersen (2017), "A Century of Evidence on Trend-Following Investing": time-series momentum built back to 1880 had positive average returns in every decade, low correlation to traditional assets, and did well in 8 of the 10 largest crisis periods. — [AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing); [PDF copy](https://www.chesler.us/resources/academia/A_Century_of_Evidence_on_Trend_Following.pdf)
- After strong results in 2008, trend following did poorly in 2009–2013. The authors note that trend-following performance tends to be weak for about four years on average after a global financial crisis. Sources give different start dates (1880 vs 1903) for different versions of the century study. — [Quantpedia](https://quantpedia.com/strategies/time-series-momentum-effect); [Alpha Architect](https://alphaarchitect.com/time-series-momentum-aka-trend-following-the-historical-evidence/)
- Moskowitz, Ooi & Pedersen (2012) is the foundational TSMOM paper; it uses futures and forwards from about 1985. Babu et al. (2019) report out-of-sample evidence across 82 additional securities. — [Quantpedia](https://quantpedia.com/strategies/time-series-momentum-effect)
- There is also time-series momentum evidence within individual stocks over nearly 100 years. — [Lancaster University eprint, "Time-Series Momentum in Nearly 100 Years of Stock Returns"](https://eprints.lancs.ac.uk/id/eprint/128366/1/Time_Series_Momentum_in_Nearly_100_Years_of_Stock_Returns.pdf) (figures not retrieved)

**Channel / all-time-high breakouts on single stocks (closest evidence to "Donchian on stocks")**
- [PRACTITIONER] Wilcox & Crittenden (2005), "Does Trend Following Work on Stocks?": the system buys at the next open after a weekly close at a new all-time high and exits on a 10-ATR trailing stop. The test covered 24,000+ securities over 22 years, with 18,000+ trades, a 49.3% win rate and 0.5% round-trip transaction costs. The authors conclude trend following on stocks has positive expectancy. — [UPenn copy of paper](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf); [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following)
- Critique of Wilcox & Crittenden: Victor Niederhoffer questioned its statistical significance and noted that small stocks did much better than big stocks late in the sample. He reports that his own similar tests on S&P 500 stocks produced random results. He also cites a growth figure of about $1,000 to $30,000 that was not verified against the paper. — [Daily Speculations](https://dailyspeculations.com/vic/trend.html)
- [WORKING PAPER/PRACTITIONER] Zarattini, Pagani & Wilcox (Jan 2025), "Does Trend Following Still Work on Stocks?": a survivorship-bias-free sample of all liquid US stocks from 1950 to Nov 2024. Under 7% of trades generate most of the cumulative profit, and these properties held out of sample from 2005 to 2024. Transaction costs are a "major challenge" for high-turnover versions, and a turnover-control algorithm is used to mitigate them. — [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following); [Concretum page (fetch blocked)](https://concretumgroup.com/does-trend-following-still-work-on-stocks/)
- Reported performance for that portfolio: 15.19% CAGR and 6.18% annualized alpha gross of fees over 1991–2024, per the Concretum summary. A Harbourfront Quant summary gives 15.02% CAGR, 6.19% alpha and a 31.75% max drawdown, period unclear. The sources conflict slightly, and no Sharpe ratio was found. — [Concretum summary, via search](https://concretumgroup.com/does-trend-following-still-work-on-stocks/); [Harbourfront Quant](https://harbourfrontquant.substack.com/p/does-trend-following-still-work-on)
- A related Zarattini & Antonacci industry-timing trend study (1926–2024) reports 18.5% average annual return, 12.1% volatility and a Sharpe ratio of 1.46. This is an industry-level study, not single stocks. — [search summary of Concretum materials](https://concretumgroup.com/tag/momentum/)

**Generic technical breakout and moving-average rules: data snooping and costs**
- [PEER-REVIEWED] Bajgrowicz & Scaillet (2012, JFE 106(3):473–491) test the 7,846 rules from Sullivan, Timmermann & White (1999) on the DJIA using a false-discovery-rate control. Before costs, technical analysis looked useful in 1897–1996 even after controlling for data snooping. However, persistence tests show an investor could not have picked the future best rules ex ante. Transaction costs fully offset even the in-sample performance, and in 1997–2007 the outperformance disappears. The authors conclude that publicly available technical indicators do not have predictive power exceeding their transaction costs. — [IDEAS/RePEc](https://ideas.repec.org:443/a/eee/jfinec/v106y2012i3p473-491.html); [CFA Institute digest](https://rpc.cfainstitute.org/research/cfa-digest/2013/02/technical-trading-revisited-false-discoveries-persistence-tests-and-transaction-costs-digest); [EFMA 2008 working version](https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/Bajgrowicz.pdf)

**Post-publication decay and costs (applies to all published anomalies)**
- [PEER-REVIEWED] McLean & Pontiff (2016) find a 58% drop in anomaly performance after publication. A later strategy-decay paper estimates a similar 43% drop in Sharpe ratio. — [arXiv 2105.01380, "Why and how systematic strategies decay"](https://arxiv.org/pdf/2105.01380)
- Another paper describes the McLean–Pontiff result as post-publication returns about 50% smaller than in-sample, the 58% vs 50% gap probably reflecting different measures. It also reports returns declining about 25% three years post-sample and 40% five years post-sample, and estimates that about half of the decay is publication bias. — [arXiv 2209.13623, "Publication Bias in Asset Pricing Research"](https://arxiv.org/pdf/2209.13623)
- [PEER-REVIEWED] Novy-Marx & Velikov (2016, RFS), "A Taxonomy of Anomalies and Their Trading Costs": costs reduce the profitability and significance of every anomaly studied. Most anomalies with under 50% monthly one-sided turnover still earn significant net spreads when designed to limit costs; few higher-turnover ones do. Momentum is classed as "mid-turnover", while industry momentum and short-term reversals are high-turnover. A buy/hold spread (stricter rules to enter than to stay) is the most effective cost mitigation. — [NBER w20721](https://www.nber.org/papers/w20721.pdf); [author PDF](https://mysimon.rochester.edu/novy-marx/research/ToAatTC.pdf)
- Frazzini, Israel & Moskowitz (2014, using real institutional trade data) find size, value and momentum remain positive after costs. Novy-Marx & Velikov's net estimate for momentum is "MUCH lower". — [Alpha Architect](https://alphaarchitect.com/trading-costs-destroy-factor-investing/)

### Inferences
- Slow, cross-sectional "breakout" signals (52-week high, 12-month momentum, all-time-high trend following) survive costs only at institutional cost levels and with turnover control. They depend on a small share of outsized winners, so a retail trader who cuts winners early or trades few names will likely miss the trades that carry the edge.
- The 52-week-high effect probably overlaps heavily with ordinary momentum. Whether it survives on its own is disputed (Barroso & Wang), and its sensitivity to liquidity is unresolved (the dissertation and the ANU study conflict).
- Decay evidence (McLean & Pontiff: roughly 50–58% decline; Bollinger signals failing after 2001; DJIA rules failing after 1997) suggests haircutting any published backtest by at least half before expecting live results.
- Time-series momentum is best documented for diversified futures (indices, bonds, FX, commodities), not single stocks. Evidence for single-stock time-series momentum is thinner and mostly practitioner-run (Wilcox/Crittenden, Zarattini et al.).

### Gaps
- Could not read the original George & Hwang (2004) tables. Commonly cited figures (such as the sample period and monthly spread) were not verified in this session and are deliberately omitted.
- No peer-reviewed study of classic Donchian (N-day high) channel breakouts on individual US stocks with realistic costs was found. The closest evidence is the practitioner all-time-high studies above.
- No source found on momentum-factor or 52-week-high performance in 2020–2026, so it is unknown whether the post-2000 weakness persisted. Exact Sharpe ratios for Moskowitz–Ooi–Pedersen and Hurst–Ooi–Pedersen were not retrieved.
- The full Barroso & Wang post-2000 small-stock breakdown was not retrieved.

## 2. Intraday breakout strategies: opening-range breakouts (ORB), "stocks in play", gap-and-go vs gap-fade, VWAP

### Takeaway
The main intraday breakout evidence is a set of working papers by Zarattini, Aziz and Barbon. They report very large backtested returns for a 5-minute ORB, but only when it is restricted to "stocks in play" (abnormal relative volume, usually news-driven); a plain ORB is weak. The authors have commercial ties to day-trading education, the papers are not peer-reviewed, and independent checks flag sensitivity to slippage and to the choice of window. Intraday momentum (the first half-hour predicting the last half-hour) is peer-reviewed but economically small. No rigorous US single-stock study shows a robust after-cost edge for either gap-and-go or gap-fade.

### Cited Findings
**ORB on "stocks in play" (Zarattini, Barbon & Aziz 2024)**
- [WORKING PAPER] "A Profitable Day Trading Strategy For The U.S. Equity Market", Swiss Finance Institute Research Paper 24-98 (SSRN 4729284). It tests ORB, focusing on a 5-minute opening range, on more than 7,000 US stocks from 2016 to 2023. Restricting trades to Stocks in Play, defined as stocks with higher-than-normal activity that day mostly because of company news, remains beneficial after transaction costs. The top-20 portfolio earned a total net return above 1,600%, a Sharpe ratio of 2.81 and annualized alpha of 36%. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284); [RePEc](https://ideas.repec.org/p/chf/rpseri/rp2498.html); [Univ. St. Gallen repository PDF](https://alexandria.unisg.ch/bitstreams/3c2989c4-688d-4d78-8a71-f02690990d51/download)
- One summary gives 1,637% total return and 41.6% annualized IRR from Jan 1, 2016 to Dec 31, 2023. — [search summary; SSRN listing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284)
- Screening rules as summarized:
  - opening price above $5;
  - 14-day average daily volume of at least 1,000,000 shares;
  - 14-day ATR above $0.50;
  - opening-range volume relative to the last 14 days ("relative volume") of at least 100%;
  - among the 20 highest relative-volume names.
- Entry and exit rules as summarized: entries are stop orders at the 5-minute high (long) or low (short); the stop-loss is 10% of ATR from entry; positions are closed at the market close. — [QuantConnect replication](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/); [GitHub replication](https://github.com/jlmn-code/bot_intradia_orb)
- QuantConnect's replication used the 5-minute window because it performed best in the paper. It reports a Sharpe ratio of about 2.4 with beta near zero. — [QuantConnect](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/)
- A critical review says not every ORB variant was profitable, and that the 2024 paper itself found a plain (unfiltered) ORB weak. — [danfin.net review (fetch blocked; via search summary)](https://danfin.net/opening-range-breakout-research)
- Another test reportedly found the 5-minute range the weakest window: "28% of its cells are powered-negative", with losses shrinking as the range widens. The search summary did not identify this study clearly, so treat it as unverified. — [search summary of danfin.net / related critique](https://danfin.net/opening-range-breakout-research)
- The GitHub replicator notes the usual criticism that these studies underestimate slippage and commissions in small, illiquid stocks. — [GitHub jlmn-code/bot_intradia_orb](https://github.com/jlmn-code/bot_intradia_orb)
- Author affiliation: Andrew Aziz is a day-trading author and educator associated with Bear Bull Traders, and the VWAP paper is hosted on Bear Bull Traders' site. Carlo Zarattini is with Concretum Group, a quant research firm. Andrea Barbon is an academic (Swiss Finance Institute / University of St. Gallen series). — [Wikipedia: Andrew Aziz](https://en.wikipedia.org/wiki/Andrew_Aziz); [Bear Bull Traders VWAP page](https://bearbulltraders.com/?p=2606339)

**ORB on QQQ/TQQQ (Zarattini & Aziz 2023)**
- [WORKING PAPER] "Can Day Trading Really Be Profitable?" (SSRN 4416622) tests a 5-minute ORB on QQQ and TQQQ from 2016 to 2023. The strategy returned 1,484% vs 169% for buy-and-hold QQQ, with annualized alpha of 33% net of commissions. The authors stress that the edge is amplified with leverage or 3x leveraged ETFs. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622); [PDF copy](https://static1.squarespace.com/static/5983d931579fb366729580d8/t/643ed6765176b45506e41a01/1681839734183/SSRN-id4416622.pdf); [Semantic Scholar](https://www.semanticscholar.org/paper/Can-Day-Trading-Really-Be-Profitable-Evidence-of-in-Zarattini-Aziz/4d55f526cc56f08662cb8976796cd3b719ef6d2b)
- Rules as summarized: buy (sell) QQQ at the start of the second 5-minute bar if the first 5-minute bar was up (down), sizing each trade so that hitting the stop-loss costs 1% of capital. — [CXO Advisory](https://www.cxoadvisory.com/technical-trading/day-trading-with-an-opening-range-breakout-strategy/)
- No Sharpe ratio was found for this QQQ paper. Do not attribute the 2.81 figure (from the stocks-in-play paper) to it. — [search summary](https://www.cxoadvisory.com/technical-trading/day-trading-with-an-opening-range-breakout-strategy/)

**VWAP-based entries (Zarattini & Aziz 2023/2025)**
- [WORKING PAPER] "Volume Weighted Average Price (VWAP): The Holy Grail for Day Trading Systems" (SSRN 4631351, posted Nov 2023, revised Apr 2025): long when price is above VWAP and short when below, on QQQ and TQQQ from Jan 2, 2018 to Sep 28, 2023. $25,000 grew to $192,656 net of commissions, a 671% return. — [Bear Bull Traders](https://bearbulltraders.com/?p=2606339); [Concretum page (fetch blocked)](https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/)
- A QuantConnect reproduction cites a Sharpe ratio of about 2.10 for the original paper (not verified against the paper). A QuantConnect forum thread titled "Bear Bull Traders' paper on 'The Holy Grail': not so fast" shows community skepticism; its arguments were not retrieved. — [QuantConnect backtest](https://www.quantconnect.com/terminal/cache/embedded_backtest_b115d0894231d55994b1068202f6c0ae.html); [QuantConnect forum](https://www.quantconnect.com/forum/discussion/16706/bear-bull-traders-039-paper-on-quot-the-holy-grail-quot-not-so-fast/)

**Intraday momentum (peer-reviewed)**
- [PEER-REVIEWED] Gao, Han, Li & Zhou (2018, JFE), "Market Intraday Momentum": on SPY from 1993 to 2013, the first half-hour return (measured from the prior close) predicts the last half-hour return, and the same holds for 10 other actively traded ETFs. Predictability is stronger when volatility is high, in recessions, and on some macro-news days. — [WashU profile](https://profiles.wustl.edu/en/publications/market-intraday-momentum/); [Alpha Architect](https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/)
- Economic size of the effect, which varies by source:
  - average annual returns of 6.67% (SPY), 11.72% (IWM) and 24.22% (IYR);
  - a SPY timing rule earned 6.3% gross annualized vs -0.5% for always holding the last half-hour;
  - the first half-hour return explains only 1–2% of the variance in the last half-hour return;
  - last-half-hour moves after extreme first-half-hour moves are "too small in magnitude for most investors to exploit";
  - a QuantConnect re-creation found lower returns over its own test period.
  — [CXO Advisory](https://cxoadvisory.com/calendar-effects/first-and-last-half-hours-of-trading-linked); [Harbourfront Quant](https://harbourfrontquant.substack.com/p/does-intraday-momentum-exist-in-stock); [QuantConnect](https://www.quantconnect.com/learning/articles/investment-strategy-library/intraday-etf-momentum)
- Li, Sakkas & Urquhart find significant first-to-last half-hour predictability in 12 of 16 international markets. — [University of Reading accepted version](https://reading-9.eprints-hosting.org/95566/1/Accepted-Version.pdf)

**Gap-and-go vs gap-fade**
- [PEER-REVIEWED, smaller journal] Study of US stocks' opening gaps:
  - negative opening gaps are much larger than positive ones;
  - the asymmetry is stronger in Russell 2000 and Nasdaq-100 stocks than in S&P 500 stocks;
  - gaps usually follow new firm, industry or macro information;
  - after positive gaps, prices drift up, which the authors say offers profitable opportunities.
  — [PMC (PubMed Central)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017064/)
- [ANECDOTAL] A practitioner blog says about 70% of overnight gaps fill intraday, but the basic return of trading the fill is "zero". So a high fill rate does not imply an edge. — [Systematic Individual Investor](https://systematicindividualinvestor.com/2018/05/09/dead-simple-the-opening-gap-and-other-intraday-patterns-around-the-market-opening/)
- [ANECDOTAL] SPY/QQQ, past 5 years: about half of gaps larger than 1% faded intraday to some degree, and SPY kept rising from open to close on about 40% of gap-up days. — [SharePlanner](https://www.shareplanner.com/blog/strategies-for-trading/fading-the-gap-how-large-overnight-moves-in-spy-and-qqq-play-out-during-the-trading-day.html)
- [WORKING PAPER, futures] Two 2026 arXiv falsification studies on Micro Nasdaq (MNQ) futures find that OHLCV-based intraday momentum, gap-continuation and gap-fade rules mostly fail after costs or work only in particular regimes. — [arXiv 2605.04004](https://arxiv.org/pdf/2605.04004); [arXiv 2605.11423](https://arxiv.org/pdf/2605.11423)

### Inferences
- In the Zarattini–Barbon–Aziz work, the ingredient that matters is the stocks-in-play filter (abnormal relative volume, usually tied to news), not the ORB mechanic itself. That points to news and attention catalysts as the real driver of intraday breakout follow-through.
- Headline figures (1,484%, 1,600%+, 671%) are compounded, leveraged backtests (1% risk per trade, leveraged ETFs) from authors who sell trading education or research. Sharpe ratios of 2–3 for simple public rules on 2016–2023 data should be treated as an upper bound, given the post-publication decay evidence in section 1.
- Tight stops (10% of ATR) on small, news-driven names make results highly sensitive to slippage at the open, when spreads are widest. Retail fills through payment-for-order-flow routing at the open may differ from the backtest assumptions.

### Gaps
- Exact cost assumptions (per-share commission, slippage) and leverage caps in the two ORB papers and the VWAP paper could not be verified because the fetch was blocked. The commonly quoted $0.0035/share and 4x leverage were not confirmed in any snippet.
- No win rate or hit rate was found for the ORB papers.
- No independent peer-reviewed replication of the stocks-in-play ORB was found, and no post-2023 out-of-sample results.
- No rigorous, large-sample, after-cost US single-stock study of gap-and-go vs gap-fade was found.

## 3. Features that help flag a breakout early: relative volume, volatility contraction, relative strength, float and short interest, pre-market gaps, unusual options activity

### Takeaway
Abnormal volume (the high-volume return premium) and option-market order flow (put/call ratios, option-to-stock volume) have the best peer-reviewed support as early signals. Relative strength and momentum are well supported at monthly horizons (section 1). Volatility-contraction setups (Bollinger squeeze) worked in older index data but not after 2001. VCP, float and "short-squeeze" signals have little or no rigorous support, and high short interest predicts lower, not higher, future returns on average.

### Cited Findings
**Relative volume / volume surges**
- [PEER-REVIEWED] Gervais, Kaniel & Mingelgrin (2001, JF 56(3):877–919), "The High-Volume Return Premium": abnormally high volume over a day or week predicts higher subsequent returns. — [Wharton Rodney White Center working paper](https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9901.pdf); [RePEc](https://ideas.repec.org/p/fth/pennfi/01-99.html)
- One summary says the effect on NYSE stocks lasts about 50 days. The explanation is Merton's (1987) investor-recognition hypothesis: volume shocks raise a firm's visibility. — [search summaries of GKM; NYU archive copy](https://archive.nyu.edu/bitstream/2451/27578/2/SSRN-id1122463.pdf)
- Kaniel, Ozoguz & Starks (2012) find the high-volume premium in developed markets generally, with mixed results in emerging markets. — [CEPR DP14587 / search summary](https://repec.cepr.org/repec/cpr/ceprdp/DP14587.pdf)
- The premium disappears quickly for illiquid stocks but persists much longer for highly liquid stocks. — [search summary of follow-up study; Clute Journals](https://clutejournals.com/index.php/JBER/article/view/7521)
- The intraday stocks-in-play result (section 2) uses opening-range relative volume of at least 100% and the top 20 by relative volume as its key filter. — [QuantConnect](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/)
- [PRACTITIONER, counter-evidence] Bulkowski's volume study (8,000 chart patterns, Jul 1991–May 2011; rectangles and double/triple tops and bottoms): 14% of patterns with above-average breakout volume failed to rise more than 10%, vs 5% for below-average breakout volume. This contradicts the usual practitioner rule that high breakout volume confirms a breakout. — [ThePatternSite volume study](https://thepatternsite.com/VolumeStudy.html)

**Volatility contraction (Bollinger squeeze, narrow ranges, VCP)**
- [PEER-REVIEWED per CXO summary] Fang, Jacobsen & Qin, "Popularity versus Profitability: Evidence from Bollinger Bands". The squeeze signal fires when band width hits a 6-month low and price closes beyond a band. Over the full sample, the average daily gross return spread between buy and sell signals was significantly positive for all 14 indexes. In 1983–2001 the signals beat the market for only 10 (buy) and 8 (sell) indexes and did not work for US indexes. After 2001, the average daily buy-minus-sell spread was -0.07% and the strategy was unprofitable gross of costs. The authors attribute the decline to market adaptation as the bands became popular, and their index-based tests ignore tracking costs. — [CXO Advisory](https://www.cxoadvisory.com/big-ideas/when-bollinger-bands-snapped/)
- [PRACTITIONER] A StockCharts SystemTrader test of a squeeze system on S&P 1500 stocks, with a trend filter and momentum trigger, reports outperforming buy-and-hold. This is a single vendor backtest. — [StockCharts / Arthur Hill](https://articles.stockcharts.com/article/articles-arthurhill-2017-03-systemtrader---testing-a-bollinger-band-squeeze-system-for-stocks-in-the-sp-1500-/)
- [ANECDOTAL] A Reddit analysis of 399 squeeze events in 50 S&P 500 stocks found 49.6% directional accuracy unfiltered. Breakouts nearly always happen, but their direction is a coin flip. — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1rdji47/snapshots/2026-02-27T22%3A12%3A05.0165Z)
- At the market level, Barroso & Wang find most momentum profits occur after low-volatility periods. This is a market-volatility regime finding, not stock-level contraction. — [Liverpool seminar page](https://liverpool.ac.uk/management/conferences-and-events/what-explains-price-momentum-and-52-week-high-momentum-when-they-really-work-seminar)

**Relative strength**
- See section 1: cross-sectional momentum, the 52-week high and all-time-high trend following. In the Jiang–Kelly–Xiu image-CNN study, the closest benchmarks were Han–Zhou–Zhu's TREND signal and 1-week short-term reversal. Over short (weekly) horizons, raw relative strength tends to reverse rather than continue. — [CXO Advisory summary of JKX](https://www.cxoadvisory.com/?p=34917); [Yale-hosted JF article](https://economics.yale.edu/sites/default/files/2023-11/The%20Journal%20of%20Finance%20-%202023%20-%20JIANG%20-%20Re%25E2%2580%2590%20Imag%20in%20ing%20Price%20Trends_0.pdf)

**Short interest / days to cover**
- [PEER-REVIEWED] Diether, Lee & Werner (daily short-sale data): rising short selling is followed by negative returns for up to five days, and short sellers time trades well against short-term trends. Their sample averaged short interest of about 3.3% of shares and 4.7 days to cover. — [NBER conference paper](https://users.nber.org/~confer/2005/mmf05/werner.pdf)
- [WORKING PAPER] Hong, Li, Ni, Scheinkman & Yan, "Days to Cover and Stock Returns" (NBER w21166), argue that days-to-cover (short ratio divided by turnover) is the better-founded measure of shorting costs and overpricing. Their sample averaged about 5.5 days to cover, with a cross-sectional standard deviation of 8. The return figures were not retrieved. — [NBER w21166](https://www.nber.org/papers/w21166.pdf)
- UK evidence (Mohamad et al. 2011): firms with large daily jumps in short interest had a -1.48% cumulative abnormal return over 15 days after the data were published. — [search summary; IIUM repository](https://irep.iium.edu.my/28465/)
- [ANECDOTAL] A blog backtest of 2,269 stocks found the lowest days-to-cover quintile had the highest average returns, which cuts against the squeeze thesis. Its method is unclear. — [fffinstill blog](https://fffinstill.com/blog/short-interest-backtest-squeeze-candidates-sector-analysis)

**Unusual options activity**
- [PEER-REVIEWED] Pan & Poteshman (2006, RFS) build a put/call ratio from buyer-initiated, position-opening option volume using CBOE data. Stocks with low put/call ratios outperform high-ratio stocks by about 40 bps the next day and about 1% over the next week. The predictability is short-lived, and it relies on signed, non-public volume data. Unsigned put/call ratios also have some predictive power. — [NBER w10925](https://nber.org/system/files/working_papers/w10925/w10925.pdf); [NBER conference version](https://users.nber.org/~confer/2003/aps03/pan.pdf)
- [PEER-REVIEWED] Johnson & So (2012, JFE): the weekly option-to-stock volume ratio (O/S) is negatively related to next-week returns. It also predicts the sign and size of earnings surprises the following week, and it is stronger when short-sale constraints are higher. — [arXiv review citing it](https://arxiv.org/pdf/2201.09319); [Emerald JDQS article](https://www.emerald.com/insight/content/doi/10.1108/JDQS-11-2023-0036)
- Put/call ratios predict better at a daily horizon, while O/S predicts better at weekly and monthly horizons. In Korea the O/S sign is reversed (positive). — [Emerald JDQS article](https://www.emerald.com/insight/content/doi/10.1108/JDQS-11-2023-0036)

**Pre-market gaps:** see section 2. Gaps usually follow news, and positive gaps show post-gap drift in one US study, but no rigorous after-cost US single-stock gap strategy was found. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017064/)

**Attention as a negative feature for buyers:** Robinhood "herding" into attention-grabbing stocks predicts negative abnormal returns (section 5). A feature that flags a stock everyone is watching may mark the end of a move rather than its start for late retail buyers. — [Barber et al. 2022, WashU](https://profiles.wustl.edu/en/publications/attention-induced-trading-and-returns-evidence-from-robinhood-use/)

### Inferences
- The most defensible "early breakout" feature set is: an abnormal-volume shock, ideally with a fundamental news catalyst; bullish signed option flow (low buyer-initiated put/call ratio, though retail cannot see signed data); and longer-horizon relative strength or nearness to the 52-week high. Each is documented separately in peer-reviewed work. None was found tested as a combined, after-cost breakout entry signal.
- Volatility contraction appears to predict that a big move is coming, but not its direction (the 49.6% anecdote; post-2001 Bollinger failure). Directional edge has to come from elsewhere, such as trend, volume or catalyst.
- High short interest is, on average, a bearish signal. Squeeze trades rely on rare tail events, and the evidence base for them is anecdotal.

### Gaps
- No peer-reviewed evidence found for Minervini's "VCP", NR7/narrow-range-day breakouts, or "cup-and-handle" style patterns on US stocks.
- No rigorous evidence found on low float as a breakout predictor.
- Option-flow evidence uses signed or open-interest data (CBOE open-buy volume) that is not equivalent to retail "unusual options activity" scanners. No study evaluating those commercial scanners was found.
- The Hong et al. days-to-cover return magnitudes were not retrieved.

## 4. How often breakouts fail, and how results change with transaction costs, slippage and small-cap liquidity

### Takeaway
Most individual breakout trades lose or go nowhere. Win rates near 50% for trend systems are typical, profits come from a small minority of trades, and practitioner failure rates for chart-pattern breakouts roughly doubled from the 1990s to the mid-2000s. Costs are the decisive variable: technical rules that look good gross are wiped out net, high-turnover anomalies rarely survive, and breakout and volume effects are weakest or negative in illiquid small caps, where retail breakout traders concentrate.

### Cited Findings
- [PRACTITIONER] Bulkowski, failure defined as price not rising at least 10% after an upward breakout:
  - 11% in 1991, peaking at 44% in 2007;
  - an average of 14% in the 1990s bull market, doubling to 28% in 2003–2007;
  - only 12% of chart patterns produced large gains at the start of the 2008 bear market;
  - the study covered 13,932 patterns from 1991 to 2008;
  - an alternative definition counts a pattern as failed if price moves less than 5% beyond the breakout before reversing.
  — [Bulkowski, Stocks & Commodities 2009](https://www.traders.com/Documentation/FEEDbk_docs/2009/05/Bulkowski.html); [ThePatternSite failure rates](https://thepatternsite.com/FailureRates.html)
- [PRACTITIONER] All-time-high trend following on stocks had a 49.3% win rate with 0.5% round-trip costs — [Wilcox & Crittenden 2005](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf). In the 1950–2024 follow-up, under 7% of trades generate most cumulative profits — [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following)
- [ANECDOTAL] Bollinger squeeze breakouts showed 49.6% directional accuracy across 399 events. — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1rdji47/snapshots/2026-02-27T22%3A12%3A05.0165Z)
- [PEER-REVIEWED] Transaction costs completely offset even the in-sample performance of the best of 7,846 technical rules on the DJIA. — [Bajgrowicz & Scaillet 2012, RePEc](https://ideas.repec.org:443/a/eee/jfinec/v106y2012i3p473-491.html)
- [PEER-REVIEWED] Few anomalies with monthly turnover above 50% survive costs. Momentum survives only with cost-aware design, and its net premium is much lower than gross. — [Novy-Marx & Velikov, NBER w20721](https://www.nber.org/papers/w20721.pdf); [Alpha Architect](https://alphaarchitect.com/trading-costs-destroy-factor-investing/)
- The 52-week-high strategy is significantly negative among illiquid Australian stocks — [ANU](https://researchportalplus.anu.edu.au/en/publications/the-impact-of-liquidity-and-transaction-costs-on-the-52-week-high/). The high-volume premium disappears quickly in illiquid stocks — [Clute Journals](https://clutejournals.com/index.php/JBER/article/view/7521)
- Small stocks drove much of the late-sample performance of all-time-high trend following, and S&P 500-only tests were "random" — [Niederhoffer review](https://dailyspeculations.com/vic/trend.html). Transaction costs are a "major challenge" for high-turnover stock trend following — [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following)
- Intraday ORB replicators warn that slippage and commissions in small, illiquid stocks are underestimated — [GitHub](https://github.com/jlmn-code/bot_intradia_orb). Index-based Bollinger tests overstate returns by ignoring tracking costs — [CXO Advisory](https://www.cxoadvisory.com/big-ideas/when-bollinger-bands-snapped/)
- [PEER-REVIEWED] Eaton, Green, Roseman & Wu (2022, JFE 146:502–528) compare 25 Robinhood outage days (Jan–Aug 2020) with outages at traditional brokers. In high-retail-interest stocks, less Robinhood participation means smaller order imbalances, better liquidity and lower volatility; the opposite holds when traditional brokers go down. Herding by inexperienced traders creates inventory risk that worsens liquidity. — [SSRN](https://papers.ssrn.com/abstract=3776874); [CXO Advisory](https://cxoadvisory.com/?p=35082)

### Inferences
- Breakout trading's realistic profile is a hit rate of roughly 50% or lower, with a positive skew that depends on letting rare winners run. Any rule that caps upside, such as fixed small profit targets or quick scalps, removes the source of the edge.
- Retail breakout traders are drawn to small, high-volume, news-driven names, where the documented effects are weakest net of costs and where herding by other retail traders widens spreads and adds volatility (Eaton et al.).
- Rising failure rates over time (Bulkowski) are consistent with the decay evidence in section 1.

### Gaps
- No peer-reviewed estimate of a "false breakout rate" specifically for intraday ORB or pre-market gap breakouts on US small caps was found.
- No study was found quantifying actual retail fill slippage (including payment-for-order-flow routing) on breakout entries at the open.
- Bulkowski's 2009–2026 failure rates were not retrieved.

## 5. What happens to retail traders who trade this way: day-trader outcome studies and Robinhood research

### Takeaway
Large administrative-data studies are uniformly negative. Fewer than 1% of Taiwanese day traders are predictably profitable net of fees, and 97% of persistent Brazilian futures day traders lost money, with only about 1% earning more than minimum wage. Robinhood users' attention-driven herding into top-bought stocks is followed by negative abnormal returns of about 3–6% within days. Welch (2022) shows that the aggregate Robinhood crowd portfolio did fine in 2018–2020, which is a different claim from saying active breakout or attention trading pays.

### Cited Findings
**Taiwan (Barber, Lee, Liu & Odean)**
- [PEER-REVIEWED] "The cross-section of speculator skill: Evidence from day trading" (J. Financial Markets 2014, vol. 18, pp. 1–24), Taiwan 1992–2006: fewer than 1% of day traders predictably and reliably earn positive abnormal returns net of fees. In the published abstract, the top 500 ranked day traders go on to earn 61.3 bps per day before fees and 37.9 bps after. A working-paper version instead refers to the "4,000 most profitable day traders (<1% of the population)", so the two versions give different group sizes. — [IDEAS/RePEc](https://ideas.repec.org/a/eee/finmar/v18y2014icp1-24.html); [Berkeley working paper](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/Day%20Trading%20Skill%20110523.pdf)
- A related Barber–Lee–Liu–Odean paper on whether day traders rationally learn about their ability is reported to state that 97% of day traders can expect to lose money. This comes from a search summary and was not verified in the text. — [Berkeley PDF](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/day%20trading%20and%20learning%20110217.pdf); [RePEc, Review of Asset Pricing Studies 2020](https://ideas.repec.org/a/oup/rasset/v10y2020i1p61-93..html)
- [ANECDOTAL] A secondary claim that 84.3% of 360,000 Taiwanese day traders lost money, with a median return of -8.7%, comes from a low-authority TradingView post. Verify it against the original before using. — [TradingView post](https://my.tradingview.com/chart/EURUSD/pJsnrpJF-The-Ineffectiveness-of-Day-Trading-A-Critical-Review-of-Empiric)

**Brazil (Chague, De-Losso & Giovannetti)**
- [WORKING PAPER, FGV/SSRN] "Day Trading for a Living?" studies individuals who began day trading Brazil's equity (mini-index) futures in 2013–2015 and persisted at least 300 days. 97% lost money. Only 1.1% earned more than the Brazilian minimum wage, and only 0.5% earned more than a bank teller's starting salary. The authors find no evidence of learning and conclude it is "virtually impossible" to day trade for a living, contrary to course providers' claims. — [FGV repository](https://repositorio.fgv.br/items/e87d04fc-4b4c-4a56-ab5a-1c84c1afde1b); [RePEc](https://ideas.repec.org/p/fgv/eesptd/525.html); [Quantpedia](https://quantpedia.com/retail-day-trading-is-an-uphill-battle/)
- Caveat: the sample is Brazilian futures traders who persisted at least 300 days, not US equity breakout traders. — [Quantpedia](https://quantpedia.com/retail-day-trading-is-an-uphill-battle/)

**Robinhood: Barber, Huang, Odean & Schwarz (2022)**
- [PEER-REVIEWED] "Attention-Induced Trading and Returns: Evidence from Robinhood Users", Journal of Finance 77(6):3141–3190. Robinhood users engage in more attention-induced trading than other retail investors and herd into the same stocks. Average 5-day abnormal returns for the top stocks bought each day are -3%, or -6% in the most extreme herding episodes. An SSRN version reports -4.7% average 20-day abnormal returns. — [WashU profile](https://profiles.wustl.edu/en/publications/attention-induced-trading-and-returns-evidence-from-robinhood-use/); [ResearchGate](https://www.researchgate.net/publication/364066611_Attention-Induced_Trading_and_Returns_Evidence_from_Robinhood_Users); [SSRN mirror](https://colab.ws/articles/10.2139/ssrn.3715077)
- Herding episodes are linked to the app's simplified display of information (such as the top-mover and popularity lists) and to standard attention proxies. In a natural experiment, Robinhood outages disproportionately reduce trading in high-attention stocks. — [ResearchGate](https://www.researchgate.net/publication/346399054_Attention_Induced_Trading_and_Returns_Evidence_from_Robinhood_Users)

**Robinhood: Welch (2022)**
- [PEER-REVIEWED] "The Wisdom of the Robinhood Crowd", Journal of Finance 77(3):1489–1527 (NBER w27866):
  - the aggregate Robinhood crowd (Robintrack holdings data, mid-2018 to mid-2020) added to holdings during the March 2020 crash, so there was no panic selling, and benefited from the rebound;
  - holdings tilted toward high-volume, mostly large stocks, with trading volume explaining about 50–60% of portfolio weights;
  - the consensus portfolio had good timing and alpha over the window and did not underperform standard benchmark models.
  — [NBER](https://www.nber.org/papers/w27866); [RePEc](https://ideas.repec.org:443/a/bla/jfinan/v77y2022i3p1489-1527.html)

**Robinhood: market-quality externality**
- [PEER-REVIEWED] Eaton et al. (2022, JFE) find Robinhood herding worsens liquidity and raises volatility in high-retail-interest stocks, as described in section 4. They describe the average Robinhood user as 31 years old vs 50 for the average US retail investor. — [SSRN](https://papers.ssrn.com/abstract=3776874)

### Inferences
- Welch and Barber et al. do not contradict each other. Holding a diversified, mostly large-cap crowd portfolio through 2018–2020 did fine, while chasing the day's most-bought attention stocks lost about 3–6% within a week. Breakout and "stocks in play" trading on retail apps resembles the second behavior.
- Robinhood's own interface (top movers, popularity lists, push notifications) is documented to concentrate attention. Breakout signals surfaced through the app are therefore likely to be crowded, and crowding is followed by negative abnormal returns on average.
- Across Taiwan, Brazil and Robinhood, three different markets and data sources, the base rate for retail short-horizon speculation is losses for the large majority, with no evidence of learning. Any breakout strategy recommendation should start from that prior.

### Gaps
- No US-regulator (SEC/FINRA) or exchange study of US retail day-trader profitability was found in this session.
- No study isolating retail traders who specifically use breakout or ORB rules, as opposed to day traders in general, was found.
- No post-2022 Robinhood outcome studies were retrieved (for example on 0DTE options or 24-hour trading), and no data on how Robinhood's interface changes after 2021 affected herding.

## 6. Machine-learning or LLM-based breakout prediction with credible out-of-sample evidence

### Takeaway
The most credible ML result is Jiang, Kelly & Xiu (2023, JF): a CNN trained on price/volume chart images predicts short-horizon returns out of sample. Its edge is gross of costs, concentrated in equal-weighted (small-cap) portfolios, and much weaker in large caps (value-weighted Sharpe ratio about 0.6, or slightly above 1 for the top 500 stocks). LLM news-sentiment signals (Lopez-Lira & Tang) predicted next-day returns, but performance declined over 2021–2024, and later work shows look-ahead and memorization bias can inflate such results. No study specifically predicting "breakouts" with credible after-cost, out-of-sample evidence was found.

### Cited Findings
**Jiang, Kelly & Xiu (2023)**
- [PEER-REVIEWED] "(Re-)Imag(in)ing Price Trends", Journal of Finance 2023, pp. 3193–3249: a CNN reads images of daily OHLC prices, volume and a moving average and predicts future return direction. — [Yale-hosted JF article](https://economics.yale.edu/sites/default/files/2023-11/The%20Journal%20of%20Finance%20-%202023%20-%20JIANG%20-%20Re%25E2%2580%2590%20Imag%20in%20ing%20Price%20Trends_0.pdf); [SSRN](https://papers.ssrn.com/abstract=3756587)
- Long-short decile portfolios earn annualized gross Sharpe ratios of up to about 2.5 equal-weighted and 0.6 value-weighted. The best benchmark, 1-week short-term reversal, earns 1.3 (EW) and 0.3 (VW) with similar turnover. Results hold across horizons, with a skipped week, and internationally when the model is trained on US data. — [CXO Advisory](https://www.cxoadvisory.com/?p=34917)
- A BSIC article reports much higher equal-weighted long-short Sharpe ratios of 7.2, 6.8 and 4.9 for the 5-, 20- and 60-day image models. It says these fall to slightly above 1 when the universe is restricted to the 500 largest stocks. These figures conflict with CXO's, so check the paper's tables. — [BSIC](https://bsic.it/technical-analysis-on-steroids/)
- The BSIC replication found that 55.9% of test images were "up" moves and that the CNN's directional accuracy was near a coin toss. Its value lay in cross-sectional ranking, not in directional calls. — [BSIC](https://bsic.it/technical-analysis-on-steroids/)
- A 2024 follow-up proposes image-based importance weights to enhance price-trend strategies. — [arXiv 2408.08483](https://arxiv.org/html/2408.08483v1)

**Lopez-Lira & Tang (LLM news sentiment)**
- [WORKING PAPER] "Can ChatGPT Forecast Stock Price Movements?": ChatGPT's sentiment scores on news headlines predict next-day returns. The authors argue the tests are out-of-sample because training data ended in Sep 2021; the sample runs Oct 2021 to May 2024. They report a general decline in the strategy's performance over the sample, which they call suggestive. — [arXiv 2304.07619](https://arxiv.org/pdf/2304.07619); [UCLA Anderson PDF](https://www.anderson.ucla.edu/sites/default/files/document/2024-04/4.19.24%20Alejandro%20Lopez%20Lira%20ChatGPT_V3.pdf)
- Lopez-Lira told CNBC that return predictability should decline as more people use these tools. — [CNBC](https://www.cnbc.com/2023/04/12/chatgpt-may-be-able-to-predict-stock-movements-finance-professor-says.html)
- [WORKING PAPER] A look-ahead-bias test using Llama-3.3-70B (2012–2023 in-sample, 2024 out-of-sample) reproduces the central effect in-sample: a one-step move in the LLM signal predicts a 0.21% higher next-day return (t = 12.18). The authors attribute the in-sample effect partly to possible memorization and use 2024 as a placebo test. — [arXiv 2512.23847](https://arxiv.org/pdf/2512.23847)
- Separate work assesses look-ahead bias in GPT-sentiment return predictions. — [arXiv 2309.17322](https://arxiv.org/pdf/2309.17322)
- A 2026 working paper on academia.edu, "Generative AI as a Common Signal: LLM Stock Recommendations, Retail Crowding and the Salience Premium", examines retail crowding into LLM-recommended stocks. It was not reviewed in detail. — [academia.edu](https://academia.edu/179547661/Generative_AI_as_a_Common_Signal_LLM_Stock_Recommendations_Retail_Crowding_and_the_Salience_Premium)

**Deep learning for trend following (futures, not stocks)**
- arXiv papers apply deep networks and changepoint detection to time-series momentum in futures. They are not US-stock breakout evidence, and their figures were not retrieved. — [arXiv 1904.04912](https://arxiv.org/pdf/1904.04912); [arXiv 2105.13727](https://arxiv.org/pdf/2105.13727)

### Inferences
- The strongest ML evidence (JKX) is cross-sectional ranking over weekly-to-monthly horizons, gross of costs, and strongest in small caps. That is the segment where section 4 shows costs and illiquidity erode edges most, so the net-of-cost retail-tradable edge is likely far smaller than a Sharpe ratio of 2.5.
- LLM news signals face rapid crowding and decay, as their author predicted and observed. Out-of-sample claims for LLMs are hard to trust because of training-data look-ahead and memorization.
- No credible evidence was found that ML or LLM tools let a retail trader identify US stock breakouts early, after costs, out of sample.

### Gaps
- The JKX paper's own net-of-cost results and exact decile Sharpe tables were not retrieved.
- Gu, Kelly & Xiu (2020) and other large ML-return-prediction studies were not covered in this session.
- No peer-reviewed study of ML classifiers built to predict chart-pattern or ORB breakout success on US stocks with out-of-sample, after-cost results was found. Commercial "AI breakout scanner" claims were not evaluated.
- The magnitude of the decline in Lopez-Lira & Tang's post-2023 returns was not retrieved.
