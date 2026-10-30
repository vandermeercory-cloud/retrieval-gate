# Evidence on Breakout and Momentum-Style Trading Strategies for US Stocks (as of October 2026)

Method note for the report writer:
- This cloud session's network allowlist blocked direct page fetches. WebFetch failed with ENOTFOUND on concretumgroup.com and danfin.net, so no further fetches were tried. Every finding below comes from web-search result snippets and search-engine summaries of the linked pages, not from reading full papers. Treat exact figures as "reported by the linked source". Where sources disagree, both are given.
- Source-quality tags: [PEER-REVIEWED] = journal article; [WORKING PAPER] = SSRN/NBER/institute series, not yet peer-reviewed; [PRACTITIONER] = practitioner/vendor research with some disclosed method; [ANECDOTAL] = blog/forum/marketing with unclear method.
- User constraint (from coordinator): the account starts with $100 and cannot day trade. Only swing trades held from overnight to a few weeks are relevant. Intraday findings (ORB, VWAP, gap-and-go/gap-fade intraday) are summarized briefly in section 3 and labeled NOT USABLE under this constraint.
- User clarification: there is no minimum or maximum share price. Fractional shares let a $100 account buy any stock, including high-priced large caps, so these notes do not steer toward low-priced or penny stocks. Price filters quoted from papers (such as the ORB paper's "price above $5") describe those papers' universes, not a recommendation. The evidence on low-priced and lottery-like stocks is in sections 2 and 4.

## 1. Academic evidence on price breakouts: 52-week high, channel/trend following, time-series vs cross-sectional momentum, and decay

### Takeaway
"Breakout" signals measured slowly have the strongest long-sample evidence: nearness to the 52-week high, all-time-high entries, and 12-month time-series and cross-sectional momentum. These operate over holding periods of weeks to months, so they fit the swing constraint. Their net-of-cost edge is much smaller than the gross edge, it is concentrated in a few large winners, it suffers sharp crashes, and it has weakened since publication (after 2000 for stock momentum, after 2009 for trend following). Generic public technical rules (moving-average and channel rules) do not beat transaction costs once data snooping is controlled for.

### Cited Findings
**52-week-high effect (George & Hwang 2004 and follow-ups)**
- [PEER-REVIEWED] George & Hwang (2004, Journal of Finance): stocks near their 52-week high outperform stocks far from it, and nearness to the 52-week high accounts for much of the profit from price momentum. — [Marquette paper summarizing it](https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1168&context=fin_fac)
- [PEER-REVIEWED] George & Hwang argue that the returns predicted by the 52-week-high strategy are permanent: unlike ordinary momentum, they do not reverse over the long run. — [George & Hwang paper, UH Bauer copy](https://www.bauer.uh.edu/tgeorge/papers/gh4-paper.pdf)
- Barroso & Wang (2021) argue that the 52-week-high effect is limited to small stocks and that price momentum explains its predictability. This challenges the original result. — [Marquette paper citing Barroso & Wang](https://epublications.marquette.edu/cgi/viewcontent.cgi?article=1168&context=fin_fac)
- Barroso & Wang (seminar summary): most momentum profits are predictable and occur after periods of low volatility. Standard models fit well most of the time but not when the profits are produced. Stocks near the 52-week high are significantly more liquid than stocks far from it. — [University of Liverpool seminar page](https://liverpool.ac.uk/management/conferences-and-events/what-explains-price-momentum-and-52-week-high-momentum-when-they-really-work-seminar)
- International evidence is mixed. One study finds the 52-week-high strategy does not dominate traditional momentum internationally — [ScienceDirect, J. Int. Money & Finance](https://www.sciencedirect.com/science/article/abs/pii/S0261560610001099). A 20-market index study finds short-run momentum alongside long-run reversals — [ScienceDirect, Global Finance Journal](https://www.sciencedirect.com/science/article/abs/pii/S106297690700021X). Another index study finds the 52-week-high effect "not as reliable or as robust as the momentum effect" — [Griffith University repository](https://research-repository.griffith.edu.au/items/7519d620-c8d2-55df-984d-4293560ba0f8)
- The evidence on liquidity conflicts. A Louisiana Tech dissertation reports that 52-week high/low profits "come largely from small stocks" — [Louisiana Tech Digital Commons](https://digitalcommons.latech.edu/dissertations/122). An Australian study finds significantly positive raw returns among liquid stocks and significantly negative returns among illiquid stocks — [ANU research portal](https://researchportalplus.anu.edu.au/en/publications/the-impact-of-liquidity-and-transaction-costs-on-the-52-week-high/)

**Cross-sectional momentum: decay and crashes**
- A summary of a 1926–2005 US study: momentum is strong from 1939 to 2000 but "much weaker before 1939 and after 2000". This is secondhand; the underlying paper is not named. — [CXO Advisory](https://www.cxoadvisory.com/?p=1158)
- [PEER-REVIEWED] Daniel & Moskowitz, "Momentum Crashes": in a 1927–2010 sample, July and August 1932 were the two worst consecutive months for long-short momentum. In March–May 2009, past losers rose about 163% while past winners rose only about 8%. — [NBER w20439](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf); [Columbia draft](https://business.columbia.edu/sites/default/files-efs/pubfiles/4607/mom11.pdf)
- Secondary sources put the 1932 momentum loss at about -91% (June–August) and the 2009 Fama-French momentum return at about -52.6%. Crashes come from time-varying beta after market declines, and volatility scaling improves results significantly. — [Alpha Architect](https://alphaarchitect.com/avoiding-momentum-crashes/); [ETF.com / Swedroe](https://www.etf.com/node/94406.md); [ETF.com / Swedroe](https://www.etf.com/node/94015.md)

**Time-series momentum / trend following**
- [PEER-REVIEWED/PRACTITIONER, AQR] Hurst, Ooi & Pedersen (2017), "A Century of Evidence on Trend-Following Investing": time-series momentum built back to 1880 had positive average returns in every decade, low correlation to traditional assets, and did well in 8 of the 10 largest crisis periods. — [AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing); [PDF copy](https://www.chesler.us/resources/academia/A_Century_of_Evidence_on_Trend_Following.pdf)
- Trend following was weak in 2009–2013. The authors note that trend-following performance tends to be weak for about four years after a global financial crisis. Sources give different start dates (1880 vs 1903) for versions of the century study. — [Quantpedia](https://quantpedia.com/strategies/time-series-momentum-effect); [Alpha Architect](https://alphaarchitect.com/time-series-momentum-aka-trend-following-the-historical-evidence/)
- Moskowitz, Ooi & Pedersen (2012) is the foundational TSMOM paper, using futures and forwards from about 1985. Babu et al. (2019) report out-of-sample evidence across 82 additional securities. — [Quantpedia](https://quantpedia.com/strategies/time-series-momentum-effect)
- There is also time-series momentum evidence within individual stocks over nearly 100 years; figures not retrieved. — [Lancaster University eprint](https://eprints.lancs.ac.uk/id/eprint/128366/1/Time_Series_Momentum_in_Nearly_100_Years_of_Stock_Returns.pdf)

**Channel / all-time-high breakouts on single stocks (closest evidence to "Donchian on stocks"; multi-week holds)**
- [PRACTITIONER] Wilcox & Crittenden (2005): buy at the next open after a weekly close at a new all-time high and exit on a 10-ATR trailing stop. The test covered 24,000+ securities over 22 years, with 18,000+ trades, a 49.3% win rate and 0.5% round-trip costs. The authors conclude it has positive expectancy. — [UPenn copy of paper](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf); [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following)
- Niederhoffer's critique: the statistical significance is questionable, small stocks did much better than big stocks late in the sample, and his own tests on S&P 500 stocks produced random results. — [Daily Speculations](https://dailyspeculations.com/vic/trend.html)
- [WORKING PAPER/PRACTITIONER] Zarattini, Pagani & Wilcox (Jan 2025), "Does Trend Following Still Work on Stocks?": survivorship-bias-free data on all liquid US stocks from 1950 to Nov 2024. Under 7% of trades generate most of the cumulative profit, and these properties held out of sample from 2005 to 2024. Transaction costs are a "major challenge" for high-turnover versions, so a turnover-control algorithm is used. — [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following); [Concretum page (fetch blocked)](https://concretumgroup.com/does-trend-following-still-work-on-stocks/)
- Reported performance for that portfolio conflicts slightly between summaries, and no Sharpe ratio was found:
  - 15.19% CAGR and 6.18% annualized alpha gross of fees over 1991–2024 (Concretum summary);
  - 15.02% CAGR, 6.19% alpha and a 31.75% max drawdown, period unclear (Harbourfront Quant).
  — [Concretum summary, via search](https://concretumgroup.com/does-trend-following-still-work-on-stocks/); [Harbourfront Quant](https://harbourfrontquant.substack.com/p/does-trend-following-still-work-on)
- A Zarattini & Antonacci industry-level trend study (1926–2024) reports 18.5% average annual return, 12.1% volatility and a Sharpe ratio of 1.46. This is industry portfolios, not single stocks. — [search summary of Concretum materials](https://concretumgroup.com/tag/momentum/)

**Generic technical rules: data snooping and costs**
- [PEER-REVIEWED] Bajgrowicz & Scaillet (2012, JFE 106(3):473–491) test 7,846 rules (from Sullivan, Timmermann & White 1999) on the DJIA with false-discovery-rate control:
  - before costs, technical analysis looked useful in 1897–1996, even after controlling for data snooping;
  - persistence tests show the future best rules could not have been picked ex ante;
  - transaction costs fully offset even the in-sample performance;
  - in 1997–2007 the outperformance disappears.
  The authors conclude that public technical indicators do not beat their transaction costs. — [IDEAS/RePEc](https://ideas.repec.org:443/a/eee/jfinec/v106y2012i3p473-491.html); [CFA Institute digest](https://rpc.cfainstitute.org/research/cfa-digest/2013/02/technical-trading-revisited-false-discoveries-persistence-tests-and-transaction-costs-digest)

**Post-publication decay and costs**
- [PEER-REVIEWED] McLean & Pontiff (2016) find a 58% post-publication drop in anomaly performance. A later strategy-decay paper estimates a 43% drop in Sharpe ratio. — [arXiv 2105.01380](https://arxiv.org/pdf/2105.01380)
- Another paper describes the McLean–Pontiff result as about 50% lower post-publication returns. It also reports declines of about 25% three years and about 40% five years post-sample, and estimates that about half of the decay is publication bias. — [arXiv 2209.13623](https://arxiv.org/pdf/2209.13623)
- [PEER-REVIEWED] Novy-Marx & Velikov (2016, RFS):
  - costs reduce the profitability and significance of every anomaly studied;
  - most anomalies with under 50% monthly one-sided turnover survive costs when cost-aware, but few higher-turnover ones do;
  - momentum is classed as "mid-turnover", while industry momentum and short-term reversals are high-turnover;
  - a buy/hold spread is the most effective cost mitigation.
  — [NBER w20721](https://www.nber.org/papers/w20721.pdf); [author PDF](https://mysimon.rochester.edu/novy-marx/research/ToAatTC.pdf)
- Frazzini, Israel & Moskowitz (2014) find momentum positive after costs, whereas Novy-Marx & Velikov's net momentum estimate is "MUCH lower". — [Alpha Architect](https://alphaarchitect.com/trading-costs-destroy-factor-investing/)

### Inferences
- Slow breakout signals survive costs only at institutional cost levels and with turnover control. They depend on a small share of outsized winners, so a trader who cuts winners early or holds very few names will likely miss the trades that carry the edge.
- The 52-week-high effect likely overlaps with ordinary momentum, and whether it survives on its own is disputed.
- Decay evidence suggests haircutting any published backtest by at least half before expecting live results.

### Gaps
- The original George & Hwang (2004) tables could not be read. Commonly cited figures were not verified and are omitted.
- No peer-reviewed study of Donchian N-day-high breakouts on individual US stocks with realistic costs was found.
- No source found on momentum-factor or 52-week-high performance in 2020–2026. Exact Sharpe ratios for Moskowitz–Ooi–Pedersen and Hurst–Ooi–Pedersen were not retrieved.

## 2. Swing-horizon evidence (overnight to a few weeks) relevant to a $100, no-day-trading account

### Takeaway
At holding periods of 1 day to about 1 month, the default cross-sectional pattern for US stocks is reversal: last week's or month's winners tend to underperform. The main exception is high-turnover, large and liquid stocks, which show short-term momentum (Medhat & Schmeling 2022). Momentum profits accrue overnight rather than intraday, so overnight holds are the right vehicle for momentum-type signals. Post-earnings drift for large caps may have vanished (Martineau 2022), though 2025 papers dispute this. Attention-driven Robinhood herding buys are followed by -3% to -6% abnormal returns over 5 days. Account mechanics matter too: a $100 account is effectively a cash account, so day trading is limited by settlement rules regardless of the 2026 pattern-day-trader (PDT) rule change.

### Cited Findings
**Short-term reversal vs short-term momentum (1 week to 1 month)**
- Lehmann (1990) and Jegadeesh (1990) contrarian (reversal) profits were sizable, but smaller than likely transaction costs. The reversal is concentrated in high-turnover, illiquid stocks with large market-impact costs. — [Goyal NBER conference paper](https://users.nber.org/~confer/2004/mmsu04/goyal.pdf)
- Trading costs on short-term reversal fall substantially once small caps are excluded — [EFMA 2011 paper](https://efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2011-Braga/papers/0259_update.pdf). One study reports net reversal profits of about 30–50 bps per week — [search summary; Quantpedia](https://quantpedia.com/strategies/short-term-reversal-in-stocks)
- [PEER-REVIEWED] Medhat & Schmeling (2022, RFS 35(3)), "Short-term Momentum": double-sorting on last month's return and share turnover shows reversal among low-turnover stocks but short-term momentum among high-turnover stocks. The momentum survives transaction costs and is strongest among the largest, most liquid and most-covered stocks. — [CEPR DP15857](https://repec.cepr.org/repec/cpr/ceprdp/DP15857.pdf); [City Research Online](https://openaccess.city.ac.uk/id/eprint/31278/)
- Reported gross figures for the winner-minus-loser strategy within the highest-turnover decile conflict between summaries: 1.37% per month (t = 4.74) in one; 1.31% in a CXO summary, which labels it annual in one passage and monthly in another (monthly is more consistent with the 1.74% purged figure); and 1.74%/month when the last 3 trading days of the month are excluded. No net figure was retrieved. — [Alpha Architect](https://alphaarchitect.com/short-term-momentum/); [CXO Advisory](https://www.cxoadvisory.com/momentum-investing/interaction-of-short-term-stock-momentumreversal-and-turnover/)

**Overnight vs intraday returns**
- [PEER-REVIEWED] Lou, Polk & Skouras (2019, JFE), "A Tug of War: Overnight Versus Intraday Expected Returns":
  - momentum abnormal returns are earned almost entirely overnight, and the intraday component is insignificant;
  - size and value premiums accrue intraday instead;
  - across 14 strategies, profits are earned either entirely overnight or entirely intraday;
  - variation in the overnight-intraday spread is about 2% per month;
  - the authors warn that costs make exploiting these patterns much less attractive.
  — [LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/87481); [Alpha Architect](https://alphaarchitect.com/overnight-momentum-vs-intraday-momentum/); [CXO Advisory](https://www.cxoadvisory.com/calendar-effects/momentum-happens-at-night/)
- A secondary summary reports intermediate-term momentum of +0.89% overnight vs -0.18% intraday per month (1993–2013). Not verified against the paper. — [Alpha Architect](https://alphaarchitect.com/2015/02/overnight-momentum-vs-intraday-momentum/)

**Post-earnings-announcement drift (PEAD, a classic multi-week swing signal)**
- [PEER-REVIEWED] Martineau (2022, Critical Finance Review): prices now fully reflect earnings surprises on the announcement day. PEAD has been non-existent in large stocks since 2006 and has disappeared only recently in microcaps. — [Now Publishers](https://nowpublishers.com/article/Details/CFR-0122); [author PDF](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf)
- A UCLA Anderson brief says the drift began disappearing from non-microcaps in 2001 and was gone by 2006, partly linked to faster high-frequency trading after 2005 regulation. Two papers accepted in 2025, including Dickerson, Julliard & Mueller, claim PEAD is "alive and well". Subrahmanyam attributes the disagreement to research-design choices. — [UCLA Anderson Review](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)

**Other signals whose documented horizon is days to weeks (details in sections 4 and 7)**
- The high-volume return premium lasts about 50 days on NYSE data. — [Wharton working paper](https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9901.pdf)
- Option-flow signals work over 1 day to 1 week: low buyer-initiated put/call ratio stocks beat high by about 40 bps next day and about 1% next week (Pan & Poteshman), and weekly option-to-stock volume predicts next-week returns negatively (Johnson & So). — [NBER w10925](https://nber.org/system/files/working_papers/w10925/w10925.pdf); [Emerald JDQS](https://www.emerald.com/insight/content/doi/10.1108/JDQS-11-2023-0036)
- The Jiang–Kelly–Xiu image CNN predicts 5-, 20- and 60-day returns. — [CXO Advisory](https://www.cxoadvisory.com/?p=34917)
- The Robinhood top-bought stocks earn -3% (-6% under extreme herding) over 5 days and -4.7% over 20 days. — [WashU profile](https://profiles.wustl.edu/en/publications/attention-induced-trading-and-returns-evidence-from-robinhood-use/)

**Account mechanics ($100, no day trading)**
- The SEC approved FINRA's Rule 4210 amendments on April 14, 2026 (Release No. 34-105226). Regulatory Notice 26-10 set the effective date as June 4, 2026. The pattern-day-trader designation and $25,000 minimum are removed and replaced by intraday-margin requirements. One source says firms have until October 2027 to fully implement these, and brokers are rolling them out during the phase-in. All of this comes from secondary sources; the SEC/FINRA documents were not checked directly. — [E*TRADE](https://us.etrade.com/knowledge/library/margin/pattern-day-trading-rule-change); [Yahoo Finance](https://finance.yahoo.com/markets/options/articles/sec-eliminates-25-000-pattern-050417843.html); [StockTitan](https://www.stocktitan.net/articles/pattern-day-trader-rule-eliminated-2026); [Wikipedia](https://en.wikipedia.org/wiki/Pattern_day_trader)
- Margin accounts still require the standard minimum, which one source puts at $2,000. — [search summary of PDT-change articles](https://tradezero.com/en-us/blog/the-usd25-000-day-trading-minimum-is-gone-here-s-what-it-means-for-you)
- In a cash account, selling a security bought before it was paid for with settled funds is a "good faith violation". Fidelity restricts an account to settled cash after 3 good-faith violations or 1 free-riding violation in 12 months; Webull's free-ride restriction lasts 90 days. US stocks settle T+1. — [Fidelity](https://www.fidelity.com/trading/faqs-trading-restrictions); [E*TRADE](https://US.eTrade.com/knowledge/library/stocks/understanding-cash-account-violations); [Schwab](https://www.schwab.com/learn/story/avoid-these-violations-when-trading-cash); [Webull](https://www.webull.com/help/faq/11160-Buying-Power)
- Robinhood's own cash-account policy on good-faith violations was not verified; sources conflict.
- Robinhood fractional shares:
  - a fractional buy or sell must be at least $1 in value, and a position worth less than $1 can be sold out — [Robinhood support](https://robinhood.com/us/en/support/articles/fractional-shares);
  - per a Robinhood Learn article, eligible stocks must trade above $1 per share with a market cap over $25 million, and OTC stocks are reportedly excluded — [Robinhood Learn](https://robinhood.com/us/en/learn/articles/how-to-start-investing-for-as-little-as-1-dollar); [Wall Street Survivor](https://www.wallstreetsurvivor.com/?p=33653);
  - not every security is eligible for fractional trading in extended hours, market orders are not supported in extended or overnight sessions, and stop orders placed then queue for the next regular open — [Robinhood extended-hours support](https://robinhood.com/us/en/support/articles/360001226766/extendedhours-trading/).
  Older sources (a 2019 TechCrunch article and a 2020 FINRA addendum) describe fractional trading as market-orders-only and regular-hours-only. These appear outdated, so verify current rules in the app.

**Low-priced / lottery-like stocks (why account size is not a reason to favor cheap stocks)**
- [PEER-REVIEWED] Bali, Cakici & Whitelaw (2011, JFE), "Maxing Out": stocks with the highest maximum one-day return in the past month (top 10% "MAX") subsequently underperform. The authors read this as lottery-seeking investors overpaying. — [Alpha Architect](https://alphaarchitect.com/hot-off-the-jfe-press-maxing-out-your-returns/); [Uni Trier PDF](https://www.uni-trier.de/fileadmin/fb4/prof/BWL/FIN/Files/Maxing_out.pdf)
- [PEER-REVIEWED] Gorman, Akhtar, Durand & Gould (2021, Critical Finance Review) argue that post-high-MAX underperformance is general and reflects a "slow reversal of overreaction" rather than lottery preference specifically. Either way, the stocks that jumped most underperform afterward. — [Critical Finance Review PDF](https://cfr.ivo-welch.info/published/papers/gorman2021could.pdf); [Macquarie](https://researchers.mq.edu.au/en/publications/it-could-be-overreaction-not-lottery-seeking-that-is-behind-bali-/)
- Another study finds the MAX effect unstable over time and sensitive to controls in the US. — [IDEAS/RePEc, J. Behavioral Finance 2022](https://ideas.repec.org/a/taf/hbhfxx/v23y2022i3p338-352.html)
- Kumar (2009), "Who Gambles in the Stock Market?", is cited as evidence that retail investors prefer lottery-type (often low-priced) stocks. Its specific findings were not retrieved in this session.

### Inferences
- For a swing holder, the evidence favors:
  - holding momentum and trend positions overnight and for weeks, since momentum is earned overnight;
  - buying strength mainly in large, liquid, high-turnover names (Medhat–Schmeling short-term momentum; liquid-stock 52-week-high profits);
  - avoiding 1-week to 1-month "chase" entries in illiquid small caps, where reversal dominates;
  - avoiding the day's most-crowded Robinhood names, where herding precedes -3% to -6% abnormal returns over 5 days.
- With fractional shares and a $1 minimum order, share price does not limit which stocks a $100 account can hold. Any eligible stock, including high-priced large caps, can be bought, and the account could in principle hold several small positions. There is therefore no account-size reason to favor low-priced stocks. The evidence points the other way: the more robust short-horizon effects are in large, liquid, high-turnover stocks (Medhat–Schmeling; liquid-stock 52-week-high profits; longer persistence of the high-volume premium in liquid stocks). Lottery-like stocks with extreme recent one-day jumps (high MAX) tend to underperform.
- Even so, a $100 account will hold few positions and make few trades, so outcomes will be dominated by the luck of a few trades. The documented edges (positive skew, under 7% of trades driving profits) need many trades or positions to show up. Even a strategy with a real edge would have very wide outcome dispersion at this scale.
- Because a $100 account is below the margin minimum, it is a cash account. The June 2026 PDT repeal does not, by itself, enable day trading for this user; settlement rules do the limiting. This supports treating intraday strategies as unusable.

### Gaps
- No net-of-cost figure was retrieved for Medhat & Schmeling's short-term momentum.
- No recent re-estimate was found of Jegadeesh–Lehmann reversal profits net of retail-level costs, such as spreads on fractional-share orders.
- Robinhood's specific cash-account settlement and good-faith-violation policy as of Oct 2026 was not verified.
- No study was found of strategy performance at very small (~$100) account sizes or with fractional shares.
- Kumar (2009) on retail gambling in low-priced stocks was not retrieved, and post-2020 evidence on the MAX effect in US stocks was not found.

## 3. Intraday breakout strategies (ORB, "stocks in play", gap-and-go/gap-fade, VWAP): NOT USABLE under the no-day-trading constraint

### Takeaway
NOT USABLE for this user: these are same-day round trips. For completeness, the main intraday evidence is a set of non-peer-reviewed working papers by Zarattini, Aziz and Barbon reporting very large leveraged backtests. The reported edge comes from the "stocks in play" filter (abnormal relative volume, usually news-driven), and a plain ORB was weak. The peer-reviewed intraday-momentum effect is economically small.

### Cited Findings
- [WORKING PAPER] Zarattini, Barbon & Aziz (SFI RP 24-98): a 5-minute ORB on more than 7,000 US stocks from 2016 to 2023. The top-20 "stocks in play" portfolio earned over 1,600% net, with a Sharpe ratio of 2.81 and 36% annualized alpha. Screening rules as summarized:
  - price above $5;
  - 14-day average daily volume of at least 1M shares;
  - ATR above $0.50;
  - opening-range relative volume of at least 100%, top 20 by relative volume.
  The stop is 10% of ATR, and positions exit at the close. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729284); [QuantConnect replication (Sharpe ~2.4)](https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/)
- A plain ORB was weak in that paper. An unclear-provenance critique found the 5-minute window weakest, and replicators say slippage in small, illiquid names is underestimated. — [danfin.net (fetch blocked; via search)](https://danfin.net/opening-range-breakout-research); [GitHub replication](https://github.com/jlmn-code/bot_intradia_orb)
- [WORKING PAPER] Zarattini & Aziz, QQQ/TQQQ 5-minute ORB (2016–2023): 1,484% vs 169% for buy-and-hold QQQ, with 33% alpha net of commissions, using leverage and 1% risk per trade. — [SSRN 4416622](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622); [CXO Advisory](https://www.cxoadvisory.com/technical-trading/day-trading-with-an-opening-range-breakout-strategy/)
- [WORKING PAPER] Zarattini & Aziz VWAP trend (QQQ, 2018–Sep 2023): $25,000 grew to $192,656 net, a 671% return. QuantConnect cites a Sharpe ratio of about 2.10, and a forum thread disputes the result ("not so fast"). — [Bear Bull Traders](https://bearbulltraders.com/?p=2606339); [QuantConnect forum](https://www.quantconnect.com/forum/discussion/16706/bear-bull-traders-039-paper-on-quot-the-holy-grail-quot-not-so-fast/)
- Author ties: Aziz is associated with Bear Bull Traders, a day-trading education business, and Zarattini with Concretum Group, a quant research firm. — [Wikipedia: Andrew Aziz](https://en.wikipedia.org/wiki/Andrew_Aziz)
- [PEER-REVIEWED] Gao, Han, Li & Zhou (2018, JFE): SPY's first half-hour return predicts its last half-hour return (1993–2013). It explains only 1–2% of the variance, and a SPY timing rule earned 6.3% gross per year. — [WashU](https://profiles.wustl.edu/en/publications/market-intraday-momentum/); [CXO Advisory](https://cxoadvisory.com/calendar-effects/first-and-last-half-hours-of-trading-linked)
- Gaps:
  - [PEER-REVIEWED] in a US-stock study, negative gaps are larger than positive ones (more so in Russell 2000 and Nasdaq-100 names), and positive gaps show post-gap drift. The drift may be relevant to overnight-to-multiday holds. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017064/)
  - [ANECDOTAL] about 70% of gaps fill, but the return from trading the fill is about zero. — [Systematic Individual Investor](https://systematicindividualinvestor.com/2018/05/09/dead-simple-the-opening-gap-and-other-intraday-patterns-around-the-market-opening/)
  - [WORKING PAPER] MNQ futures falsification studies find intraday gap and momentum rules mostly fail after costs. — [arXiv 2605.04004](https://arxiv.org/pdf/2605.04004)

### Inferences
- The one transferable lesson for swing trading is that a news-driven relative-volume shock is what separates breakouts that follow through. That is consistent with the multi-week high-volume return premium (section 4).

### Gaps
- Cost and leverage assumptions in the ORB and VWAP papers were not verified (fetch blocked). No independent peer-reviewed replication was found, and no post-2023 out-of-sample results.

## 4. Features that help flag a breakout early: relative volume, volatility contraction, relative strength, float and short interest, pre-market gaps, unusual options activity

### Takeaway
Abnormal volume (the high-volume return premium, about a 50-day horizon) and option-market order flow (1-day to 1-week horizon) have the best peer-reviewed support as early signals, and both fit swing horizons. Relative strength and momentum are well supported at monthly horizons. Volatility-contraction setups (Bollinger squeeze) worked in older index data but not after 2001. VCP, float and "short-squeeze" signals have little or no rigorous support, and high short interest predicts lower, not higher, future returns on average.

### Cited Findings
**Relative volume / volume surges**
- [PEER-REVIEWED] Gervais, Kaniel & Mingelgrin (2001, JF 56(3):877–919), "The High-Volume Return Premium": abnormally high volume over a day or week predicts higher subsequent returns. — [Wharton working paper](https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/9901.pdf); [RePEc](https://ideas.repec.org/p/fth/pennfi/01-99.html)
- One summary says the effect lasts about 50 days on NYSE data. The explanation is Merton's (1987) investor-recognition hypothesis: volume shocks raise a firm's visibility. — [NYU archive copy](https://archive.nyu.edu/bitstream/2451/27578/2/SSRN-id1122463.pdf)
- Kaniel, Ozoguz & Starks (2012) find the premium generally in developed markets but mixed in emerging markets. — [CEPR DP14587](https://repec.cepr.org/repec/cpr/ceprdp/DP14587.pdf)
- The premium disappears quickly for illiquid stocks but persists longer for liquid ones. — [Clute Journals](https://clutejournals.com/index.php/JBER/article/view/7521)
- [PRACTITIONER, counter-evidence] Bulkowski (8,000 patterns, 1991–2011): 14% of patterns with above-average breakout volume failed to rise more than 10%, vs 5% with below-average volume. This contradicts the "volume confirms breakout" rule of thumb. — [ThePatternSite volume study](https://thepatternsite.com/VolumeStudy.html)

**Volatility contraction (Bollinger squeeze, narrow ranges, VCP)**
- [PEER-REVIEWED per CXO summary] Fang, Jacobsen & Qin, "Popularity versus Profitability: Evidence from Bollinger Bands". The squeeze fires on a 6-month low in band width plus a close beyond a band.
  - Over the full sample, the gross buy-minus-sell spread was significantly positive for all 14 indexes.
  - In 1983–2001 the signals worked for only 10 (buy) and 8 (sell) indexes and not for US indexes.
  - After 2001, the daily spread was -0.07% and the strategy was unprofitable gross of costs.
  - The authors attribute the decline to market adaptation.
  — [CXO Advisory](https://www.cxoadvisory.com/big-ideas/when-bollinger-bands-snapped/)
- [PRACTITIONER] A StockCharts squeeze system on S&P 1500 stocks (with trend filter and momentum trigger) reports beating buy-and-hold in a single vendor backtest — [StockCharts](https://articles.stockcharts.com/article/articles-arthurhill-2017-03-systemtrader---testing-a-bollinger-band-squeeze-system-for-stocks-in-the-sp-1500-/). [ANECDOTAL] 399 squeeze events showed 49.6% directional accuracy — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1rdji47/snapshots/2026-02-27T22%3A12%3A05.0165Z)

**Relative strength:** see sections 1 and 2. At 1-week to 1-month horizons, raw relative strength tends to reverse, except in high-turnover large caps. The image-CNN study's closest benchmarks were the Han–Zhou–Zhu TREND signal and 1-week reversal. — [CXO Advisory on JKX](https://www.cxoadvisory.com/?p=34917)

**Short interest / days to cover**
- [PEER-REVIEWED] Diether, Lee & Werner: rising short sales are followed by negative returns for up to 5 days. Their sample averaged short interest of about 3.3% of shares and 4.7 days to cover. — [NBER conference paper](https://users.nber.org/~confer/2005/mmf05/werner.pdf)
- [WORKING PAPER] Hong, Li, Ni, Scheinkman & Yan, "Days to Cover and Stock Returns" (NBER w21166), argue days-to-cover is the better-founded measure. Their sample averaged about 5.5 days to cover (standard deviation 8). Return figures were not retrieved. — [NBER w21166](https://www.nber.org/papers/w21166.pdf)
- UK evidence: large daily short-interest jumps were followed by a -1.48% cumulative abnormal return over 15 days. — [IIUM repository](https://irep.iium.edu.my/28465/)
- [ANECDOTAL] In a 2,269-stock blog backtest, the lowest days-to-cover quintile had the highest returns. — [fffinstill blog](https://fffinstill.com/blog/short-interest-backtest-squeeze-candidates-sector-analysis)

**Unusual options activity**
- [PEER-REVIEWED] Pan & Poteshman (2006): stocks with a low buyer-initiated, position-opening put/call ratio beat high-ratio stocks by about 40 bps the next day and about 1% the next week. The effect is short-lived and relies on non-public signed CBOE data. Unsigned put/call ratios have some predictive power. — [NBER w10925](https://nber.org/system/files/working_papers/w10925/w10925.pdf)
- [PEER-REVIEWED] Johnson & So (2012, JFE): weekly option-to-stock volume is negatively related to next-week returns, predicts earnings surprises, and is stronger when short-sale constraints are higher. Put/call ratios predict better at a daily horizon, O/S better at weekly and monthly horizons. The O/S sign is reversed in Korea. — [arXiv review](https://arxiv.org/pdf/2201.09319); [Emerald JDQS](https://www.emerald.com/insight/content/doi/10.1108/JDQS-11-2023-0036)

**Pre-market gaps:** positive gaps show post-gap drift in one US study, and gaps typically follow news. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10017064/)

**Attention as a negative feature:** Robinhood herding into attention-grabbing stocks predicts negative abnormal returns (section 6). — [WashU profile](https://profiles.wustl.edu/en/publications/attention-induced-trading-and-returns-evidence-from-robinhood-use/)

**Extreme one-day jumps as a negative feature (MAX effect):** stocks with the largest single-day return in the past month subsequently underperform (Bali, Cakici & Whitelaw 2011). The cause is disputed: lottery preference vs slow reversal of overreaction (Gorman et al. 2021). A stock that "breaks out" with one huge up day is, by construction, a high-MAX stock. — [Alpha Architect](https://alphaarchitect.com/hot-off-the-jfe-press-maxing-out-your-returns/); [Critical Finance Review PDF](https://cfr.ivo-welch.info/published/papers/gorman2021could.pdf)

### Inferences
- The most defensible swing-horizon early-breakout feature set is a news-linked abnormal-volume shock, longer-horizon relative strength or nearness to the 52-week high, and a liquid, high-turnover stock. Retail-visible option data is only a weak proxy for the signed flow used in research.
- Volatility contraction seems to predict that a large move is coming, not its direction.
- High short interest is, on average, a bearish signal. Squeeze trades rely on rare tail events.

### Gaps
- No peer-reviewed evidence found for Minervini's VCP, NR7, cup-and-handle patterns, or low float as a breakout predictor.
- No study was found evaluating retail "unusual options activity" scanners.

## 5. How often breakouts fail, and how results change with costs, slippage and small-cap liquidity

### Takeaway
Most individual breakout trades lose or go nowhere. Win rates near 50% are typical for trend systems, profits come from a small minority of trades, and practitioner failure rates for chart-pattern breakouts roughly doubled from the 1990s to the mid-2000s. Costs decide the outcome: gross-profitable technical rules fail net, high-turnover anomalies rarely survive, and breakout and volume effects are weakest or negative in illiquid small caps.

### Cited Findings
- [PRACTITIONER] Bulkowski, failure defined as not rising 10% after an upward breakout:
  - 11% in 1991, peaking at 44% in 2007;
  - an average of 14% in the 1990s bull market vs 28% in 2003–2007;
  - only 12% of chart patterns produced large gains at the start of the 2008 bear market;
  - the study covered 13,932 patterns from 1991 to 2008.
  — [Stocks & Commodities 2009](https://www.traders.com/Documentation/FEEDbk_docs/2009/05/Bulkowski.html); [ThePatternSite](https://thepatternsite.com/FailureRates.html)
- Win rates and trade concentration: all-time-high trend following had a 49.3% win rate with 0.5% round-trip costs, and under 7% of trades generate most profits (1950–2024). — [Wilcox & Crittenden](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf); [CXO Advisory](https://cxoadvisory.com/momentum-investing/all-time-high-trend-following)
- [PEER-REVIEWED] Costs fully offset even the in-sample performance of the best of 7,846 DJIA technical rules — [Bajgrowicz & Scaillet](https://ideas.repec.org:443/a/eee/jfinec/v106y2012i3p473-491.html). Few anomalies with turnover above 50% per month survive costs — [Novy-Marx & Velikov](https://www.nber.org/papers/w20721.pdf)
- Liquidity:
  - the 52-week-high strategy is negative among illiquid stocks — [ANU](https://researchportalplus.anu.edu.au/en/publications/the-impact-of-liquidity-and-transaction-costs-on-the-52-week-high/);
  - the high-volume premium fades fast in illiquid stocks — [Clute Journals](https://clutejournals.com/index.php/JBER/article/view/7521);
  - reversal profits concentrate in illiquid, high-cost stocks — [Goyal](https://users.nber.org/~confer/2004/mmsu04/goyal.pdf).
- [PEER-REVIEWED] Eaton, Green, Roseman & Wu (2022, JFE 146:502–528), using 25 Robinhood outage days in Jan–Aug 2020: in high-retail-interest stocks, less Robinhood participation means smaller order imbalances, better liquidity and lower volatility. The average Robinhood user is 31, vs 50 for the average retail investor. — [SSRN](https://papers.ssrn.com/abstract=3776874); [CXO Advisory](https://cxoadvisory.com/?p=35082)

### Inferences
- A realistic breakout profile is a hit rate of about 50% or lower with a positive skew. Capping upside with tight profit targets removes the source of the edge.
- Retail breakout traders are drawn to small, news-driven, crowded names, where effects are weakest net of costs and retail herding itself worsens liquidity.

### Gaps
- No peer-reviewed false-breakout rate was found for US small-cap swing breakouts, and Bulkowski's 2009–2026 rates were not retrieved.
- No data was found on actual retail fill slippage under payment-for-order-flow routing.

## 6. What happens to retail traders who trade this way: day-trader outcome studies and Robinhood research

### Takeaway
Administrative-data studies are uniformly negative. Fewer than 1% of Taiwanese day traders are predictably profitable net of fees, and 97% of persistent Brazilian futures day traders lost money. Robinhood users' attention-driven herding into top-bought stocks is followed by negative abnormal returns of about 3–6% within 5 days. Welch (2022) shows the aggregate Robinhood crowd portfolio did fine in 2018–2020, which is a different claim from saying attention or breakout trading pays.

### Cited Findings
- [PEER-REVIEWED] Barber, Lee, Liu & Odean, "The cross-section of speculator skill" (J. Financial Markets 2014, 18:1–24), Taiwan 1992–2006: fewer than 1% of day traders are predictably profitable net of fees. The top 500 earn 61.3 bps per day before fees and 37.9 bps after. A working-paper version instead refers to the top 4,000 (<1%). — [RePEc](https://ideas.repec.org/a/eee/finmar/v18y2014icp1-24.html); [Berkeley WP](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/Day%20Trading%20Skill%20110523.pdf)
- A related Barber et al. paper on learning (Review of Asset Pricing Studies 2020) reportedly states that 97% of day traders can expect to lose money. This comes from a search summary and was not verified. — [Berkeley PDF](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/day%20trading%20and%20learning%20110217.pdf); [RePEc](https://ideas.repec.org/a/oup/rasset/v10y2020i1p61-93..html)
- [ANECDOTAL] A claim that 84.3% of 360,000 Taiwanese day traders lost money, with a median return of -8.7%, comes from a TradingView post. Verify before use. — [TradingView post](https://my.tradingview.com/chart/EURUSD/pJsnrpJF-The-Ineffectiveness-of-Day-Trading-A-Critical-Review-of-Empiric)
- [WORKING PAPER] Chague, De-Losso & Giovannetti, "Day Trading for a Living?", Brazilian mini-index futures, traders who started in 2013–2015 and persisted at least 300 days: 97% lost money. Only 1.1% earned more than the minimum wage, and only 0.5% more than a bank teller's starting salary. The authors find no evidence of learning. — [FGV repository](https://repositorio.fgv.br/items/e87d04fc-4b4c-4a56-ab5a-1c84c1afde1b); [RePEc](https://ideas.repec.org/p/fgv/eesptd/525.html); [Quantpedia](https://quantpedia.com/retail-day-trading-is-an-uphill-battle/)
- [PEER-REVIEWED] Barber, Huang, Odean & Schwarz (2022, JF 77(6):3141–3190), "Attention-Induced Trading and Returns: Evidence from Robinhood Users":
  - Robinhood users herd into attention stocks;
  - the top stocks bought each day earn -3% average 5-day abnormal returns, or -6% under extreme herding, and -4.7% over 20 days (SSRN version);
  - herding is linked to the app's simplified display of information;
  - Robinhood outages reduce trading in high-attention stocks.
  — [WashU profile](https://profiles.wustl.edu/en/publications/attention-induced-trading-and-returns-evidence-from-robinhood-use/); [ResearchGate](https://www.researchgate.net/publication/346399054_Attention_Induced_Trading_and_Returns_Evidence_from_Robinhood_Users)
- [PEER-REVIEWED] Welch (2022, JF 77(3):1489–1527), "The Wisdom of the Robinhood Crowd", Robintrack holdings mid-2018 to mid-2020:
  - the crowd added holdings during the March 2020 crash;
  - holdings tilted toward high-volume, mostly large stocks, with volume explaining about 50–60% of weights;
  - the consensus portfolio had good timing and alpha and did not underperform standard benchmark models.
  — [NBER w27866](https://www.nber.org/papers/w27866); [RePEc](https://ideas.repec.org:443/a/bla/jfinan/v77y2022i3p1489-1527.html)
- [PEER-REVIEWED] Eaton et al. (2022, JFE) find Robinhood herding worsens liquidity and raises volatility in high-retail-interest stocks (section 5). — [SSRN](https://papers.ssrn.com/abstract=3776874)

### Inferences
- Welch and Barber et al. are consistent. Holding a diversified, mostly large-cap crowd portfolio did fine, while chasing the day's most-bought attention stocks lost about 3–6% within 5 days, which is squarely a swing horizon. Swing breakout buys of app-trending names resemble the losing behavior.
- Across three markets, the base rate for retail short-horizon speculation is losses for the large majority, with no evidence of learning.

### Gaps
- No SEC/FINRA study of US retail day-trader or swing-trader profitability was found.
- No study was found isolating retail traders who use breakout rules specifically.
- No post-2022 Robinhood outcome studies were retrieved.

## 7. Machine-learning or LLM-based breakout prediction with credible out-of-sample evidence

### Takeaway
The most credible ML result is Jiang, Kelly & Xiu (2023, JF): a CNN trained on chart images predicts 5- to 60-day returns out of sample, which matches the swing horizon. The edge is gross of costs and concentrated in equal-weighted (small-cap) portfolios. In large caps it is much weaker: a value-weighted Sharpe ratio of about 0.6, or slightly above 1 for the top 500 stocks. LLM news-sentiment signals (Lopez-Lira & Tang) weakened over 2021–2024 and face look-ahead and memorization bias. No study was found that predicts "breakouts" specifically with credible after-cost, out-of-sample evidence.

### Cited Findings
- [PEER-REVIEWED] Jiang, Kelly & Xiu (2023, JF pp. 3193–3249): a CNN on daily OHLC, volume and moving-average images. — [Yale-hosted JF article](https://economics.yale.edu/sites/default/files/2023-11/The%20Journal%20of%20Finance%20-%202023%20-%20JIANG%20-%20Re%25E2%2580%2590%20Imag%20in%20ing%20Price%20Trends_0.pdf); [SSRN](https://papers.ssrn.com/abstract=3756587)
- Reported Sharpe ratios conflict between summaries; check the paper's tables:
  - CXO: decile long-short gross Sharpe ratios of about 2.5 equal-weighted and 0.6 value-weighted, vs 1.3 and 0.3 for 1-week reversal with similar turnover. Results hold across horizons and internationally. — [CXO Advisory](https://www.cxoadvisory.com/?p=34917)
  - BSIC: equal-weighted Sharpe ratios of 7.2, 6.8 and 4.9 for the 5-, 20- and 60-day models, falling to slightly above 1 for the top 500 stocks. — [BSIC](https://bsic.it/technical-analysis-on-steroids/)
- The BSIC replication found that 55.9% of test images were "up" and the model's directional accuracy was near a coin toss. Its value came from cross-sectional ranking. — [BSIC](https://bsic.it/technical-analysis-on-steroids/)
- [WORKING PAPER] Lopez-Lira & Tang: ChatGPT headline sentiment predicts next-day returns. The sample runs Oct 2021 to May 2024, with a general decline in performance over that period. — [arXiv 2304.07619](https://arxiv.org/pdf/2304.07619); [CNBC](https://www.cnbc.com/2023/04/12/chatgpt-may-be-able-to-predict-stock-movements-finance-professor-says.html)
- [WORKING PAPER] A Llama-3.3-70B look-ahead test reproduces the effect in-sample (2012–2023): a 0.21% next-day return per signal step, t = 12.18. The authors attribute this partly to memorization and use 2024 as an out-of-sample placebo. — [arXiv 2512.23847](https://arxiv.org/pdf/2512.23847); [arXiv 2309.17322](https://arxiv.org/pdf/2309.17322)

### Inferences
- The ML edge is a gross, small-cap-heavy ranking signal across many stocks. It is not a single-stock timing tool, and it is unlikely to survive retail costs on a $100 account holding one or two names.

### Gaps
- No net-of-cost JKX results, no Gu–Kelly–Xiu (2020) coverage, and no credible evaluation of commercial "AI breakout" tools were found.

## 8. Single-stock backtest selection bias: hindsight ticker choice, small trade counts, data snooping in strategy builders, and backtest-vs-live gaps (applied to the IREN marketing claim)

### Takeaway
A single-stock backtest on a ticker chosen after it became a huge winner, with 18 trades over 3.1 years, is close to uninformative about future profitability. Large-sample evidence shows backtest Sharpe ratios barely predict live results: R² < 0.025 across 888 Quantopian algorithms. Bank "alternative beta" strategies lost about 73–75% of their backtested Sharpe ratio once live. The more configurations a tool tries, the more likely the winner is overfit: more than about 45 configurations on 5 years of data almost guarantees an in-sample Sharpe of 1 with an expected out-of-sample Sharpe of 0. The IREN claim reports neither the number of trials nor out-of-sample results.

### Cited Findings
**Backtest vs live performance (large samples)**
- [PRACTITIONER/WORKING PAPER] Wiecki, Campbell, Lent & Stauth (Quantopian, 2016), "All that Glitters Is Not Gold":
  - 888 US-equity algorithms backtested from 2010 to 2015, each with at least 6–12 months of true out-of-sample live paper trading;
  - backtest Sharpe ratios had almost no predictive power for out-of-sample Sharpe (R² < 0.025);
  - the more backtesting a developer did, the larger the gap between backtest and out-of-sample results;
  - nonlinear ML models using many in-sample features predicted out-of-sample Sharpe better (R² ≈ 0.17).
  — [Quantpedia](https://quantpedia.com/quantopians-academic-paper-about-in-vs-out-of-sample-performance-of-trading-alg/); [CXO Advisory](https://www.cxoadvisory.com/big-ideas/in-sample-vs-out-of-sample-performance-of-888-trading-strategies); [Hedge Fund Alpha](https://hedgefundalpha.com/strategies/comparing-backtest-sample-performance-large-cohort-trading-algorithms/); [paper copy](https://c.mql5.com/forextsd/forum/208/All%20that%20Glitters%20Is%20Not%20Gold%20-%20Comparing%20Backtest%20and%20Out-of-Sample%20Performance%20on%20a%20Large%20Cohort%20o.pdf)
- [PEER-REVIEWED] Suhonen, Lennkh & Perez (2017, Journal of Portfolio Management), "Quantifying Backtest Overfitting in Alternative Beta Strategies":
  - 215 bank-sponsored strategies (from 15 or 17 banks, depending on the source), selected from about 3,000;
  - median Sharpe ratio fell from 1.20 in backtests to 0.31 live, a 73% decline; a typical strategy fell from 1.42 to 0.36, a 75% haircut;
  - only 18 of 215 matched or beat their backtested Sharpe live, and 65 (30%) had negative live Sharpe;
  - the most complex strategies suffered a haircut more than 30% larger than simpler ones.
  — [Alpha Architect](https://alphaarchitect.com/?p=36892); [CXO Advisory](https://www.cxoadvisory.com/big-ideas/live-performance-of-alternative-beta-products/); [Mathematical Investor](https://mathinvestor.org/2017/08/backtest-overfitting-in-smart-beta-investments/)
- [PEER-REVIEWED] Published anomalies lose about 50–58% of their performance after publication (McLean & Pontiff 2016), and about half of that decay is attributed to publication bias. — [arXiv 2105.01380](https://arxiv.org/pdf/2105.01380); [arXiv 2209.13623](https://arxiv.org/pdf/2209.13623)

**Data snooping / number of trials (relevant to "AI-built" strategy generators)**
- [PEER-REVIEWED] Bailey, Borwein, López de Prado & Zhu, "The Probability of Backtest Overfitting" (J. Computational Finance 2015):
  - the probability of overfitting rises with the number of configurations tried;
  - published backtests almost never disclose how many trials were run;
  - trying more than about 45 configurations on a 5-year sample almost guarantees finding one with an in-sample annualized Sharpe of 1 but an expected out-of-sample Sharpe of 0;
  - the paper derives a minimum backtest length as a function of the number of trials;
  - overfitting cannot be assessed when the number of alternatives tried is not reported.
  — [SSRN 2326253](https://papers.ssrn.com/abstract=2326253); [Borwein PDF](https://carmamaths.org/jon/backtest.pdf); [CXO Advisory](https://www.cxoadvisory.com/big-ideas/measuring-investment-strategy-snooping-bias/)
- CXO's summary of the same research group's work stresses the "insidiousness of overfitting investment strategies via iterative backtests". — [CXO Advisory](https://www.cxoadvisory.com/big-ideas/insidiousness-of-overfitting-investment-strategies-via-iterative-backtests)
- [PEER-REVIEWED] Harvey & Liu (2015, JPM), "Backtesting":
  - a Sharpe ratio is converted to a t-ratio and "haircut" for the number of tests run;
  - a t-ratio of 3.0 can be insignificant once multiple testing is accounted for;
  - the haircut is nonlinear: the highest Sharpe ratios take moderate haircuts and marginal ones take heavy haircuts;
  - the authors reject a flat 50% rule;
  - the cross-sectional literature has tested at least 315 factors (Harvey, Liu & Zhu).
  — [Duke PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF); [Man Group summary](https://www.man.com/insights/backtesting)
- [PEER-REVIEWED] Bajgrowicz & Scaillet (2012): even rules that looked significant in-sample could not be identified ex ante, as their persistence tests show. — [RePEc](https://ideas.repec.org:443/a/eee/jfinec/v106y2012i3p473-491.html)

**Small samples / track-record length**
- [PEER-REVIEWED] Bailey & López de Prado (2012, Journal of Risk 15(2)) define the minimum track-record length needed to reject the hypothesis that a measured Sharpe ratio is below a threshold at a given confidence. The required length grows with negative skew and fat tails. — [Risk.net](https://www.risk.net/journal-risk/2223785/sharpe-ratio-efficient-frontier); [PortfolioOptimizer](https://portfoliooptimizer.io/blog/the-probabilistic-sharpe-ratio-bias-adjustment-confidence-intervals-hypothesis-testing-and-minimum-track-record-length/)
- Lo (2002), "The Statistics of Sharpe Ratios": serial correlation can overstate annualized Sharpe ratios. Lo's original was not retrieved; this is from a secondary practice note. — [SLCG practice note](https://www.slcg.com/files/practice-notes/sharpe-ratio.pdf)

**Hindsight ticker selection: IREN context**
- IREN (Iris Energy) pivoted from bitcoin mining to AI cloud and data centers, including a Microsoft deal for AI clusters at its Childress site. One article cites a "nearly 258.9% rally over the past year", article date not shown. A Nasdaq/Zacks piece cites a 397.5% year-to-date gain, year unclear. Mirrored low-quality pages claim about 58% year-to-date in 2026. IREN was therefore an extreme, news-driven winner over the backtest window, but its exact returns are unverified. — [Barchart](https://www.barchart.com/story/news/36409945/this-data-center-stock-could-gain-nearly-195-over-the-next-12-months-is-it-a-buy-here); [Nasdaq](https://www.nasdaq.com/articles/how-can-irens-transition-ai-cloud-benefit-stock)

### Inferences
The arithmetic below is computed from the marketing post's own numbers and is not from a source.
- **Return comparison:** +725% over 3.1 years is about 97.5% per year, vs about 91.0% per year for the +643% buy-and-hold. Ending wealth is 8.25x vs 7.43x, only about 11% more. Nearly all of the strategy's return is IREN's own hindsight-selected rise. The relevant question is what the same rules would have done on stocks chosen before the fact, including the many miners and AI names that fell, and the post does not answer it.
- **Trade count:** 18 trades is far too few to separate skill from luck. One or two trades could account for the entire 82-percentage-point cumulative edge over buy-and-hold.
- **Sharpe uncertainty:** under the standard i.i.d. approximation commonly attributed to Lo (2002), the standard error of an annualized Sharpe ratio is about √((1+SR²/2)/T) (formula not verified from the original here). Over T = 3.1 years that is about 0.70 for a true Sharpe of 1 and about 0.98 for a Sharpe of 2. Before any adjustment for multiple trials, the backtest cannot reliably distinguish a Sharpe of 0 from one of 1.5.
- **Number of trials:** an "AI-built" strategy generator implicitly searches many indicator, parameter, timeframe and ticker combinations. Per Bailey et al. and Harvey & Liu, the reported result must be haircut by the undisclosed number of trials. With roughly 45 or more configurations, an attractive in-sample result is expected even with no edge.
- **Live expectation:** large-sample evidence suggests expecting most of any backtested edge to disappear live (Quantopian R² < 0.025; alternative-beta Sharpe haircut of 73–75%; post-publication decay of 50–58%).
- **Drawdown and execution:** the -38.6% max drawdown on a single stock means a $100 account could fall to about $61 even in the favorable backtest. The 30-minute bars suggest intraday entries and exits, which may conflict with the no-day-trading constraint and with cash-account settlement rules.
- **Conclusion:** the claim does not show consistent profitability. At most, it shows that one in-sample rule roughly matched, and slightly beat, the buy-and-hold return of a stock that was picked after it soared.

### Gaps
- The original marketing post, its platform, and its methodology were not reviewed (not provided or located), including trial count, whether parameters were fit on the same data, commissions and slippage, and whether trades were intraday.
- No peer-reviewed study was found specifically on retail "AI strategy builder" tools or single-ticker backtest marketing.
- IREN's buy-and-hold max drawdown over the same window was not verified, so the post's drawdown comparison could not be checked.
- The original Lo (2002) paper and the Deflated Sharpe Ratio paper (Bailey & López de Prado 2014) were not retrieved directly.
