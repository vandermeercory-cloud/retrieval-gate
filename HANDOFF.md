# Handoff: Robinhood agentic trading assistant

I'm building a trading assistant for my Robinhood **Agentic Account**, using Robinhood's official Trading MCP connector (`https://agent.robinhood.com/mcp/trading`), which I've connected on claude.ai. Work on the `claude/trading-research` branch and commit there.

## Read first
- `reports/Breakout and news trading for Robinhood.md`: the research report and recommendation. Its last section is the plan.
- `research_notes/Breakout and news trading for Robinhood/`: the source notes (broker APIs, regulation and risk, news catalysts, breakout evidence, backtests).
- `research_code/breakout_backtests/`: backtest code and results. `engine.py` and `event_study.py` define the signals.

## Account constraints
- Starts with **$100**. Don't assume I'll add money.
- **No day trading.** Never sell a position in the same session it was bought.
- Any share price is fine; use fractional or dollar-amount orders if the connector supports them.
- Regular market hours only, with no extended-hours orders.

## Safety rules (non-negotiable)
1. **Never place, change or cancel an order without my explicit "yes" to that specific ticket in chat.** Show the ticket first: symbol, dollar amount, order type, limit price if any, time in force, signal date, catalyst tag and planned exit date.
2. Never ask me to "always allow" the order tool, and never call money-movement tools.
3. Hard limits, enforced as blocks rather than warnings:
   - $20 per position and at most 5 open positions.
   - At most 2 new orders a day and one order per symbol.
   - Duplicate-order check against open orders and positions.
   - Reject a fill price more than 3% from the last price.
4. **Kill switch:** if Agentic Account equity is at or below $80, stop proposing entries and tell me.
5. The connector can read all my Robinhood accounts. Only read the Agentic Account unless I ask otherwise, and don't copy account numbers into files or commits.

## Step 1: verify the connector (read-only, no orders)
- List the Robinhood MCP tools and read every order-related schema. Answer these:
  - Does it accept dollar-amount (notional) or fractional orders, and what's the minimum?
  - Which order types and time-in-force values does it support?
  - Does it support stop orders, including on fractional positions?
  - Is there a dry-run or preview mode?
- With read-only tools, show the Agentic Account's cash, buying power, positions and account type (cash or margin).
- Remind me to confirm that Robinhood's in-app trade approvals are on for external agents.
- Write the findings to `docs/connector_findings.md`. **If orders are whole-share only, stop and tell me**, because the $20-per-position plan doesn't work then.

## Step 2: build the nightly scanner and journal
- **Universe:** current S&P 500 stocks with at least $1M average daily dollar volume, fractional-eligible, and no share-price filter.
- **Signal D, the only tested signal with a residual edge:** day-t open at least 4% above the prior close, and day-t volume at least 3× the 50-day average. Scan after the close.
- **Hard exclusions:** "strategic alternatives" language, or an offering filing (S-3 or 424B) after the run-up.
- **Log as tags but don't use for decisions yet:** catalyst type (from headlines and EDGAR 8-K items), guidance raises, confirming analyst revisions, insider buys (Form 4).
- **Journal:** SQLite. Record every signal, traded or not, plus every proposal, my approve/reject decision and reason, fills, and slippage against that day's open.
- **Paper-track every signal** against SPY and an equal-weight basket of the universe over the same window.
- **Data:** Yahoo Finance daily bars. Its domains (`query1.finance.yahoo.com`, `query2.finance.yahoo.com`, `fc.yahoo.com`) are allowlisted in this environment. SEC EDGAR needs `www.sec.gov`, `efts.sec.gov` and `data.sec.gov` allowed in the environment's network settings, and a User-Agent with a contact email. Ask me which email to use; don't guess.

## Step 3: morning routine
- Read the journal and the Agentic Account state, then draft tickets for eligible signals.
- Wait for my approval of each ticket, then place approved orders during the first hour of the regular session.
- **Exits:** propose a sell at 60 trading days. Propose one earlier only after a downgrade to sell or an offering filing. No tight stops.

## Step 4: weekly report
Compare these with SPY and the equal-weight basket:
- Mean excess return of all signals, traded and not.
- Slippage.
- Approved versus rejected signals.
- The live account versus a $100 SPY shadow position.

## Rules for judging it
- The rules are frozen for 12 months, and any change counts as a new trial.
- **Retire the signal** if, after 12 months and at least 150 paper events, its mean excess return over the equal-weight basket is zero or negative.
- **Don't add money** until about 400 events show a t-statistic of at least 2.
- The fallback is a broad index fund.
