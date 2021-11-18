# Strategy Development and Testing

As a user concerned with developing various strategies to deploy in the market, I should be able to set buy/sell triggers in a test portfolio, and back-test the strategy against historical data.

I should be able to specify a specific historical period for the test the strategy against the given period.

I should be able to test the strategy/portfolio against a set of time periods and compare the results.

I should be able to test multiple strategies against a given time-period, or against an identical set of time-periods and compare the results of each.

I would like an option to set the strategy and test portfolio to run in the background and track its performance using current and ongoing market data.

Strategies should have a field to enter notes and observations.

Portfolio and Strategy fields that should be included are:

- Cash, Shares Owned, Portfolio Value.

- Buy Triggers, the condition, the allotment of portfolio to invest.

- Sell Triggers, the condition, the allotment of shares owned to sell.

- Time period(s) to test, start-date, end-date, portfolio value on end-date.

- Multi-Period performance: number of random periods to test, length of period to test. points to plot, ie: total portfolio value, %change, shares owned, shares sold, etc.
