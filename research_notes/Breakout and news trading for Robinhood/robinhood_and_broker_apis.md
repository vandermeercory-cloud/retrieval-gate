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
