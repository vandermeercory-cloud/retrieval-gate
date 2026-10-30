# Programmatic and AI-agent access to Robinhood, and alternative brokers with official APIs (as of 30 Oct 2026)

Method note (read first): This cloud session could not reach several hosts directly. WebFetch returned ENOTFOUND for techcrunch.com, docs.robinhood.com, robinhood.com, cdn.robinhood.com and vorplabs.com. Most findings below therefore come from search-result snippets and summaries of the cited pages, not from full-page reads. Any claim that rests on a third-party source, or that conflicts with another source, is flagged. Dates are given as reported. "As of Oct 2026" means the source was surfaced in searches run on 2026-10-30.

## 1. What official Robinhood APIs exist as of October 2026?

### Takeaway
As of October 2026, Robinhood offers two official programmatic routes:
1. **Robinhood Crypto Trading API.** Launched 30 May 2024. It is crypto-only and uses an API key with Ed25519 request signing.
2. **Robinhood Trading MCP server ("Agentic Trading").** Launched in beta on 27 May 2026. It uses OAuth and trades only from a separate, user-funded "Agentic Account". It started with stocks; options and crypto followed, with crypto fully rolled out from about 17 Aug 2026.

Built-in "Robinhood Agents" were announced at HOOD Summit on 29 Sep 2026. Separately, Cortex is a consumer AI feature inside the app. I found no general-purpose REST API for equities or options aimed at retail developers.

### Cited Findings

**Robinhood Crypto Trading API (official)**
- Launch date: Robinhood's newsroom post is dated **May 30, 2024**. It says the API and its documentation were available that day for checking crypto market data, viewing accounts and placing orders programmatically. — [Robinhood newsroom, 2024-05-30](https://robinhood.com/us/en/newsroom/robinhood-crypto-trading-api/); also covered June 2024 by [Crowdfund Insider](https://www.crowdfundinsider.com/2024/06/225864-robinhood-crypto-introduces-api-to-view-market-data-manage-investment-portfolios/) and [Benzinga](https://benzinga.com/amp/content/39089540)
  - No source supported a March 2024 launch date; the earliest dated source is 30 May 2024. — [Robinhood newsroom](https://robinhood.com/us/en/newsroom/robinhood-crypto-trading-api/)
- Eligibility: US Robinhood Crypto customers with an **active Robinhood Crypto account**. — [Robinhood support: Crypto Trading API](https://robinhood.com/us/en/support/articles/crypto-api)
  - Keys are created in a desktop browser on the web interface ("web classic"), under crypto account settings. The user chooses which API actions each key may perform. — [Robinhood support](https://robinhood.com/us/en/support/articles/crypto-api); [Crowdfund Insider, 2024](https://www.crowdfundinsider.com/2024/06/225864-robinhood-crypto-introduces-api-to-view-market-data-manage-investment-portfolios/)
- Versions: there are two, v1 and v2.
  - With v2, customers in eligible jurisdictions can trade with fee tiers, using the API action "Place crypto orders with fee tiers". Only v2 orders count toward fee-tier volume.
  - v1 has "no deprecation timeline" as of the page's last update. The page's update date could not be read.
  - — [Robinhood support: Crypto Trading API](https://robinhood.com/us/en/support/articles/crypto-api)
- Authentication:
  - Each request carries the headers `x-api-key`, `x-timestamp` and `x-signature`. The signature is a detached Ed25519 signature.
  - The private key is a base64-encoded **32-byte Ed25519 seed**: never a 64-byte expanded key, never PKCS#8.
  - One Rust client says the signed message concatenates API key, timestamp, path, method and body. I could not confirm that ordering against the official docs.
  - — [nirholas/robinhood-mcp README](https://github.com/nirholas/robinhood-mcp); [robinrust auth module](https://docs.rs/robinrust/latest/robinrust/auth/index.html); [docs.robinhood.com](https://docs.robinhood.com/), seen as a garbled search snippet only
- Endpoints:
  - Host: `trading.robinhood.com`.
  - Trading paths under `/api/v1/crypto/trading/`: accounts, holdings, orders, cancel order.
  - Market-data paths under `/api/v1/crypto/marketdata/`: best bid/ask, estimated price.
  - — [docs.robinhood.com](https://docs.robinhood.com/); [nirholas/robinhood-mcp](https://github.com/nirholas/robinhood-mcp)
- Order types: market, limit, stop_loss and stop_limit. — [nirholas/robinhood-mcp](https://github.com/nirholas/robinhood-mcp) and [robinrust](https://github.com/Saver05/robinrust). Both are third-party; I could not check the official order schema.
- Rate limits: **100 requests per minute per user account, with bursts up to 300 per minute.** The limiter is a token bucket, and limits are set per endpoint. — [docs.robinhood.com](https://docs.robinhood.com/), via search snippet
  - An older TradersPost page (about 2024–25) said Robinhood published no explicit number. The official figure above supersedes it. — [TradersPost docs](https://docs.traderspost.io/docs/learn/platform-concepts/rate-limits)
- The API is crypto-only. A third-party GitHub project documenting Robinhood's *private* API links to the official docs only for "v1 of their crypto API". — [sanko/Robinhood](https://github.com/sanko/Robinhood); [AlgoTrading101](https://algotrading101.com/learn/robinhood-api-guide/)

**Robinhood Trading MCP / Agentic Trading (official, launched 2026)**
- Launch: on **27 May 2026** Robinhood opened "agentic trading" in **beta**. Users connect their own AI agents to Robinhood's MCP service to analyze holdings and execute trades. At launch it covered **stocks only**. — [TechCrunch, 2026-05-27](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/); [CNBC, 2026-05-27](https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html)
- Robinhood's newsroom post "Robinhood is Now Open to Agents" describes:
  - A dedicated agentic trading account that is **separate from the rest of your portfolio**. The agent "only has access to the funds you deposit into that account."
  - Separate **Trading and Banking MCP servers**, plus an agentic credit card.
  - — [Robinhood newsroom](https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/)
- Endpoint and authentication: the server is at `https://agent.robinhood.com/mcp/trading` and uses OAuth, so the agent never handles the user's password.
  - It is added as a custom connector in Claude Desktop, or with `claude mcp add` in Claude Code.
  - Vorp Labs reviewed the page on 7 Oct 2026 and listed the server as an official public-beta endpoint.
  - — [Vorp Labs, reviewed 2026-10-07](https://vorplabs.com/agent-tools/robinhood-cli); [Walnut comparison, 2026](https://walnutinvest.com/resources/mcp-connectors-for-brokerages-compared); [Gumloop docs](https://docs.gumloop.com/nodes/mcp/robinhood.md), which say "OAuth 2.0"
- Eligibility: sources conflict.
  - Robinhood's X post says the service is free for all US-based Robinhood customers. — [Robinhood on X](https://x.com/RobinhoodApp/status/2079195918595764300)
  - Finovate reports that at launch both agentic trading and the agentic credit card were available to **Robinhood Gold cardholders**, with Platinum cardholders to follow. This may describe the card product only. — [Finovate, May 2026](https://finovate.com/robinhood-lets-agents-trade-stocks-and-make-payments/)
- Supported AI clients: third-party reviews list Claude, Claude Code, ChatGPT, Codex/Codex CLI, Cursor, Grok and other MCP-capable platforms. — [Finder](https://www.finder.com/stock-trading/robinhood-agentic-accounts); [Sentisense](https://sentisense.ai/blog/robinhood-agentic-trading-mcp-review/). Robinhood's support page says you must "choose an AI platform" before connecting. — [Robinhood support: Onboarding an external agent](https://robinhood.com/us/en/support/articles/onboarding-an-external-agent/)
- Data access is broader than trading access.
  - A connected external agent gets **read access to all of the user's Robinhood accounts, including account numbers**. It can **only place trades in the Agentic account**. — [Robinhood support: Onboarding an external agent](https://robinhood.com/us/en/support/articles/onboarding-an-external-agent/)
  - Once data is shared with an AI provider, "it leaves Robinhood's security environment and is governed by that provider's terms." — [Robinhood newsroom](https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/)
- Liability: "By creating an Agentic Account, you authorize third-party AI agents to view your account data and execute trades on your behalf. Robinhood does not control, supervise, monitor, recommend, or audit these AI agents." Users bear losses from agent-placed orders. — [Robinhood newsroom](https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/); [CoinDesk, 2026-09-30](https://www.coindesk.com/markets/2026/09/30/robinhood-is-giving-customers-an-ai-agent-that-trades-for-them-plus-10x-crypto-bets)
- Reported limits on the agent:
  - It cannot trade outside its dedicated account, change security settings, or access login credentials. — reported by [CNBC, 2026-05-27](https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html) and [Finovate](https://finovate.com/robinhood-lets-agents-trade-stocks-and-make-payments/)
  - Robinhood has published no general cap on agent trade size, so the amount funded acts as the position limit. — third-party guide, [Vorp Labs](https://vorplabs.com/agent-tools/robinhood-cli)
- Trade-approval defaults, per Robinhood's help page "Trading with your agent":
  - **Built-in Robinhood Agents:** approvals are **on by default**.
  - **MCP accounts (external agents):** approvals are **off by default**.
  - Trade approvals are "still rolling out" for MCP accounts.
  - — [Robinhood support: Trading with your agent](https://robinhood.com/us/en/support/articles/trading-with-your-agent/), via search snippet, Oct 2026
  - Conflict: a Greenlit review found no approval step in Robinhood's documents, probably reflecting an earlier state. — [Greenlit](https://greenlitbooks.com/field-notes/is-robinhood-agentic-trading-safe)
- Crypto expansion timeline:
  - 1 Jul 2026 keynote: crypto "coming soon" for eligible customers.
  - Robinhood then posted "Agentic Trading for crypto is rolling out now to eligible users… trade crypto alongside equities and options from a dedicated Agentic Account—using only the funds you deposit". This post also shows options were supported by that point.
  - Later post: "100% rolled out… Restrictions apply."
  - — [Robinhood on X (coming soon)](https://x.com/RobinhoodApp/status/2072716802145014050?lang=en); [Robinhood on X (rolling out)](https://x.com/RobinhoodApp/status/2089415757734014987); [Robinhood on X (100%)](https://x.com/RobinhoodApp/status/2094491408514077009)
  - Press dates the rollout to **17 Aug 2026**. — [Crypto Times, 2026-08-18](https://www.cryptotimes.io/2026/08/18/robinhood-rolls-out-agentic-accounts-for-crypto-trading/). An earlier Genfinity report dated a crypto announcement to 20 Jul 2026. — [Genfinity, 2026-07-21](https://genfinity.io/2026/07/21/robinhood-agentic-trading-crypto-ai-agents/)
- Crypto restrictions:
  - An agent's crypto orders need a Robinhood Crypto account that corresponds to the agentic account.
  - Agents can trade crypto but **cannot transfer, stake or lend** it.
  - Agent crypto trading is **unavailable in some states, including New York**.
  - — third-party guide, checked 2026-10-07: [Vorp Labs](https://vorplabs.com/agent-tools/robinhood-cli)
- Product-scope conflicts in third-party reviews:
  - **Farao:** agents can trade equities and **single-leg options**, but not multi-leg options. They cannot short, use leverage or move money out. — [Farao](https://getfarao.com/blog/robinhood-agentic-trading-review)
  - **NexusTrade (a competitor), 8 Jul 2026:** debit spreads not supported; no crypto at that time; OAuth only completed on localhost; "seemingly only one agentic account per user"; "zero docs". — [NexusTrade, 2026-07-08](https://nexustrade.io/blog/robinhood-agentic-trading-mcp-review-20260708); [Medium version](https://medium.com/@austin-starks/i-just-tried-robinhoods-alleged-agentic-trading-i-am-not-impressed-33d3725a23e0)
  - **The Rundown:** tools cover long equities, options and supported crypto pairs, subject to account permissions, product eligibility and state restrictions, with explicit order-review tools. — [The Rundown](https://www.therundown.ai/tools/agentic-trading)
- HOOD Summit (Houston, **29 Sep 2026**):
  - Robinhood announced built-in **Robinhood Agents** and **Agent Apps**. Each trades from a dedicated agentic account.
  - Third-party agents can run natively inside **Robinhood Legend** via the Trading MCP.
  - The Trading MCP remains available for "bring your own agent".
  - Rollout started with summit attendees, with "coming soon" for other eligible US customers.
  - — [Robinhood newsroom: HOOD Summit 2026](https://robinhood.com/newsroom/hood-summit-2026/); [Investing.com transcript](https://www.investing.com/news/transcripts/robinhood-at-hood-summit-26-pushes-trading-into-living-hours-93CH-4923894); [Sentisense](https://sentisense.ai/blog/robinhood-agents-explained/); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/robinhood-unveils-app-ai-agents-094550758.html)
- Regulatory framing:
  - Robinhood's FY2026 10-Q risk factors say agentic trading, "in which autonomous third-party AI agents initiate and execute transactions on behalf of users, presents novel and complex regulatory, privacy and cybersecurity risks." — [Robinhood 10-Q for the period ending 2026-09-30](https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000167/hood-20260930.htm). The snippet did not show which of the 2026 10-Qs holds the quote; [Q2](https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000114/hood-20260630.htm) is also a candidate.
  - Forkast reports that FINRA's 2026 oversight report flags autonomy without human validation, scope creep, auditability and misaligned reward functions. — [Forkast](https://forkast.news/robinhood-gave-ai-agents-a-trading-account-and-a-credit-card-the-liability-gap-just-got-wider/)

**Cortex and Legend (consumer features, not developer APIs)**
- At the December 2025 "YES/NO" event, Robinhood said Cortex lets customers "use plain English to buy and sell equities and crypto, conduct market research, explore event contracts, and adjust their account settings". This is an in-app consumer feature. — [Robinhood newsroom: YES/NO event](https://robinhood.com/newsroom/robinhood-presents-yes-no-event/)
- A third-party review says the Cortex AI assistant is gated to Robinhood Gold at $5/month. — [Tapeboard](https://tapeboard.com/blog/robinhood-legend-gaps)
- In February 2026 Robinhood launched a scanner in Legend with 50+ technical, fundamental, options and price filters, and said "custom scans by Cortex are coming soon." — [Robinhood on X, Feb 2026](https://x.com/RobinhoodApp/status/2019802681326354842)
- HOOD Summit 2025 introduced active-trader tools, none of them a developer API. — [Traders Magazine](https://www.tradersmagazine.com/xtra/robinhood-unveils-powerful-new-tools-for-active-traders-at-hood-summit-2025/); [Investing.com transcript, 2025](https://www.investing.com/news/transcripts/robinhood-at-hood-summit-25-new-tools-for-traders-93CH-4232723)

### Inferences
- For an AI-assistant connector to Robinhood equities or options, the **official Trading MCP plus an Agentic Account is now the only sanctioned route**. The Crypto Trading API remains the only official route for a non-LLM custom app, and it covers crypto only.
- The approval default matters for safety. External MCP agents default to **no per-trade approval**, so a connector must add its own confirmation step or the user must enable approvals where available.
- The MCP's read scope (all accounts, including account numbers) is wider than its trade scope. That matters for privacy, because the data flows to the LLM provider under that provider's terms.
- The product moved quickly between May and October 2026: stocks only at first, then options, then crypto, then built-in agents. Any capability claim older than about a month may be stale.

### Gaps
- I could not read Robinhood's official MCP tool list or schema, its order types (market, limit, stop; extended hours; fractional or dollar-based), or its MCP rate limits; docs.robinhood.com and robinhood.com were blocked. The NexusTrade review (July 2026) said there were no docs at the time.
- Whether the Trading MCP may be called by a plain script rather than an "AI agent" is untested. It is technically an OAuth-protected MCP endpoint, and I found no Robinhood statement either way.
- No source surfaced **Robinhood Connect** (Robinhood's crypto on-ramp partner program), so I did not verify its current status.
- Eligibility (all US customers vs Gold) and whether multi-leg options are supported remain conflicting across sources.

## 2. Unofficial routes (robin_stocks and reverse-engineered clients): authentication, reliability, terms-of-service risk

### Takeaway
Unofficial clients such as robin_stocks call Robinhood's **private, undocumented app API** with username, password and MFA, keeping a device token and pickled session. They break whenever Robinhood changes its login or verification flow (documented repeatedly through at least July 2025). Logging in repeatedly can trigger device-approval prompts or an account lock. I found no official Robinhood statement on restricting accounts for using them. Robinhood legal documents dated 2026 that surfaced in search prohibit automated access or crawling for certain services. The current US Customer Agreement (revised 1 Oct 2026) exists, but I could not read its text.

### Cited Findings
- Robinhood "does not provide any in-house libraries", and robin_stocks-style access is "sort of an unofficial API". — [AlgoTrading101](https://algotrading101.com/learn/robinhood-api-guide/), older guide
- Community projects document the private API. — [sanko/Robinhood: "Unofficial Documentation of Robinhood Trade's Private API"](https://github.com/sanko/Robinhood)
- robin_stocks authentication: the login takes username, password and an optional `mfa_code` (TOTP), and stores a session and device token. — [robin_stocks authentication module docs](https://robin-stocks.readthedocs.io/en/latest/_modules/robin_stocks/robinhood/authentication.html)
- Reliability history (dates as given):
  - **PR #300 (around 2018):** the saved `device_token` diverged from the one sent to Robinhood, causing repeated failures. The author reported needing to re-log in about monthly. — [robin_stocks PR #300](https://github.com/jmfernandes/robin_stocks/pull/300)
  - **Issue #513:** login failed because the code expected an access token that never came back, before the MFA prompt. — [Issue #513](https://github.com/jmfernandes/robin_stocks/issues/513)
  - **Issue #521:** "login(... mfa_code=totp) started failing on Dec 17". The year was not visible in the snippet. — [Issue #521](https://github.com/jmfernandes/robin_stocks/issues/521)
  - **Issue #530:** "login is broken". The workaround was to pass `mfa_code` explicitly. — [Issue #530](https://github.com/jmfernandes/robin_stocks/issues/530)
  - **Issue #1621 (July 2025):** Robinhood changed its verification approach, and trusted-device status had to be rebuilt before login worked again. — [Issue #1621](https://github.com/jmfernandes/robin_stocks/issues/1621)
- Lockout risk: a go-trader issue (about October 2026) warns that logging in fresh on every run, with a new random device token each time, can trigger device-approval pushes, SMS codes or an **account lock**. Reusing a stored session and a stable device token avoids this. A related PR refuses a Robinhood login unless the library holds the returned token. — [richkuo/go-trader issue #1818](https://github.com/richkuo/go-trader/issues/1818); [PR #1829](https://github.com/richkuo/go-trader/pull/1829). These are third-party; Robinhood has not published such guidance.
- Terms of service (documents surfaced in search; not fully read):
  - **Robinhood Customer Agreement, revised 1 Oct 2026** (Robinhood Financial LLC & Robinhood Securities, LLC). It exists, but I could not read its automated-access or third-party-access text. — [Customer Agreement PDF](https://cdn.robinhood.com/assets/robinhood/legal/Robinhood-Customer-Agreement.pdf)
  - **Robinhood Social User Agreement, effective 18 Sep 2026:** "You may not access or collect data from Robinhood Social using automated means." — [PDF](https://cdn.robinhood.com/assets/robinhood/legal/robinhood_social_user_agreement.pdf)
  - **Robinhood Banking Mobile Application Terms of Use, effective 1 Jun 2026:** prohibits using software to crawl or spider pages, and actions that burden the infrastructure or interfere with the Services. — [PDF](https://cdn.robinhood.com/assets/robinhood/legal/robinhood_banking_mobile_application_terms_of_use.pdf)
  - **Older (2018) Robinhood Financial Customer Agreement:** covers "automated systems" and "API licensees", and says granting a third party access to an account is at the account holder's own risk. On its face it does not itself ban scraping. — [RHF Customer Agreement 2018](https://brokerage-static.s3.amazonaws.com/assets/robinhood/legal/RHF%20Customer%20Agreement.pdf)
  - A "Robinhood App Use Standards" document exists, but its text was not retrieved. — [PDF](https://cdn.robinhood.com/assets/robinhood/legal/robinhood-app-use-standards.pdf)
- No official Robinhood notice on restricting automated or unofficial-API accounts in 2026 turned up. — search of GitHub issues and the web, 2026-10-30; see [go-trader #1818](https://github.com/richkuo/go-trader/issues/1818) for the only lock-related warning

### Inferences
- Now that Robinhood ships an official agent route (May 2026) and an official crypto API (2024), unofficial private-API clients are harder to justify. They carry ToS ambiguity, MFA and device-verification brittleness, possible account locks, and full-account credential exposure. The official MCP instead isolates funds and uses OAuth.
- Unofficial clients give a script full trading authority over the main brokerage account. The official route deliberately prevents this.

### Gaps
- I could not read the exact current US Customer Agreement language on automated access, scraping, bots or third-party apps; cdn.robinhood.com was blocked.
- No verified first-hand reports surfaced of accounts restricted specifically for robin_stocks use in 2025–2026.
- I did not determine robin_stocks' current (Oct 2026) working status.

## 3. MCP servers and Claude/ChatGPT connectors for Robinhood and other brokers; credential handling and order confirmation

### Takeaway
By October 2026, most major US brokers ship an **official** MCP server or connector. Robinhood, Public, Webull, Interactive Brokers and Tradier host theirs, using OAuth or tokens. Alpaca and tastytrade publish open-source servers you run yourself, using API keys or OAuth refresh tokens. Order-safety designs differ:
- Robinhood (external agents): approvals off by default.
- IBKR: drafts orders only; the user submits them.
- tastytrade: dry-run gate before submission.
- Alpaca: paper mode by default.
- Webull local server: $10k per-order cap by default.
- Public: trades with user approval, per a third party.

### Cited Findings
- 2026 connector landscape, per a third-party comparison (Walnut, 2026):
  - TradeStation: January.
  - Public: hosted MCP, 31 March.
  - Robinhood: 27 May.
  - Interactive Brokers: certified Claude and ChatGPT connectors by 8 June; open to any MCP client since 28 July.
  - Webull: August.
  - tastytrade: September.
  - Moomoo: also has a connector.
  - Walnut says Robinhood's, Public's and Webull's official connectors place orders, while IBKR's **drafts orders for you to submit**. Each connector covers only its own broker. — [Walnut: MCP Connectors for Brokerages, Compared (2026)](https://walnutinvest.com/resources/mcp-connectors-for-brokerages-compared); [Walnut guide](https://walnutinvest.com/resources/mcp-connectors-for-investing)
- **Robinhood (official):** see section 1.
  - Hosted at `agent.robinhood.com/mcp/trading` with OAuth. — [Vorp Labs, 2026-10-07](https://vorplabs.com/agent-tools/robinhood-cli)
  - Approvals are off by default for external agents and on by default for built-in agents. — [Robinhood support](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)
  - Setup walkthroughs for Claude exist. — [SecProve](https://secprove.com/trading-agent-safety/connect-claude); [Ryan Doser](https://ryandoser.com/ai-trading-agent-robinhood/)
- **Community Robinhood MCP servers:**
  - `nirholas/robinhood-mcp` wraps the official Crypto Trading API at trading.robinhood.com, using API key and Ed25519 credentials. — [GitHub](https://github.com/nirholas/robinhood-mcp)
  - An MCP listing for a Robinhood crypto server defaults to 100 requests per 60 s. — [mcpmarket](https://mcpmarket.com/server/robinhood)
  - Other community projects exist; I did not check which API they use. — [kevin1chun/robinhood-for-agents](https://github.com/kevin1chun/robinhood-for-agents); [zaydiscold/robinhood-cli-mcp-api](https://github.com/zaydiscold/robinhood-cli-mcp-api); [agenthood on PyPI](https://pypi.org/project/agenthood/)
- **Alpaca (official, self-hosted):** `alpacahq/alpaca-mcp-server`.
  - Trades stocks, ETFs, crypto and options.
  - v2 is a complete rewrite on FastMCP and OpenAPI, with 65 tools across the Trading and Market Data APIs.
  - Credentials are the env vars `ALPACA_API_KEY`, `ALPACA_SECRET_KEY` and `ALPACA_PAPER_TRADE`. It **defaults to paper**; live trading needs `ALPACA_PAPER_TRADE=false` and live keys.
  - Clients: Claude Desktop, Claude Code, Cursor, VS Code, Gemini CLI and others.
  - — [GitHub](https://github.com/alpacahq/alpaca-mcp-server); [Alpaca docs: Trading API MCP](https://docs.alpaca.markets/us/docs/trading-api-mcp); [Alpaca MCP page](https://alpaca.markets/mcp-server)
- **Interactive Brokers:**
  - The hosted MCP is reportedly at `https://api.ibkr.com/v1/api/mcp`, using Streamable HTTP and OAuth; the first connection opens a browser login. — [mcpservers.org](https://mcpservers.org/zh-TW/remote-mcp-servers/ibkr)
  - A public endpoint `/v1/api/mcp-public` reportedly has about 34 tools: account data, price history, contract search, watchlists, alerts, and **draft orders it never places autonomously**. — [NousResearch/hermes-agent issue #110937](https://github.com/NousResearch/hermes-agent/issues/110937)
  - An agent directory says IBKR's developer docs contain no MCP section, and reports scopes `mcp.read` and `mcp.write`. — [Agentman](https://agentman.ai/agentskills/connections/mcp-server/interactive-brokers)
  - The community `interactive-brokers-mcp` package is unofficial, not endorsed by IBKR, and alpha. — [code-rabi/interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)
- **Public.com (official):**
  - The hosted MCP lets you connect from Claude and ChatGPT without running a server; docs also cover Perplexity. Claude Code setup instructions were added 11 Aug 2026. — [Public API changelog](https://public.com/api/docs/changelog)
  - Self-run `publicdotcom-mcp-server` wraps the `publicdotcom-py` SDK. Tools include quotes, bars and `place_order` for single-leg stocks, crypto and options. It runs over stdio or HTTP `POST /mcp`. — [PyPI](https://pypi.org/project/publicdotcom-mcp-server/0.5.1/); [GitHub](https://github.com/publicdotcom/publicdotcom-mcp-server)
  - The community `Gajesh2007/public-com-mcp` has trading tools **off by default** behind an env flag. — [GitHub](https://github.com/Gajesh2007/public-com-mcp)
- **Webull (official):**
  - The **local MCP** needs an App Key and App Secret. Its token is valid 15 days and auto-refreshes. Accounts with 2FA must approve the request in the Webull app. By default it **caps US order value at 10,000 USD** and uses the **sandbox** environment unless set to production. — [Webull Local MCP docs](https://developer.webull.com/apis/docs/AI-friendly-Resources/local-mcp/); [webull-inc/webull-mcp-server](https://github.com/webull-inc/webull-mcp-server)
  - The **cloud MCP** at `https://api.webull.com/mcp` uses OAuth. A 29 Sep 2026 release says it is available to eligible US users via Claude, Perplexity and Grok, with ChatGPT pending. — [Webull docs / Vorp Labs](https://vorplabs.com/agent-tools/webull-mcp); [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/webull-launches-mcp-server/)
  - Conflict: Webull's local-MCP page says "No application required", while a third-party guide says local paths need an approved Trading API application. — [Webull docs](https://developer.webull.com/apis/docs/AI-friendly-Resources/local-mcp/); [Vorp Labs](https://vorplabs.com/agent-tools/webull-mcp)
- **tastytrade (official, self-hosted):** `tastytrade/tastytrade-mcp`.
  - Credentials stay on the user's machine. It needs an OAuth client ID, client secret and refresh token, created under My Profile → API.
  - Sandbox and production credentials are separate. `TASTYTRADE_ENV` selects production or sandbox.
  - Order submission is gated behind a **dry-run-first confirmation flow**.
  - — [GitHub](https://github.com/tastytrade/tastytrade-mcp); [tastytrade dev docs: MCP Server](https://developer.tastytrade.com/docs/sdks-and-tools/mcp-server/); [tastytrade newsroom](https://tastytrade.com/newsroom/news/open-api-mcp-brings-ai-to-your-tastytrade-account/)
- **Tradier (official, hosted):** Streamable HTTP, 22 tools including docs search; a paper-trading flag selects sandbox or live. — [Tradier MCP docs](https://docs.tradier.com/docs/tradier-mcp)
- **Schwab and E*TRADE:** only community MCP servers surfaced; I found no official one. — [Schwab MCP (community) on LobeHub](https://lobehub.com/mcp/acidsolution-schwab-mcp-server); [E*TRADE MCP (community) on mcpmarket](https://mcpmarket.com/server/e-trade); [glama listing](https://glama.ai/mcp/servers/xelh3tvyap)

### Inferences
- Credential patterns fall into two groups:
  - **Hosted OAuth:** Robinhood, IBKR, Public hosted, Webull cloud. These suit consumer AI assistants because no secrets sit on disk.
  - **Self-hosted with keys or refresh tokens:** Alpaca, tastytrade, Webull local, Public self-run. These suit developers who want control and auditing.
- The safest defaults for an AI connector are IBKR (draft-only), tastytrade (dry-run gate), Alpaca (paper default) and Webull local (order cap). Robinhood's MCP default for external agents (no approvals) is the least conservative. Robinhood mitigates this with fund isolation.

### Gaps
- I found no official Claude connector directory listing; I could not confirm which brokers are "certified" in Anthropic's or OpenAI's directories beyond Walnut's claims.
- I did not obtain Public's exact personal-access-token scopes or its MCP approval flow.

## 4. Alternative brokers with official retail trading APIs: comparison

### Takeaway
For a US retail developer building breakout or news trading tools, each broker fits a different need:
- **Alpaca** is the easiest start: API keys, free paper trading, a Benzinga-powered news API with WebSocket, no minimum and an official MCP.
- **Interactive Brokers** is the most complete, covering the most asset classes, but its data subscriptions and setup are heavier.
- **tastytrade and Tradier** suit options-focused traders.
- **Schwab and E*TRADE** have official APIs, but their OAuth flows need a human to re-authorize regularly (Schwab every 7 days, E*TRADE daily), and neither has an official MCP.
- **Public and Webull** now have official APIs plus hosted MCPs.

### Cited Findings

**Alpaca**
- Assets: stocks, ETFs, crypto and options. — [alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)
- Commissions: "in general" no commission on trades, though some partner arrangements may preclude commission-free trades. Revenue comes from payment for order flow, interest, margin, crypto spreads and data subscriptions (per a third-party review). — [SmartAsset 2026](https://smartasset.com/investing/alpaca-trading)
- Paper trading: free, with a simulated $100K. Fills are simulated against real quotes with random partial fills, and some features (for example short-sale locates) are unavailable in paper. — [SmartAsset 2026](https://smartasset.com/investing/alpaca-trading); [Kagels Trading 2026 review](https://kagels-trading.com/blog/alpaca-review/)
- News API (with Benzinga): historical news via REST and real-time via WebSockets, an estimated 600–900 articles or headlines per day. — [Alpaca docs: News API](https://alpaca.markets/docs/news-api); [Alpaca blog](https://alpaca.markets/blog/introducing-news-api-for-real-time-fiancial-news/); partnership announced Feb 2022 — [BusinessWire](https://www.businesswire.com/news/home/20220222005083/en/Alpaca-and-Benzinga-Partner-to-Offer-Fintech-Apps-Stock-Market-News)
- Paid data: Algo Trader Plus costs about **$99/month**, per third-party trackers. It includes full real-time SIP, real-time OPRA options data, unlimited WebSocket symbols and up to 10,000 API requests per minute. — [apis.io plans](https://apis.io/plans/alpaca-markets/alpaca-markets-plans-pricing/); [PricingSaaS](https://pricingsaas.com/companies/alpaca)
  - The Alpaca Elite program includes Algo Trader Plus free ("value of $99/month") for personal use with a $100,000 deposit. — [Alpaca blog: Alpaca Elite](https://alpaca.markets/blog/introducing-alpaca-elite-low-cost-advanced-algorithmic-trading-with-white-glove-support/)
- Minimums: none for individual taxable accounts. Business accounts need $50,000 per one Alpaca doc; older pages say $30,000, so sources conflict. — [Alpaca support: minimum deposit](https://alpaca.markets/support/alpaca-minimum-deposit); [Alpaca docs: account plans](https://docs.alpaca.markets/docs/account-plans)
- Authentication: API key and secret. Official MCP: yes, self-hosted; see section 3. — [Alpaca docs](https://docs.alpaca.markets/us/docs/trading-api-mcp)

**Interactive Brokers (IBKR)**
- APIs: TWS API and Web API. The Web API uses OAuth 2.0 with signed JWT client assertions, and IBKR is consolidating its web APIs into a single "IBKR Web API". — [IBKR Campus: Trading Web API](https://www.interactivebrokers.com/campus/ibkr-api-page/web-api-trading/); [Agentman](https://agentman.ai/agentskills/connections/mcp-server/interactive-brokers)
- API cost: $0 monthly minimum for the TWS and Web APIs per IBKR's required-minimums schedule, as reported by a third party; there is no API subscription. — [PickMyTrade, 2026](https://blog.pickmytrade.io/ibkr-api-cost-every-charge-itemised-2026/)
- Market data:
  - Most securities need a Level 1 subscription; forex and crypto do not.
  - API data needs **IBKR Pro, not Lite**. Clients should hold $500 plus the cost of subscriptions.
  - A Market Data API Acknowledgement is required.
  - — [IBKR Campus: market data subscriptions](https://www.interactivebrokers.com/campus/ibkr-api-page/market-data-subscriptions/)
- Paper trading: the paper account mirrors the live account's permissions and market data subscriptions, and uses separate credentials. — [IBKR glossary](https://www.interactivebrokers.com/campus/wp-json/wp/v2/glossary-terms/179994); [PickMyTrade](https://blog.pickmytrade.io/ibkr-api-cost-every-charge-itemised-2026/)
- Lite vs Pro plan comparison. — [IBKR plans page](https://www.interactivebrokers.com/en/general/compare-lite-pro.php). I did not extract the commission figures.
- Official MCP: hosted, OAuth, draft-only orders, per third parties; see section 3.

**Charles Schwab Trader API**
- Individual developers apply on the Schwab Developer Portal. After a "quick review" they choose "Trader API – Individual" or "Commercial". This comes from a 2023 transition-era forum post. — [TD Ameritrade API forum](https://apiforums.tdameritrade.com/node/116)
- OAuth: the access token lasts 30 minutes and the **refresh token 7 days**. Auto-refresh does not extend the 7 days, so a browser login is required weekly. Refresh tokens rotate. — [schwabr CRAN docs, 2026](https://cran.r-project.org/web/packages/schwabr/readme/README.html); [Jose and Goose blog](https://joseandgoose.com/writing/how-i-self-healed-schwab-oauth); [LobeHub Schwab MCP](https://lobehub.com/mcp/acidsolution-schwab-mcp-server)
  - One R package says Schwab indicated this "might change in the future", with no timeline. — [schwabr](https://cran.r-project.org/web/packages/schwabr/readme/README.html)
- Streaming: a WebSocket Streamer with 15 services. No sandbox was published, per a third-party package README. — [dp_exchange_schwab README](https://hex.pm/packages/dp_exchange_schwab/0.2.5/files/README.md)
- Commissions: equity options $0.65/contract, no account minimum, per a third-party comparison. — [QuantWheel](https://quantwheel.com/marketplace/brokers/schwab-vs-tastytrade)
- Official MCP: none found; a community server exists.

**Tradier**
- API access is included with the brokerage account at no extra charge. — [Tradier docs](https://docs.tradier.com/docs/getting-started). A third-party review lists a $10/month tier, which conflicts. — [Tradier API review](https://algoplatforms.com/broker-apis/tradier-api)
- Authentication: bearer tokens from the API settings page. Per Tradier's FAQ, "OAuth is not enabled for this type of API access as it is available for personal use only". This conflicts with a review that says OAuth 2.0. — [Tradier FAQ](https://docs.tradier.com/docs/faq#/)
- Streaming at `stream.tradier.com/v1` over WebSocket or HTTP. The sandbox has 15-minute delayed data and paper fills, and **no streaming in paper**. Futures are not available. — [Tradier docs: endpoints](https://docs.tradier.com/docs/endpoints)
- Commissions:
  - Options: $0.35/contract standard, per a third party. — [TradingToolsHub 2026](https://tradingtoolshub.com/review/tradier/)
  - Pro Plus plan: $0.10/contract on SPX and $0.00 on SPY/QQQ, rates as of March 2026. — [Tradier promo page](https://trade.tradier.com/ovtlyr/)
- Official MCP: hosted, 22 tools. — [Tradier MCP docs](https://docs.tradier.com/docs/tradier-mcp)

**Public.com**
- Assets via the API: stocks, ETFs, options, crypto and prediction markets. Authentication is by personal access token (`POST` Create personal access token). — [Public API docs](https://public.com/api/docs)
- "The Public Individual API is for your own personal, non-commercial use." — [Public API docs](https://public.com/api/docs)
- New API crypto fee tiers by monthly volume took effect 16 Jun 2026; I did not retrieve the fee table. — [Public API changelog](https://public.com/api/docs/changelog)
- Official MCP: hosted and self-run; see section 3.

**Webull OpenAPI**
- Individuals apply in-account under OpenAPI management. Review typically takes 1–2 business days; sandbox applications are auto-approved within minutes. — [Webull: Trading API Application](https://developer.webull.com/apis/docs/authentication/IndividualApplicationAPI/); [Webull FAQ](https://developer.webull.com/apis/docs/faq/)
- Authentication: App Key and App Secret, with a 15-day token. — [Webull Local MCP docs](https://developer.webull.com/apis/docs/AI-friendly-Resources/local-mcp/)
- Options: $0 commission and $0 per-contract fee for standard equity options, per a third party. — [stockbrokers.com tastytrade vs Webull](https://www.stockbrokers.com/compare/tastytrade-vs-webull)
- Official MCP: local and cloud; see section 3.

**E*TRADE (Morgan Stanley)**
- Authentication: **OAuth 1.0a**, HMAC-SHA1 only, three-legged with a browser verifier code.
  - Tokens expire at **midnight US Eastern** and go inactive after **2 hours** without a request. They are not refreshable; the user must re-authorize.
  - Production access needs a signed Developer Agreement. Order placement also needs a User Intent Survey.
  - Sandbox and production hosts are separate (`api.etrade.com/v1`).
  - — [E*TRADE Developer Guides](https://developer.etrade.com/getting-started/developer-guides); [api-evangelist/etrade](https://github.com/api-evangelist/etrade); [Sean Soper blog](https://seansoper.com/blog/connecting-etrade/)
- Options: $0.65/contract ($0.50 at 30+ trades per quarter), per a third party. — [QuantWheel](https://quantwheel.com/marketplace/brokers/e-trade-vs-tastytrade)
- Official MCP: none found.

**tastytrade**
- Authentication: OAuth2 is required for all API users. The legacy `POST /sessions` login was decommissioned on 11 Feb 2026.
  - The sandbox (`api.cert.tastyworks.com`) is separate from production (`api.tastyworks.com`).
  - A community package says the client must be created with read and trade scopes; I did not verify this.
  - — [tastytrade OAuth2 docs](https://developer.tastytrade.com/docs/authentication/oauth2/); [tastytrade-mcp](https://github.com/tastytrade/tastytrade-mcp); [PyPI tastytrade-mcp](https://pypi.org/project/tastytrade-mcp/)
- Options: $1.00/contract to open, $0 to close, $10 cap per leg, per a third party. — [stockbrokers.com](https://www.stockbrokers.com/compare/tastytrade-vs-webull)
- Official MCP: self-hosted with a dry-run gate; see section 3.

**Summary matrix** (✓ = confirmed in the sources above; "?" = not verified in this session)

| Broker | Official retail API auth | Paper/sandbox | Streaming | Official MCP (Oct 2026) | Minimum |
|---|---|---|---|---|---|
| Alpaca | API key/secret | ✓ free paper | ✓ WebSocket (market data and news) | ✓ self-hosted, paper default | $0 individual |
| IBKR | OAuth 2.0 (Web API); TWS socket | ✓ paper account | ✓ (subscriptions needed) | ✓ hosted, draft-only (third-party reports) | $500 + data costs for API data |
| Schwab | OAuth, 7-day refresh | ✗ no sandbox (third-party) | ✓ Streamer WebSocket | ✗ community only | $0 (third-party) |
| Tradier | Bearer token | ✓ sandbox, 15-min delayed | ✓ live only | ✓ hosted | ? |
| Public | Personal access token | ? | ? | ✓ hosted and self-run | ? |
| Webull | App Key/Secret | ✓ sandbox | ? | ✓ local and cloud (OAuth) | ? |
| E*TRADE | OAuth 1.0a, daily expiry | ✓ sandbox host | ? | ✗ | ? |
| tastytrade | OAuth2 (since Feb 2026) | ✓ cert sandbox | ? | ✓ self-hosted, dry-run gate | ? |

### Inferences
- For a breakout or news-driven bot, Alpaca uniquely bundles brokerage, paper trading and a real-time news WebSocket under one key pair. IBKR offers broader markets but needs Pro plus data subscriptions.
- Schwab's 7-day and E*TRADE's daily re-authorization requirements make fully unattended bots awkward. Robinhood's OAuth MCP may have similar session-renewal issues, which I could not verify.

### Gaps
- I did not verify IBKR commission figures, the Webull, Public, tastytrade and E*TRADE streaming details, or account minimums for Tradier, Public, Webull, E*TRADE and tastytrade.
- tastytrade's site has a page titled "THE PDT RULE IS GONE" ([tastytrade.com/pdt](https://tastytrade.com/pdt)). That suggests a 2026 change to pattern-day-trader rules relevant to small-account breakout traders, but I did not research it.
- I found no official Schwab statement on current API approval times.

## 5. What a realistic Robinhood "connector" looks like today (October 2026)

### Takeaway
There are four realistic sanctioned options:
1. **AI-assistant connector:** the official Robinhood Trading MCP (OAuth) against a separately funded Agentic Account. It covers equities, at least single-leg options, and crypto since about 17 Aug 2026. The connector should add its own confirmation step, because external-agent approvals default to off.
2. **Custom crypto bot:** the official Crypto Trading API (API key and Ed25519, 100 requests per minute).
3. **Main-account equities:** alerts plus manual execution in the Robinhood app or Legend.
4. **Fully programmatic equities or news strategies:** a broker with a mature API, such as Alpaca, ideally paper-trading first.

Unofficial private-API scraping of the main account is technically possible but carries ToS, lockout and security risk.

### Cited Findings
- The Trading MCP gives trade authority only over the Agentic Account and only with deposited funds, but it gives read access to all accounts. — [Robinhood support: Onboarding an external agent](https://robinhood.com/us/en/support/articles/onboarding-an-external-agent/); [Robinhood newsroom](https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/)
- External MCP approvals are off by default and still rolling out. — [Robinhood support: Trading with your agent](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)
- Agent crypto has restrictions: no transfers, staking or lending, and it is unavailable in some states including NY. — [Vorp Labs, 2026-10-07](https://vorplabs.com/agent-tools/robinhood-cli)
- Reported product limits:
  - No short selling, leverage or money movement; single-leg options only. — [Farao](https://getfarao.com/blog/robinhood-agentic-trading-review)
  - Spreads unsupported as of July 2026. — [NexusTrade, 2026-07-08](https://nexustrade.io/blog/robinhood-agentic-trading-mcp-review-20260708)
- Extended-hours constraints from the Customer Agreement (revised 1 Oct 2026) and support pages:
  - Fractional-share or dollar-amount orders are not executable in the After-Hours session.
  - Market orders are not supported during extended hours.
  - — [Robinhood Customer Agreement](https://cdn.robinhood.com/assets/robinhood/legal/Robinhood-Customer-Agreement.pdf); [Robinhood support: market order](https://robinhood.com/us/en/support/articles/market-order-update/?hcs=true); [Robinhood support: extended-hours trading](https://robinhood.com/us/en/support/articles/extendedhours-trading/)
- Liability for agent trades sits with the user, and Robinhood does not audit agents. — [Robinhood newsroom](https://robinhood.com/newsroom/robinhood-is-now-open-to-agents/); [CoinDesk, 2026-09-30](https://www.coindesk.com/markets/2026/09/30/robinhood-is-giving-customers-an-ai-agent-that-trades-for-them-plus-10x-crypto-bets)
- The Crypto API has a 100 requests/min (300 burst) limit, enough for polling-based crypto breakout logic but not tick-level streaming. — [docs.robinhood.com](https://docs.robinhood.com/)
- Robinhood's Legend platform has a native scanner with 50+ filters (February 2026). It can serve as the "alert" side of an alerts-plus-manual workflow. — [Robinhood on X](https://x.com/RobinhoodApp/status/2019802681326354842)

### Inferences
- A practical architecture for a breakout or news app targeting Robinhood users, as of October 2026:
  - Market and news data from a third-party feed, for example Alpaca's Benzinga news WebSocket.
  - Signal generation in the app.
  - Execution through the Robinhood Trading MCP into a small, capped Agentic Account. Robinhood's approvals should be enabled, or the app should enforce its own approval, and use limit orders only.
  - Crypto strategies can instead use the Crypto Trading API directly.
  - The main brokerage account stays read-only through the MCP, or fully manual.
- Robinhood offers no streaming market-data API to retail developers that I could find. A news or breakout app will need an external data source regardless.
- Agent and MCP capabilities changed month to month through 2026, so a production connector should discover its tools at runtime rather than hard-code them.

### Gaps
- The MCP's actual order types, rate limits, session or token lifetime, and any rules on non-LLM automated clients are unverified; Robinhood's docs and support hosts were blocked.
- I found no confirmation of a Robinhood market-data streaming API or webhooks for retail developers.

## 6. Added constraint: $100 account, no day trading (swing holds overnight or longer), no share-price limit. Fractional and notional orders, minimum order sizes, small-account fees, and Robinhood Crypto API minimums and fees

User clarification (received 2026-10-30): there is no minimum or maximum share price. Any stock is eligible because fractional or dollar-amount orders let a $100 account buy expensive stocks. **Fractional and notional order support through each broker's API is therefore a primary comparison point.** The only constraints are the $100 starting balance and no day trading.

### Takeaway (fractional and notional via API, ranked by how well confirmed it is in official sources)
1. **Confirmed in official API docs:**
   - **Alpaca:** `notional` or fractional `qty`, $1 minimum; fractional orders are DAY-only.
   - **Webull OpenAPI:** cash-amount `entrust_type`, $5 minimum, MARKET orders only.
   - **Public:** `amount` field.
   - **tastytrade:** "Notional Market" order type; third-party integrators say automation support is partial.
   - **IBKR:** `cashQty`, with fractional trading enabled in account settings; an older forum post conflicts.
2. **Unconfirmed or conflicting:**
   - **Robinhood Trading MCP:** the `place_equity_order` schema was not found; third-party claims conflict.
   - **Tradier:** SnapTrade claims fractional support; nothing official.
3. **Probably not supported via API:**
   - **E*TRADE:** API "DOLLAR" quantity type noted as unavailable by a community client.
   - **Schwab Trader API:** no source either way; Stock Slices is an app feature that bars limit orders.

Other points (unchanged):
A $100 swing account is workable at Robinhood, Alpaca, IBKR Lite, E*TRADE and tastytrade, which all report $0 minimums and no inactivity fees.

Watch-outs:
- **Tradier** charges $50/year inactivity for accounts under $2,000 with fewer than 2 trades a year.
- **Public** reportedly needs a $20 minimum deposit and charges $3.99/month inactivity on accounts under $70 after 6 months.
- **IBKR's API market data** needs IBKR Pro plus $500 in the account, which is out of reach at $100.

Fractional and dollar-amount ("notional") orders are supported via API at:
- **Robinhood** (app: $1 minimum; via MCP: conflicting reports).
- **Alpaca** ($1 minimum).
- **IBKR** (`cashQty`, with fractional trading enabled).
- **Webull** ($5 minimum, market orders only).
- **Public** (`amount` field).

Many brokers restrict fractional orders to market-only or DAY-only. A swing trader may therefore be unable to keep a resting overnight stop on a fractional position through the API.

Robinhood Crypto charges no commission on default market-maker routing; the cost sits in the spread. Exchange-routed (fee-tier) orders pay 0.95% taker or 0.50% maker at the lowest-volume tier. Minimum sizes are per trading pair and should be read from the API's `trading_pairs` endpoint.

### Cited Findings

**Pattern-day-trader context (dated)**
- The SEC approved FINRA Rule 4210 amendments on 14 Apr 2026. FINRA Regulatory Notice 26-10 (20 Apr 2026) set **4 Jun 2026** as the effective date.
  - The $25,000 minimum equity and the pattern-day-trader designation are removed and replaced by intraday-margin-based restrictions.
  - Firms may phase in until **20 Oct 2027**.
  - Schwab said it would stop counting day trades from 8 Jun 2026.
  - — [ACA Global](https://www.acaglobal.com/industry-insights/finra-ends-the-pattern-day-trader-rule/); [FINRA weekly archive, 2026-04-22](https://www.finra.org/compliance-tools/weekly-archive/04222026); [Schwab Advisor Services](https://advisorservices.schwab.com/story/introduction-to-pattern-day-trader-rules); [tastytrade: "THE PDT RULE IS GONE"](https://tastytrade.com/pdt)
  - Under the user's no-day-trading constraint, the PDT rule is moot. It matters only if the strategy changes.

**Robinhood: equities (app and brokerage)**
- Fractional shares can be traded in real time when valued at **$1 or more**. Orders can be placed in dollar amounts or share amounts; Robinhood's example is $10 becoming 0.1 shares.
  - Fractional orders are generally handled on a "Not Held" basis.
  - Fractional shares **cannot be transferred out**.
  - — [Robinhood support: Fractional shares](https://robinhood.com/us/en/support/articles/fractional-shares), via search snippet, Oct 2026; [BrokerChooser](https://brokerchooser.com/invest-long-term/diversification/fractional-shares-robinhood)
- Extended hours: fractional or dollar-amount orders are not executable in the After-Hours session (Customer Agreement, revised 1 Oct 2026), and market orders are not supported in extended hours. — [Robinhood Customer Agreement](https://cdn.robinhood.com/assets/robinhood/legal/Robinhood-Customer-Agreement.pdf); [Robinhood support: market order](https://robinhood.com/us/en/support/articles/market-order-update/?hcs=true)
- Robinhood Gold is $5/month. A third party says Cortex requires it; it is not needed for API or MCP access per any source found. — [Tapeboard](https://tapeboard.com/blog/robinhood-legend-gaps)

**Robinhood: Agentic Account via the Trading MCP**
- Funding: the user funds the account "with an amount you choose" from a bank, another Robinhood account or an asset transfer, and can skip funding at setup. **No minimum is stated** on Robinhood's setup page. — [Robinhood support: Setting up an agent](https://robinhood.com/us/en/support/articles/setting-up-an-agent/), via search snippet, Oct 2026
  - A Finder page lists a $0 minimum, but it is marked as paid promotion. — [Finder](https://www.finder.com/stock-trading/robinhood-agentic-accounts)
- Robinhood allows **only one margin account per customer**. If the main account uses margin, the Agentic account will be a cash account. Instant Deposit limits are shared across self-directed accounts. — [Walnut help, Oct 2026](https://walnutinvest.com/help/robinhood-agentic-account), a third-party app that uses Robinhood's agent trading
- The official server's order tool is reportedly `place_equity_order`, which places a real order with Agentic-account funds. — [PolicyLayer tool listing](https://policylayer.com/tools/robinhood-agentic-trading.md)
- Fractional and dollar orders through the MCP: **conflicting third-party reports.**
  - A community Robinhood agent server says fractional shares are supported for opening or adding to a long buy.
  - Another guide says "whole shares only", adding that fractional shares break stop-loss placement on some Robinhood account types.
  - A help page lists market orders "by shares or by dollars", limit, stop limit and stop market.
  - — [kevin1chun/robinhood-for-agents](https://github.com/kevin1chun/robinhood-for-agents); [Walnut help](https://walnutinvest.com/help/robinhood-agentic-account); [HackerNoon guide](https://hackernoon.com/how-to-build-an-autonomous-ai-trading-agent-on-robinhood). The search summary did not pin each claim to a single URL; treat as unverified.
- No public parameter schema was found for `place_equity_order`, so dollar-amount fields and time-in-force values are unknown. The PolicyLayer listing rates it a critical-risk financial action. — [PolicyLayer](https://policylayer.com/tools/robinhood-agentic-trading.md), searched 2026-10-30. The definitive check is to call MCP `tools/list` against `https://agent.robinhood.com/mcp/trading` after OAuth and read the input schema; I did not do this.

**Robinhood Crypto Trading API: minimums, fees and spreads**
- Official Robinhood Crypto fee schedule (PDF; the filename suggests 22 Jun 2026):
  - Exchange-routed crypto orders use nine 30-day-volume tiers, from **0.95% taker / 0.50% maker at $0–$10K** down to **0.03% taker / 0.00% maker at $25M+**.
  - The tier is locked when the order is placed.
  - Default routing to market makers carries **no commission**; the cost is built into the spread.
  - — [Robinhood Crypto fee schedule](https://cdn.robinhood.com/assets/robinhood/legal/rhc-fee-schedule.pdf)
- A third party estimates the spread cost at about **$0.95 per $100** traded. — [BeginnerBull, 2026](https://beginnerbull.com/robinhood-fees-explained/) / [BloFin academy](https://blofin.com/en/academy/education/robinhood/robinhood-crypto-fees-explained); third-party estimate
- A CryptoSlate review lists different Smart Exchange Routing rates (0.85%–0.10%), which conflict with the official PDF; the PDF takes precedence. — [CryptoSlate](https://cryptoslate.com/crypto-exchanges/robinhood-exchange-review/)
- API v2 and fee tiers:
  - Only v2 orders count toward fee-tier volume. — [Robinhood support: Crypto Trading API](https://robinhood.com/us/en/support/articles/crypto-api)
  - v2 orders are charged the **taker** rate until maker/taker pricing is fully available. — [BloFin](https://blofin.com/en/academy/education/robinhood/robinhood-crypto-fees-explained)
  - Maker/taker fees were still "rolling out gradually" and may not be available to every customer as of **19 Oct 2026**. — [Swan Bitcoin](https://www.swanbitcoin.com/industry/robinhood-fees/)
- Minimum order size: per a third party, **$0.01 on market-maker routing and $0.03 on exchange routing**. — [BloFin](https://blofin.com/en/academy/education/robinhood/robinhood-crypto-fees-explained). A "$1/€1" minimum in another review appears to be a different product or region. — [CryptoSlate](https://cryptoslate.com/crypto-exchanges/robinhood-exchange-review/)
- Per-pair limits come from `GET /api/v1/crypto/trading/trading_pairs/`, with fields `min_order_size`, `max_order_size`, `asset_increment` and `quote_increment`. — [apis.io OpenAPI profile](https://apis.io/apis/robinhood/robinhood-trading-pairs-api/); [robinrust source](https://docs.rs/crate/robinrust/1.0.3/source/src/trading.rs)
  - The keel project reports that `max_order_size` varies by asset (for example 20 BTC, 6,500,000 DOGE). It also reports a `min_order_amount` field, in quote currency, present on 63 of 89 pairs; the size fields are in the base asset. — [keel issue #410](https://github.com/CodeGateSoftware/keel/issues/410); [keel PR #418](https://github.com/CodeGateSoftware/keel/pull/418). These are third-party; field names may differ from the official docs.

**Alpaca**
- Fractional and notional orders:
  - **Minimum $1 notional for entry orders.** Since 24 Nov 2022, quantity-based fractional orders worth under $1 are rejected.
  - `notional` and `qty` are mutually exclusive, with up to 9 decimal places.
  - — [Alpaca support](https://alpaca.markets/support/can-we-submit-orders-smaller-than-1-usd-in-notional-value); [Alpaca docs: Fractional Trading](https://docs.alpaca.markets/us/docs/fractional-trading); [QuantConnect forum](https://www.quantconnect.com/forum/discussion/18853/fractional-shares-with-alpaca-brokerage-model/)
- Fractional orders support market, limit, stop and stop-limit, but **only with time-in-force = DAY**. Fractional positions are long-only. — [Alpaca docs: Fractional Trading](https://docs.alpaca.markets/us/docs/fractional-trading); [Alpaca blog: fractional limit orders and extended hours](https://alpaca.markets/blog/fractional-shares-trading-supports-limit-orders-and-extended-hours/)
- Fees: no commission on US-listed securities for self-directed accounts, though SEC/FINRA fees may apply. Fractional fees work the same as whole shares. — [Alpaca support: what is fractional trading](https://alpaca.markets/support/what-is-fractional-trading)
- Minimum and data:
  - **No minimum deposit** for individual accounts. — [Alpaca support](https://alpaca.markets/support/alpaca-minimum-deposit)
  - The **free Basic data plan** is the default for paper and live: real-time IEX only, **30 WebSocket symbols**. Algo Trader Plus ($99/month) adds all exchanges and unlimited symbols. — [Alpaca docs: About Market Data API](https://docs.alpaca.markets/docs/about-market-data-api)

**Interactive Brokers**
- IBKR Lite has no account minimums or inactivity fees. A 2026 review lists $0 minimum and $0 inactivity for Lite and Pro. — [IBKR Lite page](https://www.interactivebrokers.com/en/trading/why-ibkr-lite.php); [NerdWallet 2026](https://www.nerdwallet.com/investing/reviews/interactive-brokers)
  - A 2024 Benzinga piece said Pro needed $100 to start, which may be outdated. — [Benzinga](https://www.benzinga.com/money/interactive-brokers-pricing)
- The commissions page lists "No minimums per order" and "No inactivity fees" for US stocks and ETFs. Fractional trades follow the plan's normal schedule. A per-order minimum of $1.00 (Pro) or $0.35 (Lite) appears in jumbled text; verify it. — [IBKR Commissions](https://www.interactivebrokers.com/commissions)
- Dollar orders through the API:
  - The Web API's `cashQty` sets an order's monetary value instead of share count.
  - Without fractional trading enabled (Client Portal → Account Settings), cash-value orders round down to whole shares.
  - — [IBKR Campus (Web API)](https://www.interactivebrokers.com/campus/ibkr-quant-news/how-to-code-a-currency-conversion-order-in-the-web-api/); [IBKR TWS release notes](https://interactivebrokers.com/en/general/tws_notes_979.php); [IBKR fractional share orders](https://interactivebrokers.ca/en/trading/orders/fractional-share-orders.php)
  - Conflict: an older QuantConnect forum post (date not visible) quotes "Fractional trading is not supported via IBKR API or FIX/CTCI at this time." — [QuantConnect forum](https://www.quantconnect.com/forum/discussion/11770/buying-fractional-shares/). The IBKR-hosted notes above on `cashQty` and fractional settings are more authoritative but may be newer; confirm with a paper-account test.
- **API market data needs IBKR Pro (not Lite) and $500 in the account plus the subscription cost**, so a $100 account would need an external data feed. — [IBKR Campus: market data subscriptions](https://www.interactivebrokers.com/campus/ibkr-api-page/market-data-subscriptions/)

**Charles Schwab**
- Schwab's fractional product, Stock Slices, treats each slice as a separate order and does **not allow limit or conditional orders**. — [Schwab Stock Slices T&Cs](https://www.schwab.com/public/file/P-12533231)
- Stock Slices truncates fractional holdings to four decimal places. — [Schwab Stock Slices T&Cs](https://www.schwab.com/public/file/P-12533231)
- A targeted search on 2026-10-30 found no source on whether the Trader API supports fractional or notional orders. Treat it as unsupported until shown otherwise. — see Gaps
- No account minimum, per a third party. — [QuantWheel](https://quantwheel.com/marketplace/brokers/schwab-vs-tastytrade)

**Tradier**
- Inactivity fee: **$50/year for accounts under $2,000 with fewer than 2 trades a year** (official pricing page). — [Tradier pricing](https://tradier.com/individuals/pricing); corroborated by [BrokerChooser](https://brokerchooser.com/invest-long-term/costs/inactivity-fee-tradier)
- Fractional shares: conflicting. BrokerChooser says supported; Bankrate says only through some third-party platforms. — [BrokerChooser](https://brokerchooser.com/broker-reviews/tradier-review/tradier-stocks); [Bankrate](https://www.bankrate.com/investing/brokerage-reviews/tradier)
  - The integrator SnapTrade lists "fractional trading in shares" for its Tradier integration. — [SnapTrade: Tradier API](https://snaptrade.com/brokerage-integrations/tradier-api)
  - A community MCP server sends a float `quantity` to Tradier's orders endpoint. That shows the code path, not that fills occur. — [glama: ReadyTrader tradier_service.py](https://glama.ai/mcp/servers/@up2itnow/ReadyTrader-Stocks/blob/dad47997bbc257b0c14f958b186af6186cfa5ed7/execution/tradier_service.py)
  - QuantConnect's Tradier docs do not mention fractional quantities. — [QuantConnect: Tradier](https://www.quantconnect.com/docs/v2/cloud-platform/live-trading/brokerages/tradier)
  - I found no dollar-amount (notional) order parameter for Tradier.
- API access cost: free (docs) versus a $10/month tier (third-party review); see section 4.

**Public.com**
- The stock/ETF order endpoint takes **`quantity` or `amount` (not both)**. Quantity is used for whole shares and for selling fractional positions. — [Public API: Place order](https://public.com/api/docs/resources/order-placement/place-order)
- Fractional minimum: conflicting. NerdWallet says $5 (and $100 for bonds). Public's disclosure says it won't accept fractional orders under $1.00, possibly in the investment-plan context. — [NerdWallet](https://www.nerdwallet.com/investing/best/best-brokers-for-fractional-shares); [Public fractional disclosure](https://public.com/disclosures/public-fractional-shares-disclosure)
- Account fees: **$20 minimum deposit** and a **$3.99/month inactivity fee for accounts under $70 after 6 months of inactivity**, per a third party. — [BrokerChooser: Public inactivity fee](https://brokerchooser.com/invest-long-term/costs/inactivity-fee-publiccom); [BrokerChooser: Public vs E*TRADE](https://brokerchooser.com/compare/publiccom-vs-e-trade)
- Crypto fees (reviews): flat fees from $0.49 (orders under $10) to about $6.29–$6.49 (orders of $250–$500), and 1.25% above $500. API trades use the same schedule as the app. — [Finder](https://www.finder.com/stock-trading/public-review); [StockBrokers.com](https://www.stockbrokers.com/review/public-com)
  - New "API crypto fee tiers" by monthly volume took effect 16 Jun 2026 and may supersede this. — [Public API changelog](https://public.com/api/docs/changelog)

**Webull OpenAPI**
- The `entrust_type` parameter accepts a quantity (fractional decimals allowed) or a cash amount.
  - **Only MARKET orders are supported for fractional trading.**
  - The fractional quantity must be greater than 0 and at most 1.
  - **The order value must be at least $5.**
  - — [Webull developer docs: Stock Trading](https://developer.webull.com/apis/docs/trade-api/stock/)
- SnapTrade's notes (January 2026) agree on the $5 minimum and say Webull now requires extra OTC and fractional-trading agreements. — [SnapTrade Webull notes](https://support.snaptrade.com/Webull-e1afeaa69a1c839ba37c0134f951baa2?pvs=21)
- Fees:
  - No extra fee for trading via OpenAPI; trading fees match the app. — [Webull HK developer FAQ](https://developer.webull.hk/apis/docs/faq)
  - **OpenAPI market data is a separate subscription**; app and desktop subscriptions do not carry over. — [Webull Market Data API overview](https://developer.webull.com/apis/docs/market-data-api/overview/)
  - A regional page offers Nasdaq Basic free. — [Webull AU subscribe quotes](https://developer.webull.com.au/apis/docs/market-data-api/subscribe-quotes); US pricing not confirmed

**E*TRADE**
- Fractional: conflicting. One source says DRIP only, with no direct fractional purchases. A 2026 source says fractional trading is now offered for some stocks and ETFs, with market-only orders for sub-one-share quantities. — [Brokerage-Review](https://www.brokerage-review.com/invest/partial/etrade-fractional-shares.aspx); [InvestingInTheWeb, 2026](https://investingintheweb.com/brokers/etrade-fractional-shares/). No API-specific source.
- E*TRADE API dollar orders:
  - A community R client for the E*TRADE API lists quantity types QUANTITY, DOLLAR and ALL_I_OWN, but notes "DOLLAR is not yet an option". — [etrader R package](https://search.r-project.org/CRAN/refmans/etrader/html/etrd_place_optn_order.html)
  - Chilkat sample preview orders use `QUANTITY` only. — [Chilkat E*TRADE preview order example](https://example-code.com/objc/etrade_v1_preview_order.asp)
  - A review says E*TRADE's software "does not accept a whole-dollar amount" for fractional orders, with the capability planned. — [Brokerage-Review](https://www.brokerage-review.com/invest/partial/etrade-fractional-shares.aspx), undated
  - Net: no evidence of notional orders via the E*TRADE API.
- **$0 minimum deposit and no inactivity fee**, per a third party. An older $40/quarter inactivity fee appears outdated. — [BrokerChooser: E*TRADE fees](https://brokerchooser.com/broker-reviews/e-trade-review/e-trade-fees); [Kiplinger (old)](https://www.kiplinger.com/article/taxes/t055-c000-s002-broker-fee-fiasco.html)

**tastytrade**
- **No account minimum and no inactivity fee** (2026 review); exchange, clearing and regulatory fees still apply. — [InvestorMint](https://investormint.com/investing/brokers/tastyworks-review)
- Fractional shares: **$5 minimum**, per a third party. — [BrokerChooser](https://brokerchooser.com/invest-long-term/diversification/fractional-shares-tastytrade)
- The official Open API orders schema includes a **"Notional Market"** order type (alongside Limit, Market, Marketable Limit, Stop and Stop Limit).
  - A dollar-value field is required for it, and `quantity` is required for every order type except notional market.
  - A value-effect field marks debit or credit.
  - The docs navigation lists a "Fractional Stock Orders" guide, but its content was not retrieved.
  - — [tastytrade Open API spec: orders](https://developer.tastytrade.com/open-api-spec/orders/); [tastytrade guide: place an equity order](https://developer.tastytrade.com/docs/guides/place-an-equity-order/); [api-evangelist schema copy](https://raw.githubusercontent.com/api-evangelist/tastytrade/refs/heads/main/json-schema/orders-postAccountsAccountNumberOrders.json)
  - "Notional Market" implies dollar-based orders are market-only, so no notional limit or stop orders. This is inferred from the order-type list, not stated.
- TradersPost says fractional quantities are "not fully supported for automated trading on tastytrade stocks", but fractional crypto is fully supported. — [TradersPost docs: tastytrade](https://docs.traderspost.io/docs/all-supported-connections/tastytrade)

**$100 swing-account summary** ("?" = not verified this session)

| Broker | Fractional/notional via API | Min order | Account min | Small-account fees to watch |
|---|---|---|---|---|
| Robinhood (MCP Agentic acct) | Unconfirmed: `place_equity_order` schema not found; conflicting third-party claims | $1 (app fractional) | None stated | None found; crypto spread / 0.95% taker at lowest tier |
| Robinhood Crypto API | Yes (quote or asset amounts per pair) | Per pair (`trading_pairs`); ~$0.01–$0.03 per third party | Active RH Crypto acct | Spread (default) or fee tiers (v2) |
| Alpaca | **Yes (official docs)**: `notional` or fractional `qty`; market/limit/stop/stop-limit, DAY only | $1 | $0 | Free IEX data (30 symbols); SEC/FINRA fees |
| IBKR | Yes, `cashQty` with fractional enabled (an older forum post conflicts) | Unclear | $0 (Lite) | API data needs Pro + $500 |
| Schwab | No evidence (Stock Slices is app-only; no limit orders) | ? | $0 | ? |
| Tradier | Fractional qty claimed by SnapTrade only; no notional field found | ? | ? | **$50/yr inactivity** (<$2k, <2 trades/yr) |
| Public | **Yes (official docs)**: `amount` or `quantity` | $1–$5 (conflicting) | $20 (third party) | **$3.99/mo inactivity** (<$70, 6 months) |
| Webull | **Yes (official docs)**: cash amount; MARKET only | $5 | ? | Separate OpenAPI data subscription |
| E*TRADE | No: API "DOLLAR" qty type "not yet an option" (community client) | ? | $0 | None (third party) |
| tastytrade | **Yes (official spec)**: "Notional Market" order type; automation support partial per TradersPost | $5 (third party) | $0 | Exchange/clearing fees |

### Inferences
- With only $100, a non-fractional broker or API path restricts the universe to stocks priced under about $100, and position sizing becomes lumpy. Notional orders (Alpaca, Robinhood app, Public, IBKR `cashQty`, Webull) matter far more than commissions here.
- Swing-holding fractional positions overnight collides with order restrictions:
  - Alpaca fractional orders are DAY-only, so a protective stop would need resubmitting each session.
  - Webull fractional orders are market-only, so no resting stop is possible.
  - Schwab Stock Slices bar limit and conditional orders.
  - A swing app should either buy whole shares where stops matter, or implement software-side stop monitoring and plan for overnight gap risk.
- Fixed fees hurt a $100 account most:
  - Tradier's $50/year inactivity fee is 50% of capital per year for a low-activity account.
  - Public's $3.99/month inactivity fee is about 48% a year if the balance falls below $70 and goes inactive.
  - Paid data feeds such as Alpaca's $99/month Algo Trader Plus are clearly uneconomic. Free feeds (Alpaca Basic/IEX, Webull Nasdaq Basic) are the realistic choice.
- For Robinhood crypto via API, a $100 account sits in the lowest volume tier. Exchange-routed v2 orders at 0.95% taker cost about the same as the estimated default spread (around $0.95 per $100), so routing choice changes little at this size.
- IBKR is cheap to hold (no minimum, no inactivity fee) but impractical for API-driven data at $100 because of the $500 balance requirement for API market data.

### Gaps
- I could not confirm from official docs whether the Robinhood Trading MCP accepts dollar-amount or fractional orders, or which time-in-force values (GTC) it supports for overnight holds.
- I could not get official Robinhood Crypto API minimum order sizes per pair or the exact v2 fee-tier API parameters; docs.robinhood.com was blocked.
- Schwab Trader API fractional/notional support, IBKR minimum `cashQty` order size, Tradier's official fractional support, E*TRADE API fractional support, and Webull's US account minimum were all unverified.
- I did not research cash-account settlement constraints (T+1 good-faith or free-riding violations), which matter for a $100 cash account that rotates capital between swing trades.
