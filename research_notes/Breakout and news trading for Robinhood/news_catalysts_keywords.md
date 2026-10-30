# News Catalysts, Keywords, Speed of Price Absorption, and News/Filings Data Sources (US equities, as of Oct 2026)

Scope note: Compiled 2026-10-30 from web search results and snippets. Direct page fetches were blocked in this environment (arxiv.org returned ENOTFOUND), so most figures come from abstracts, publisher listings, and secondary summaries. Figures that come only from secondary summaries are marked as such. **User constraint added mid-task: a $100 account that cannot day trade.** That means entry at the next session or later and holds of days to weeks, using free or nearly free data. The notes below therefore flag, for every catalyst, whether the effect survives to a next-day entry.

## Q1. Which catalyst types show measurable abnormal returns, and over what horizon?

### Takeaway
The day-0 jumps are large for M&A targets (about 15-35%), FDA, earnings and similar events, but they are priced on the announcement day or overnight, so a no-day-trade account cannot capture them. The effects that still last days to months after the news are smaller and mostly concentrated in small or illiquid stocks: post-earnings drift (now essentially gone in large caps since about 2006), guidance drift (about 200 bps until the next earnings), analyst-revision and downgrade drift, opportunistic insider buying (about 82 bps/month historically), and 8-K item drifts. Several "positive" catalysts reliably reverse afterward: strategic-alternatives announcements, attention spikes, and short squeezes.

### Cited Findings

**Earnings surprises / PEAD (and whether it has decayed)**
- Martineau, "Rest in Peace Post-Earnings Announcement Drift," *Critical Finance Review* 11(3-4):613-646 (Aug 2022). Prices "fully reflect earnings surprises on the announcement date." For large stocks, PEAD has been "non-existent since 2006," and since 2006 analyst earnings surprises "fail to positively predict post-earnings returns." — [CFR PDF](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf); [IDEAS/RePEc](https://ideas.repec.org/a/now/jnlcfr/104.00000122.html)
- Per a secondary summary of Martineau, drift began disappearing from non-microcap stocks in 2001 and was completely gone by 2006. — [UCLA Anderson Review](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)
- Counter-evidence: two papers accepted for publication in 2025 argue that "PEAD is alive and well." Subrahmanyam (2025, SSRN 5930255, "Keeping it Simple: How Can Post-Earnings Return Drift Exist and Not Exist Simultaneously?") uses US data from Feb 2001 to Dec 2024. With all stocks the PEAD strategy t-stat is 2.18, only just significant. Excluding microcaps, the t-stat falls to 1.43, which is not significant. So the drift that remains sits in microcaps that are "generally illiquid and difficult to trade." — [UCLA Anderson Review](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)
- A Copenhagen Business School thesis on 2020-2024 US data finds PEAD is still significant in small-cap firms with extreme positive surprises (student thesis). — [CBS](https://research.cbs.dk/en/studentProjects/testing-market-efficiency-in-high-volatile-conditions-evidence-fr/)
- Johnson & Schwartz (2001): profits from simple drift strategies had largely disappeared by the late 1990s. What remained was concentrated in small, low-analyst-coverage, low-priced stocks. — [NYU archive PDF](https://archive.nyu.edu/bitstream/2451/27572/2/SSRN-id416302.pdf)
- Zhao, "Explaining the Decline of PEAD: More Arbitrage or Less News?": much of the decline comes from earnings news becoming less persistent, not only from more arbitrage. — [CU Boulder listing](https://experts.colorado.edu/display/pubid_511043)
- A global thesis (2005-2020) finds drift of roughly 1% annually, with most abnormal return concentrated in the announcement window. — [Aalto](https://aaltodoc.aalto.fi/items/4c764bac-bb75-4221-a59f-244e407b49e0)
- Practitioner and blog sources cite Bernard & Thomas's classic drift over about 60 trading days. A JSE study (Swart & Hoffman 2013, non-US) finds drift starts only around trading days 20-40 after the announcement. Berkman et al. (2012) is cited for overnight gains reversing intraday, which is a different horizon. — [search summary of earnings-watcher / NWU repository](https://repository.nwu.ac.za/handle/10394/14128?show=full); [earnings-watcher wiki](https://earnings-watcher.com/wiki/post-earnings-drift-pead)

**Guidance raises / management forecasts**
- Milian (2018, *European Accounting Review*): when quarterly guidance is bundled with earnings, the earnings signal and the guidance signal each produce abnormal drifts of about 200 bps. The drift runs from the day after the announcement through the next earnings announcement, which suggests investors underweight guidance news. — [IDEAS/RePEc](https://ideas.repec.org/a/taf/euract/v27y2018i1p105-128.html)
- Seybert & Yang (2012, *Management Science*): guidance partly corrects sentiment-driven overvaluation but not fully. — [IDEAS/RePEc](https://ideas.repec.org/a/inm/ormnsc/v58y2012i2p308-319.html)
- Industry study (IntelliBusiness / Sharon Merrill, not peer-reviewed): firms giving quantitative guidance show better returns within 20 days than non-guiders. — [IR Magazine](https://irmagazine.com/reporting/giving-guidance-improves-stock-returns-study-finds)
- I found no study that isolates the phrase "raises guidance" (see Gaps).

**Analyst recommendation changes and estimate revisions**
- Womack (1996, *JF* 51:137-167): drift after buy recommendations is +2.4% and short-lived (about 1 month). Drift after sell recommendations is -9.1% and lasts about 6 months. — [IDEAS/RePEc](https://ideas.repec.org/a/bla/jfinan/v51y1996i1p137-67.html); duration detail from a secondary source in [Maynooth PDF](https://mural.maynoothuniversity.ie/id/eprint/20240/1/2006%20issue%202%20article%208.pdf)
- Kecskés, Michaely & Womack (2017, *Management Science*): recommendation changes driven by earnings-estimate revisions earn about 3% per month risk-adjusted, much more than non-earnings-based changes. — [IDEAS/RePEc](https://ideas.repec.org:443/a/inm/ormnsc/v63y2017i6p1855-1871.html)
- Govindaraj, Livnat, Savor & Zhao (1982-2011 data): after large price moves, prices keep drifting when analysts revise in the same direction. A long/short portfolio earned about 1.31%/month abnormal return (Alpha Architect summary; JOIM reports ">1% monthly"). Large moves without a confirming analyst revision tended to reverse in the short term. — [Alpha Architect](https://alphaarchitect.com/2013/03/follow-the-trend-and-the-sell-side/); [JOIM](https://joim.com/?p=4794)
- Prompt analyst revisions move more of the reaction into the announcement window and leave less for drift (Zhang). — [Columbia PDF](https://business.columbia.edu/sites/default/files-efs/pubfiles/3737/zhang.pdf)
- Momentum and PEAD may come from the same source: persistent returns after news about expected earnings (Jackson & Johnson 2006). — [Illinois PDF](https://timothyjohnson.web.illinois.edu/papers/JB_2006.pdf)

**FDA approvals and clinical trial readouts**
- Hamill, Hutchinson, Nguyen & Mulcahy (*Economics Letters* 2018), 233 NYSE pharma approvals from 2009-2015: once event-day misspecification is corrected, the reaction is centred on the event day. The gain is concentrated in after-market-close announcements, so it is realised at the next open. — [UCC CORA](https://cora.ucc.ie/handle/10468/12099)
- Aalto thesis with 476 Phase III announcements and a CAR(-20,+20) window: the results news is priced in when released, with no pre-announcement drift difference between positive and negative readouts. — [Aalto](https://aaltodoc.aalto.fi/items/4fa68b00-387e-4af9-8f14-2afdb87fe865)
- Princeton thesis (2026), minute-level data 2010-2024: limited evidence of significant abnormal returns around FDA decisions, but volatility rises, especially after Complete Response Letters (CRLs). — [Princeton](https://theses-dissertations.princeton.edu/entities/publication/bd23f089-38e8-4418-98ad-0d470d265e28)
- Huddersfield thesis: CARs of 1.5% to 9.2% around FDA designation announcements (not approvals). — [Huddersfield](https://pure.hud.ac.uk/en/studentTheses/strategic-inflection-points-in-biotechnology/)
- AAU thesis (2014-2024): approvals bring significant positive abnormal returns, stronger for smaller and more R&D-intensive firms. — [AAU PDF](https://projekter.aau.dk/projekter/files/784817115/Financial_Determinants_of_Market_Reactions_to_FDA_Drug_Approvals_in_the_Biopharmaceutical_Sector.pdf)

**M&A targets**
- Typical target abnormal return over a short announcement window is 15-30%. — [EventStudyTools](https://www.eventstudytools.com/ma-event-study-example)
- Summary of a 1990-2020 study of 225,243 transactions: average target abnormal return >30%, about 35% for small-cap targets and 19% for large-cap targets (secondary summary). — [Evidence Investor](https://www.evidenceinvestor.com/post/the-takeover-effect-what-it-is-and-how-to-benefit)
- Dutch market 1997-2006: targets beat the market by 5.4% in the 20 days before the announcement, gain a further 14.7% on announcement day, for a 20.9% total. — [CFA VBA NL](https://register.cfavba.nl/publicaties/mergers-and-acquisitions-in-the-dutch-stock-market/acf536d3-edb3-11ea-8a1e-005056b303d3)
- A NASDAQ 2009-2018 thesis finds about a quarter of the run-up occurs before the event date. — [Radboud thesis](https://theses.ubn.ru.nl/handle/123456789/8393)

**Buyback announcements**
- Ikenberry, Lakonishok & Vermaelen (1995), 1980-1990: average 4-year abnormal buy-and-hold return after an open-market repurchase announcement of 12.1%, and 45.3% for value stocks. — [SUFE newsletter abstract](https://academicnewsletter.sufe.edu.cn/info/358169); [NBER w7325](https://www.nber.org/papers/w7325.pdf)
- Lee, Park & Pearson (2019 WP, 1994-2014): post-announcement performance weakened in recent periods. — [KAIST PDF](https://www.business.kaist.ac.kr/faculty/inmoo/Articles/RepurchasesHaveChanged_June2019_final.pdf)
- Bradford (2008): after correcting for multicollinearity in the 3-factor model, the long-run alpha is insignificant. — [Fairfield](https://digitalcommons.fairfield.edu/business-facultypubs/158)

**Index additions (S&P 500)**
- Greenwood & Sammon, "The Disappearing Index Effect" (*JF* 80(2):657-698, Apr 2025). The average addition effect was about 3.4% in the 1980s and 7.6% in the 1990s, but only 0.8% over the most recent decade. The deletion effect fell from about -16% (1990s) to -0.6% (2010-2020), which is not statistically different from zero. Explanations include more additions being migrations from the S&P MidCap, where index-fund flows offset each other, and better absorption of demand shocks. — [NBER w30748](https://www.nber.org/system/files/working_papers/w30748/w30748.pdf); [IDEAS](https://ideas.repec.org/a/bla/jfinan/v80y2025i2p657-698.html); [Alpha Architect](https://alphaarchitect.com/disappearing-index-effect/)

**Contract wins**
- US military contract awards (Palkar, Larson & Larson, *Applied Financial Economics* 2012): positive abnormal returns on the announcement day, both before and after 9/11. — [IDEAS/RePEc](https://ideas.repec.org/a/taf/apfiec/v22y2012i2p147-164.html)
- Larson & Picou test whether government-grantor awards produce larger reactions (event window -3 to +5). — [IPPA PDF](https://www.ippa.org/jopp/download/vol2/issue-2/LarsonPicou.pdf)
- NPS thesis (1993): no abnormal returns in the 30 days before awards for 2 of 4 firms. The others' gains were tied to earnings surprises or sector rallies. — [DTIC](https://apps.dtic.mil/sti/pdfs/ADA277238.pdf)
- EU "Readiness 2030" study (2025/26): defense stocks rose strongly, especially before the announcement. — [UniBS PDF](https://iris.unibs.it/retrieve/handle/11379/628265/369522/1-s2.0-S0165176525003751-main.pdf)

**Short interest / short squeezes**
- Higher short-interest ratios predict lower future returns. Extreme short-sale demand predicts returns for up to about four months, with the predictive power fading within about three months (IBKR research summary). — [Interactive Brokers Campus](https://www.interactivebrokers.com/campus/wp-json/wp/v2/posts/208438)
- A PKU working paper defines a squeeze as a sharp price rise in a short-sale-constrained stock followed by a price reversal. — [PKU PDF](https://english.phbs.pku.edu.cn/uploadfile/2022/0329/20220329025242625.pdf)
- In January 2021 the short-interest factor was on pace for its worst month on record, even excluding GME and AMC. — [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/biggest-short-squeeze-ever)

**Insider buying (Form 4)**
- Cohen, Malloy & Pomorski, "Decoding Inside Information" (NBER w16454; *JF* 2012, 67(3):1009-1043). A portfolio of only "opportunistic" insider trades earns value-weighted abnormal returns of 82 bps per month. "Routine" traders, who trade in the same calendar month for years and make up about 55% of insider trades, earn about zero. Opportunistic trades predict future firm news and announcement returns around forecasts and earnings. — [NBER](https://www.nber.org/papers/w16454); [HBS Working Knowledge](https://hbswk.hbs.edu/item/decoding-inside-information); [Harvard Law Forum](https://corpgov.law.harvard.edu/2012/02/03/decoding-inside-information)
- Form 4 dissemination (Rogers, Skinner & Zechman, *JAR* 2017): mean time to dissemination to paid PDS subscribers was 30 s, versus 40 s to public posting on the SEC site. When subscribers had the advantage, prices, volume and spreads moved about 30 s before public posting. On Dec 19, 2014 the SEC announced a fix so the public site gets filings before PDS subscribers. — [IDEAS](https://ideas.repec.org/a/bla/joares/v55y2017i2p459-505.html); [Alpha Architect](https://alphaarchitect.com/fundamental-investors-following-insider-filings-beware/); [CU Boulder](https://www.colorado.edu/business/faculty-research/2018/06/17/run-edgar-run-sec-dissemination-high-frequency-world)

**8-K filing items**
- Lerman & Livnat (2010, *Review of Accounting Studies*), post-2004 8-K rules: all disclosed items, old and new, are associated with abnormal volume and return volatility around both the event and filing dates. Some items show significant return drift after filing. 10-K/Qs keep their information value. — [IDEAS](https://ideas.repec.org/a/spr/reaccs/v15y2010i4d10.1007_s11142-009-9114-7.html)
- Campbell, Twedt & Whipple: abnormal trading volume is 21% in the hour before a Reg FD 8-K and 13% in the day before. — [SUFE](https://academicnewsletter.sufe.edu.cn/info/410944)
- Cohen, Jackson & Mitts, "The 8-K Trading Gap": insiders earn 42.3 bps of abnormal return per trade in the window between the event and the 8-K filing. — [Harvard Law bibliography](https://hls.harvard.edu/bibliography/the-8-k-trading-gap)
- Class-action settlement 8-Ks: volume rises but there is no significant CAR or front-running. — [JAF](https://articlegateway.com/index.php/JAF/article/view/6498)

### Inferences

**Horizon triage for a $100, no-day-trade account (entry at the next open or later, hold days to weeks)**

| Catalyst | Day-0 effect | Left after a next-day entry? | Evidence basis |
|---|---|---|---|
| M&A target ("definitive agreement") | +15-35% | Mostly gone. A meaningful share runs up before the announcement and the rest is priced on day 0. (Inference, from general knowledge, not verified here: after a cash deal the target usually trades just below the offer price, which leaves little upside.) | EventStudyTools; Evidence Investor; Dutch study |
| FDA approval / Phase III readout | Large, centred on day 0. After-close releases are priced at the next open. | Mostly gone at the next open. The research shows no drift, mainly higher volatility (especially after CRLs). | Hamill et al. 2018; Aalto; Princeton 2026 |
| Earnings surprise, large/mid caps | Priced on announcement day | Gone since about 2006 (Martineau) | Martineau 2022; Subrahmanyam 2025 |
| Earnings surprise, small/micro caps | Priced on day 0, plus drift | Some drift may remain over weeks to a quarter, but it is statistically fragile and concentrated in illiquid microcaps where spreads eat a $100 position | Subrahmanyam 2025; CBS thesis; Johnson & Schwartz |
| Guidance raised with earnings | Day 0, plus drift | About 200 bps drift until the next earnings (historical sample) | Milian 2018 |
| Analyst upgrade | Day 0 | Small residual (+2.4%, about 1 month, 1990s data). Earnings-revision-backed changes are stronger. | Womack 1996; Kecskés et al. 2017 |
| Analyst downgrade / sell | Day 0 | Large historical drift (-9.1% over 6 months). Useful as a "don't buy" or exit filter for a long-only account. | Womack 1996 |
| Large move plus confirming estimate revisions | — | About 1-1.3%/month drift. A move without a confirming revision tends to reverse. | Govindaraj et al. |
| Opportunistic insider buy (Form 4) | Small | About 82 bps/month over months (sample ends around 2010). Form 4s are filed within 2 business days of the trade, which suits a slow trader. | Cohen-Malloy-Pomorski |
| Buyback announcement | Small positive | Long-run drift (12% over 4 years in 1980-90) has weakened and is contested | Ikenberry et al.; Lee-Park-Pearson; Bradford |
| S&P 500 addition | +0.8% recently | Essentially nothing left | Greenwood & Sammon 2025 |
| Contract win | Positive on day 0, sometimes front-run | Little documented post-day-0 drift | Palkar et al. 2012 |
| Short squeeze | Spike | Tends to reverse. High short interest predicts lower returns over about 3-4 months. | IBKR summary; PKU |
| "Strategic alternatives" | +5.3% over 3 days | Then -9.7% over 6 months, so it is a trap (see Q3) | RAS 2025 |

- Inference: the catalysts that best fit next-day-or-later holds are ones the market underweights slowly: guidance, estimate revisions, opportunistic insider buying, and drift in small caps after earnings. Even these have mostly been measured in samples that end before 2015, so post-publication decay is likely.
- Inference: a $100 account faces bid-ask spreads that are large relative to a 1-2% drift in the small and micro caps where drift survives. Net-of-cost returns may well be zero or negative. No source here measures costs at this position size.

### Gaps
- No study found that isolates guidance raises (versus guidance generally) with post-2015 US data.
- I could not confirm the published *JF* 2012 Cohen-Malloy-Pomorski return figure (the 82 bps comes from the NBER WP) or any post-2012 out-of-sample decay of insider-buy returns.
- Two other contract-award studies came up only in a search summary and could not be pinned to a URL: Gomez-Cram et al. (2025), on large federal awards earning abnormal returns concentrated on award days, and Samunderu & Yordanova (2024), on pharma contracts with positive but insignificant returns. They are excluded from the findings.
- I found no magnitude for the reversal after short squeezes. I could not check which specific 8-K items drift (Lerman & Livnat full text not accessed).
- The 2025 "PEAD is alive" papers (e.g., Dickerson et al.) were not directly accessed.

## Q2. What does research show about specific words and text signals?

### Takeaway
Text tone predicts short-horizon returns. Market-level pessimism (Tetlock 2007) produces a temporary drop that reverses. Firm-level negative financial words (Loughran-McDonald) are associated with filing-date returns. LLM headline scores (Lopez-Lira & Tang) predicted next-day returns in 2021-22, mostly in small caps and for bad news. The edge decays as LLM adoption spreads, is inflated by look-ahead bias in backtests, and largely disappears after transaction costs. I found few phrase-level studies; the exception is "strategic alternatives," which is a trap.

### Cited Findings

**Tetlock (2007) – media pessimism**
- Tetlock, "Giving Content to Investor Sentiment: The Role of Media in the Stock Market," *JF* 62 (June 2007):1139-1168. He applied the General Inquirer (Harvard IV-4) to the WSJ "Abreast of the Market" column and built a pessimism factor. High pessimism predicts downward pressure on market prices followed by reversion to fundamentals. Unusually high or low pessimism predicts high volume. Low market returns lead to high pessimism. Media content acts as a proxy for sentiment or noise trading, not new fundamental information. — [Columbia PDF](https://www.columbia.edu/~pt2238/papers/Tetlock_Media_Sentiment_JF.pdf); [SSRN](https://papers.ssrn.com/abstract=685145); [Columbia Business School](https://business.columbia.edu/faculty/research/giving-content-investor-sentiment-role-media-stock-market)
- Garcia extends this to NYT financial columns. The count of negative words predicts daily returns in 1984-1999 (citing Tetlock), and the effects are concentrated in recessions. — [Garcia WP](https://leeds-faculty.colorado.edu/garcia/media_v33.pdf)

**Loughran & McDonald financial sentiment dictionary**
- Loughran & McDonald, "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks," *JF* 66(1), Feb 2011, using 10-Ks from 1994-2008. About three-quarters of the Harvard-negative words are not negative in a financial context (e.g., tax, cost, capital, board, liability, foreign, vice). They built a 2,337-word financial-negative list. More negative 10-Ks (on the LM list) go with lower filing-date returns, while Harvard-negative quintiles show no pattern. The lists also relate to volume, later volatility, unexpected earnings, fraud and material weakness. — [SSRN](https://papers.ssrn.com/abstract=1331573); [UTS PDF](https://www.uts.edu.au/globalassets/sites/default/files/adg_cons2015_loughran-mcdonald-je-2011.pdf); [Alpha Architect](https://alphaarchitect.com/textual-analysis-and-trading-strategies/)

**Phrase-level signals**
- "Strategic alternatives" (*Review of Accounting Studies* 2025, 1,209 announcements): +5.3% three-day reaction, then -9.7% market-adjusted over the next 6 months. The drift appears in nearly all industries and years and survives controls for dividend cuts, external financing and low profitability. An earlier study found +5.4% then -9.1%. Firms that are actually acquired gain; firms not sold suffer. — [Springer RAS](https://link.springer.com/article/10.1007/s11142-025-09917-0); [CLS Blue Sky](https://clsbluesky.law.columbia.edu/2023/02/06/does-the-market-misprice-companies-strategic-alternatives-announcements/); [Duke FinReg](https://sites.duke.edu/thefinregblog/2021/06/10/should-a-company-reveal-that-it-is-evaluating-strategic-alternatives/)
- "Going concern": Taffler, Lu & Kausar (2004) argue the market underreacts, producing later negative drift. Ogneva & Subramanyam (*JAE* 2007) find no significant negative abnormal returns in the US using factor models or after controlling for momentum. The evidence is contested. — [NYU Stern Taffler PDF](https://w4.stern.nyu.edu/finance/docs/pdfs/Seminars/083m-taffler.pdf); [IDEAS (JAE 2007)](https://ideas.repec.org/a/eee/jaecon/v43y2007i2-3p439-452.html)
- "Offering" / seasoned equity offerings: see Q3 (negative announcement returns).

**LLM-based news return prediction**
- Lopez-Lira & Tang, "Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models" (arXiv 2304.07619, v1 Apr 2023 through v6 Oct 2025). ChatGPT labels each headline good, bad or neutral, and the score predicts next-day returns. GPT-1, GPT-2 and BERT cannot forecast returns. GPT-4 long-short gives the highest Sharpe ratio. Predictability is stronger in smaller stocks and after bad news, consistent with limits to arbitrage. Later versions add that strategy returns decline as LLM adoption rises, although some predictability remains in equilibrium depending on noise-trader demand volatility and transaction costs. — [arXiv v5](https://arxiv.org/abs/2304.07619v5); [arXiv v6 PDF](https://arxiv.org/pdf/2304.07619v6)
- Sample: Oct 2021 to Dec 2022, after GPT's training cutoff. One version reports cumulative returns of 350% at 10 bps per-trade cost and 50% at 25 bps. A UCLA presentation reports >400% cumulative and a Sharpe of 3.8 for the GPT-4 long-short. The figures depend on version. — [arXiv v6](https://arxiv.org/pdf/2304.07619v6); [UCLA Anderson slides](https://www.anderson.ucla.edu/sites/default/files/document/2024-04/4.19.24%20Alejandro%20Lopez%20Lira%20ChatGPT_V3.pdf)
- Replication (Vienna thesis): reproduced with lower magnitude, and predictability persists into 2023. It is larger for small caps and short trades, and "only a small part of positive returns seem to persist after transaction costs." — [Univie Phaidra](https://services.phaidra.univie.ac.at/api/object/o:2082913/download)
- Critique (Glasserman & Lin, arXiv 2309.17322, published in *Journal of Financial Data Science*), using 129,431 RavenPack-matched headlines with GPT-3.5. Anonymized headlines outperform originals in-sample: a "distraction effect," where general knowledge of the company hurts. The gap loses significance out-of-sample, implying the in-sample edge comes largely from look-ahead (knowledge of the future). Large firms show borderline outperformance of anonymized headlines even out-of-sample. — [arXiv](https://arxiv.org/abs/2309.17322); [Columbia poster](https://datascience.columbia.edu/wp-content/uploads/2024/01/P021_FB_PosterSession_Fall2023.pdf)
- Chen, Kelly & Xiu, "Expected Returns and Large Language Models": contextual LLM embeddings of news text across 16 markets and 13 languages beat bag-of-words. Trading fresh news "alerts" raises Sharpe ratios further. A Wharton discussant reports an annual Sharpe of about 1.5 and asks whether the predictability is front-loaded. — [Sydney seminar](https://business.sydney.edu.au/events/research/2024/finance/dacheng-xiu); [Wharton discussion PDF](https://jacobslevycenter.wharton.upenn.edu/wp-content/uploads/2024/09/ExpectedReturnAndLLM_Discussion_SophiaZhengziLi_NoPause.pdf)
- 2026 follow-on work on "point-in-time" language models addresses look-ahead bias in this setting. — [arXiv 2607.11889](https://arxiv.org/pdf/2607.11889); review of anonymization methods: [arXiv 2511.15364](https://arxiv.org/pdf/2511.15364)

**Machine-read news analytics**
- von Beschwitz, Keim & Massa: coverage of a story by news analytics (RavenPack) speeds the market reaction, with a larger price update and more volume in the first few minutes. When the analytics mislabel relevance, the market proves fairly resilient. — [NBER conf paper](https://conference.nber.org/conf_papers/f69879.pdf); [CAIA](https://caia.org/node/5557)

### Inferences
- For a next-day-entry account, Lopez-Lira-style scores are the closest documented fit, because the target is the next-day return. But the documented edge sits in small caps and in bad news (short side). A long-only cash account cannot short, the edge shrinks as LLM use spreads, and only a small part survives costs. Treat LLM headline scoring as a filter, not an alpha source.
- The Loughran-McDonald word lists are free and could provide a cheap baseline for scoring press releases and 8-Ks. That use is an inference; the paper's result concerns 10-K filing-date returns.
- "Strategic alternatives," "going concern" and offering language should be negative flags even when the price pops.

### Gaps
- I found no academic studies isolating the phrases "definitive agreement," "FDA approval," "raises guidance," or "offering" as text features with measured return effects. The catalyst-level evidence in Q1 and Q3 is the nearest proxy.
- Exact Lopez-Lira v6 tables were not accessible (arxiv.org fetch blocked).
- I could not verify the Chen-Kelly-Xiu headline numbers or publication status beyond seminar abstracts.

## Q3. Which news is a trap?

### Takeaway
Attention-driven buying, such as Robinhood "Top Movers" herding, Google search spikes, and post-GameStop WallStreetBets posts, predicts negative or reversing returns, especially in stocks under $1B. Strategic-alternatives announcements, equity offerings (worse after a run-up), paid promotions and short squeezes are documented traps. Most of their damage comes over days to months, exactly the holding window of a no-day-trade account.

### Cited Findings
- Barber, Huang, Odean & Schwarz, "Attention-Induced Trading and Returns: Evidence from Robinhood Users" (2020 WP, later *JF*). The top stocks bought each day by Robinhood users have average 5-day abnormal returns of -3%, and -6% in the most extreme herding. Herding relates to the app's simplified display (e.g., the "Top Movers" list) and to attention proxies. During outages, retail trading falls more in high-attention stocks. Per a secondary summary, returns were negative after herding for stocks under $1B market cap but not for those over $1B. Returns are gross of costs. — [SSRN PDF mirror](https://www.smallake.kr/wp-content/uploads/2020/12/SSRN-id3715077.pdf); [UC Davis GSM](https://gsm.ucdavis.edu/news/what-effect-brokerage-robinhood-having-stock-market); [Evidence Investor](https://www.evidenceinvestor.com/post/why-most-robinhood-traders-earn-lousy-returns)
- Barber & Odean, "All That Glitters" (*RFS* 2008): individual investors are net buyers of attention-grabbing stocks, identified by news, unusual volume and extreme returns. This causes temporary positive price pressure. — [IDEAS](https://ideas.repec.org/a/oup/rfinst/v21y2008i2p785-818.html); [PDF](https://www.smallake.kr/wp-content/uploads/2020/12/allthatglitters_rfs_2008.pdf)
- Da, Engelberg & Gao, "In Search of Attention" (*JF*): a rise in Google Search Volume predicts higher prices over the next 2 weeks and a reversal within the year, mostly in small-cap Russell 3000 stocks. It also contributes to large IPO first-day returns and later underperformance. The authors note this is not a tradable strategy after costs. — [UCSD PDF](https://rady.ucsd.edu/faculty/directory/engelberg/pub/portfolios/GOOGLE.pdf); [CXO Advisory](https://www.cxoadvisory.com/?p=2085)
- Bradley, Hanousek, Jame & Xiao, "Place Your Bets?" (*RFS* 2024), with 5,015 due-diligence reports and 13,255 other WSB posts from Jul 2018 to Jun 2021. Before GME, DD reports predicted returns and cash-flow news. An early version reports 1.1% 2-day announcement returns for buy posts and a further +2% over the next month. After GME, the predictability is eliminated, as posts shifted toward price pressure and attention-grabbing stocks. — [U. Kentucky](https://scholars.uky.edu/en/publications/place-your-bets-the-value-of-investment-research-on-reddits-walls/); [CXO Advisory](https://www.cxoadvisory.com/investing-expertise/wallstreetbets-contributors-and-users-skilled)
- An Oxford study finds WSB gives little to no signal about future prices, except for meme stocks such as GME and AMC. — [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:6f3c53d3-f0d6-4232-b3cf-bf1696b200f9/files/dsf268587w)
- Pump-and-dumps: Leuz, Meyer, Muhn, Soltes & Hackethal ("Who Falls Prey to the Wolf of Wall Street?", NBER w24083, *Management Science*) study 470 schemes and trades of more than 110,000 German bank clients from 2002-2015. About 6% of investors participate (another version says about 8%), losing on average nearly 30%. 36% of participants invest in more than one scheme. Some participants are deliberate gamblers. — [NBER](https://nber.org/papers/w24083); [CLS Blue Sky](https://clsbluesky.law.columbia.edu/2017/12/21/who-falls-prey-to-the-wolf-of-wall-street/?amp=1)
- SEC enforcement examples: in 1998, microcap pump-and-dumps used fake "independent" news reports, including a publisher paid about $400,000 in stock and cash by 50 microcaps. In 2015, three penny-stock promoters pumped prices up to 1,800% before dumping for at least $2.8M. — [SEC 1998 release](https://www.sec.gov/news/press/pressarchive/1998/98-92.txt); [Mondo Visione 2015](https://mondovisione.com/media-and-resources/news/sec-charges-three-penny-stock-promoters-behind-pump-and-dump-schemes-1-2015721/)
- Dilutive offerings: a European study of 4,953 offerings (surfaced in search; exact citation not confirmed) finds announcement returns more negative with a larger pre-event run-up, smaller firm size and larger offering size. Other non-US estimates: Sweden about -2.5% on announcement day; Norway (Oslo) -4%; Finland -3.7%. — [Lund thesis](https://lup.lub.lu.se/student-papers/record/3878653); [Vaasa](https://osuva.uwasa.fi/handle/11111/7744); [NHH](https://openaccess.nhh.no/nhh-xmlui/handle/11250/2644662?show=full)
- Strategic alternatives: +5.3% then -9.7% over 6 months (see Q2). — [Springer RAS](https://link.springer.com/article/10.1007/s11142-025-09917-0)
- Short squeezes are defined by reversal after the spike. High short interest predicts lower returns over about 3-4 months. — [PKU PDF](https://english.phbs.pku.edu.cn/uploadfile/2022/0329/20220329025242625.pdf); [IBKR](https://www.interactivebrokers.com/campus/wp-json/wp/v2/posts/208438)
- Retail investors also tend to trade against earnings surprises (study of about 2.8M accounts at a US online broker). This slows price incorporation and contributes to momentum; retail is especially active in small losers. — [NBER conf paper](https://conference.nber.org/conf_papers/f171631/f171631.pdf)

### Inferences
- A news-driven app aimed at Robinhood users risks reproducing the "Top Movers" herding pattern (-3% to -6% over 5 days in sub-$1B names). A next-day entry into yesterday's biggest gainer or most-mentioned ticker is the pattern this research says loses money.
- Practical negative filters: an offering, ATM or shelf filing (S-3/424B) after a run-up; "strategic alternatives"; promotional or paid-sponsor disclaimers; spikes in social or search volume; high short interest with a sudden spike.

### Gaps
- No US-specific magnitude found for offering announcement returns, or for offerings following a sharp run-up in small caps.
- No academic event study found on average returns to paid stock promotions (only enforcement cases and the Leuz et al. investor-loss figure).
- I did not search Stocktwits-specific attention studies.

## Q4. How fast is news priced in?

### Takeaway
For liquid instruments, prices react within milliseconds to seconds: about 5 ms for SPY/ES on macro data, about 30-40 s for EDGAR Form 4 dissemination, and the first few minutes for firm news covered by news analytics. Earnings and FDA news released after the close is mostly priced in the after-hours session or at the next open. A retail app on a typical feed, entering the next day, gets almost none of the announcement jump. It can only hope to capture slower drift, which lives mainly in small, illiquid names.

### Cited Findings
- Chordia, Green & Kottimukkalur (*RFS* 2018, "Rent Seeking by Low-Latency Traders"): SPY and E-mini prices move within about 5 milliseconds of macro surprises. Low-latency profits are only about $19,000 per event for SPY and $50,000 for ES. Speed has increased while profits have not. — [SUFE abstract](https://academicnewsletter.sufe.edu.cn/info/353121); [UNSW PDF](https://www.unsw.edu.au/content/dam/pdfs/business/banking-finance/events/news-events/2021-10-busines-banking-finance-news-events-Low-Latency-Trading-on-Macroeconomic-Announcements.pdf)
- RavenPack metrics arrive about 300 ms after a Dow Jones Newswire release, and news-analytics coverage speeds price and volume response in the first few minutes. — [NBER conf paper](https://conference.nber.org/conf_papers/f69879.pdf)
- EDGAR Form 4: subscribers received filings in about 30 s on average, versus 40 s for public posting, and prices moved about 30 s before public posting (pre-2014 fix). — [Alpha Architect](https://alphaarchitect.com/fundamental-investors-following-insider-filings-beware/)
- After-hours earnings: in a JFE study ("warp speed," 2008-2020; about 90 billion after-hours quotes and about 8 billion after-hours trades), the announcing firm's price jumps in more than 90% of after-hours sessions with an earnings release. — [Aarhus University news](https://law.au.dk/en/current/allnews/news/artikel/reagerer-med-lynets-hast-regnskabsmeddelelsers-afsmitning-paa-markedet)
- JFQA study (S&P 500 firms, 2004-2008): a significant portion of the price change and price discovery happens immediately after after-hours earnings releases. — [Cambridge JFQA](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/information-content-of-earnings-announcements-evidence-from-after-hours-trading/39171BF13B8D5EE4890B930F2FF4E19C)
- Tripathi & Rengifo (*JRFM* 2025, minute-level Nasdaq data): price-volume slopes are steeper in extended hours because liquidity is thinner. — [IDEAS](https://ideas.repec.org/a/gam/jjrfmx/v18y2025i2p75-d1582296.html)
- Blackstone (GSU dissertation, 2025): extended-hours price discovery after earnings has become faster, with more adjustment in the first 15 minutes. — [GSU ScholarWorks](https://scholarworks.gsu.edu/items/14d8839d-615a-4c16-92ed-3d3a9abc1e17)
- FDA approvals: the gain is concentrated in after-market-close announcements and centred on the event day (Hamill et al. 2018). — [UCC CORA](https://cora.ucc.ie/handle/10468/12099)
- Pre-disclosure leakage: abnormal volume of 21% in the hour before Reg FD 8-Ks, and M&A targets run up before announcements (see Q1). — [SUFE](https://academicnewsletter.sufe.edu.cn/info/410944)
- Retail speed is mixed. A UW dissertation says retail traders must judge how much of the return is already priced and often decide poorly. An Arkansas dissertation finds retail as quick as institutions to respond to news existence and coverage. — [UW](https://digital.lib.washington.edu/researchworks/bitstreams/ce78f894-a915-439e-8f68-b93599b07d3a/download); [Arkansas](https://scholarworks.uark.edu/etd/5909)
- Sensational non-financial news days reduce the number of traders by 6-7%, driven by small retail investors staying away. — [INSEAD Knowledge](https://knowledge.insead.edu/economics-finance/sensational-news-distracts-retail-investors)
- Alpaca/Benzinga real-time news carries about 600-900 headlines per day via WebSocket (see Q5). Any retail feed sits downstream of the newswire and EDGAR timestamps above.

### Inferences
- For a no-day-trade account, the announcement-day move is unreachable, whether it happens intraday, after hours or pre-market. The next-day open already reflects it. The relevant question is only whether drift continues from the next open. Per Q1, that drift is near zero for large caps and modest and fragile for small caps.
- Because the account cannot react quickly anyway, a cheap delayed feed (EDGAR, end-of-day news) loses little versus a paid real-time feed for this strategy. Speed matters only for day-0 capture, which this account cannot do.
- (Unverified, from general knowledge) Busse & Green (2002, *JFE*, "Market Efficiency in Real Time") reported that prices respond to CNBC stock reports within seconds to minutes. Search did not surface the paper to confirm this.

### Gaps
- I could not verify Busse & Green (2002) figures.
- No study found that measures typical latency of retail-grade feeds (Benzinga via Alpaca, Massive, Finnhub) versus the primary newswire timestamp.
- No direct study found on how much of a pre-market gap continues or reverses over the following days for small caps. Berkman et al. (2012), on intraday reversal of overnight gains, was cited only secondhand.

## Q5. Which news and filings data sources exist for an app (cost, latency, history, licensing)?

### Takeaway
Given the $100 constraint, the realistic stack is free. SEC EDGAR (free JSON APIs, RSS and full-text search, 10 requests/second) covers filings: Form 4, 8-K, S-3/424B offerings and 13D. Alpaca's Benzinga-sourced news API and Finnhub's free tier cover headlines, and GDELT is free with 15-minute updates. Paid feeds (Benzinga direct, Dow Jones/RavenPack, Massive real-time, Reddit commercial) cost more per month than a $100 account could plausibly earn. Several vendors have changed recently: Polygon became Massive in Oct 2025, and Reddit started charging in 2023.

### Cited Findings

**Free or nearly free (suitable for a $100 account)**
- **SEC EDGAR (free):**
  - Submissions by company and extracted XBRL are served as JSON from RESTful APIs on data.sec.gov, with no API key.
  - The SEC limits each user to 10 requests per second across all machines and may briefly block IPs that exceed it.
  - Automated access needs a declared User-Agent with name and email (stated in third-party guides).
  - The SEC offers RSS feeds and a real-time listing of filings as they are submitted.
  - — [SEC Developer Resources](https://www.sec.gov/developer); [Accessing EDGAR Data](https://www.sec.gov/os/accessing-edgar-data); [SEC rate-control announcement](https://www.sec.gov/oit/announcement/new-rate-control-limits); [SEC search filings](https://www.sec.gov/search-filings); [edgartools compliance guide](https://edgartools.readthedocs.io/en/stable/resources/sec-compliance/)
- **EDGAR full-text search:** coverage starts in 2001 through the public JSON endpoint efts.sec.gov/LATEST/search-index, with no auth. Results are reportedly capped at 10,000 per query (third-party documentation). — [Apify EDGAR FTS](https://apify.com/themineworks/sec-edgar-fulltext-search)
- **Alpaca News API (Benzinga-sourced):**
  - Historical news via REST back to 2015, and real-time via WebSocket. "All news data is currently provided directly by Benzinga."
  - About 130+ articles/day average historically; 600-900 headlines/day in real time. One endpoint covers stocks and crypto, with headline, summary, content, symbols and URL fields.
  - Community reports dispute 2015-2016 coverage gaps. An older forum thread says the real-time feed carried Benzinga newsroom content but not press releases.
  - — [Alpaca historical news docs](https://docs.alpaca.markets/us/docs/historical-news-data); [Alpaca blog](https://alpaca.markets/blog/introducing-news-api-for-real-time-fiancial-news/); [Alpaca forum, press releases](https://forum.alpaca.markets/t/real-time-news-source-not-pulling-press-releases/9281); [Alpaca forum, 2016 gap](https://forum.alpaca.markets/t/historical-news-data-missing-for-2016/13576)
- **Finnhub:** free key at about 60 calls/min for personal, non-commercial use, including company news, real-time US quotes and basic fundamentals. Monetized apps need a paid plan. Paid stock-plan prices conflict across aggregators (about $11.99, $50, $79.99/month; "All-in-One" $1,000/month per TrustRadius). The official forex plans are $49.99 and $129.99/month. — [QVeris comparison](https://qveris.ai/guides/stock-api-free-comparison/); [Finnhub forex pricing](https://www.finnhub.io/pricing-forex-api); [TrustRadius](https://tr-web.dev.trustradius.com/products/finnhub-stock-apis)
- **Massive (formerly Polygon.io):**
  - Renamed Massive.com effective Oct 30, 2025 (one directory says early 2026). api.polygon.io runs in parallel with api.massive.com during the transition.
  - Free tier: 5 calls/min, end-of-day data, 15-min delay. Starter is $29/month; Developer is $79 (another source says $99); Advanced is $199 (third-party figures, Sept and July 2026).
  - A ticker-news endpoint exists. In May 2026 Massive described an expanded Benzinga partnership for real-time news, with no published price.
  - — [FISD](https://fisd.net/polygon-io-is-now-massive); [EIN Presswire](https://www.einpresswire.com/article/863823068/polygon-io-is-now-massive); [apicostcalc](https://apicostcalc.com/blog/polygon-massive-rebrand-api-pricing.html); [Benzinga video](https://benzinga.videonest.co/videos/1548161/powering-your-trading-with-data-XzXCE-_SUA)
- **Tiingo:** free Starter; Power (individual) $30/month; Business $50/month or $499/year for internal use. Commercial and redistribution licenses go through sales. News was historically not in the free tier and was a paid add-on (about $10/month per a dated QuantConnect post). — [QuantStart](https://www.quantstart.com/articles/evaluating-data-coverage-with-tiingo/); [FitGap](https://us.fitgap.com/products/tiingo); [QuantConnect forum](https://www.quantconnect.com/forum/discussion/11887/can-t-access-tiingo-news-data/)
- **GDELT 2.0 (free):** the Event DB and Global Knowledge Graph update every 15 minutes. It covers 100 languages (65 machine-translated live) and has events back to Jan 1, 1979 (more than 300M events). Some intervals have missing data. — [Aalto DataHub](https://datahub.aalto.fi/en/data-sources/the-gdelt-database); [GDELT blog](https://blog.gdeltproject.org/gdelt-reaches-300-million-events/); [gdelt PyPI](https://pypi.org/project/gdelt/)
- **Reddit API:** free for non-commercial use at about 100 queries/min with OAuth (about 10 without). Commercial use is $0.24 per 1,000 calls and requires approval (2023 change). A $12,000/year minimum is claimed by one 2026 guide and disputed by another. — [Octolens](https://octolens.com/blog/reddit-api-pricing); [apicostcalc Reddit](https://apicostcalc.com/reddit-api-cost-calculator.html); [xpoz](https://www.xpoz.ai/blog/guides/reddit-api-pricing-tiers-and-alternatives/)
- **Stocktwits API:** ticker and user streams with OAuth 2.0, rate-limited per hour, public data by default. A 2026 third-party review rates its commercial clarity as weak. No current pricing or partner terms found. — [API Evangelist](https://providers.apievangelist.com/providers/stocktwits/)

**Paid / institutional (out of reach for a $100 account)**
- **Benzinga direct:** REST newsfeed at api.benzinga.com/api/v2/news. API pricing is custom or enterprise ("customize a news feed to fit almost any budget"). Benzinga Pro (the terminal) Streamlined tier is about $197/month. — [Benzinga APIs blog](https://www.benzinga.com/apis/blog/mastering-the-benzinga-newsfeed-api/); [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xwgvhwowjmw3g); [Liberated Stock Trader](https://www.liberatedstocktrader.com/benzinga-pro-review-real-time-news/)
- **Dow Jones / RavenPack:** machine-readable structured sentiment, relevance and novelty. History starts 2000-01-01 (WRDS lists data through 2026-06-30). Latency is about 300 ms after the DJ Newswire. Dow Jones News Analytics launched with RavenPack in 2007. Institutional pricing was not found. — [WRDS RavenPack](https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/ravenpack/); [RavenPack one-sheet](https://wrds-www.wharton.upenn.edu/documents/1164/RavenPack-one-sheet.pdf); [The TRADE](https://www.thetradenews.com/dow-jones-and-ravenpack-launch-analytic-software-for-algorithmic-trading/); [NBER conf paper](https://conference.nber.org/conf_papers/f69879.pdf)
- **FDA / PDUFA calendars:** no official machine-readable PDUFA calendar API was found. Third-party calendars exist; fdatracker.com says it parses SEC filings and press releases and claims SEC filings capture only about 75% of trader-relevant dates. Benzinga also sells an FDA calendar. — [FDATracker](https://www.fdatracker.com/fda-calendar/)

### Inferences
- A minimal free stack for this account:
  - **Filings:** EDGAR submissions JSON and RSS, polled under 10 requests/second, for Form 4 (opportunistic insider buys), 8-K items, S-3/424B (offering traps) and SC 13D. Full-text search catches phrases such as "strategic alternatives" and "going concern."
  - **Headlines:** Alpaca's Benzinga-sourced news (requires an Alpaca account; whether it is free on the basic plan is not verified here) or Finnhub's free tier.
  - **Attention:** Reddit's free tier or GDELT, used as a trap filter.
  - **Model:** an LLM or the Loughran-McDonald lists for scoring.
- Licensing caveat: free tiers (Finnhub, Reddit, Tiingo) are personal or non-commercial. If the app is ever distributed to other users or monetized, commercial licenses are needed and would quickly exceed the account's earning potential.
- Because the strategy holds days to weeks, end-of-day or delayed data is adequate. Paying for low latency buys nothing for a no-day-trade account.

### Gaps
- Not researched or not found: direct PR Newswire, GlobeNewswire and Business Wire feed pricing and latency. Companies often post releases there first and then furnish them on 8-K.
- I could not confirm whether Alpaca's news API is free on its basic plan in 2026, or its rate limits.
- No official Benzinga API price list, Massive news add-on price, or Finnhub stock-plan price from primary pages. Most pricing figures are third-party and should be checked on vendor sites.
- openFDA coverage of approval history was not verified, and no official PDUFA date feed was found.
- Stocktwits 2025-2026 API terms are unknown.
- I could not confirm an official EDGAR RSS refresh interval.
