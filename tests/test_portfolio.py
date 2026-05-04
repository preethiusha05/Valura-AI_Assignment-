from src.agents.portfolio_health import analyze_portfolio

portfolio = [
    {"ticker": "NVDA", "value": 60000},
    {"ticker": "AAPL", "value": 20000},
    {"ticker": "TSLA", "value": 20000}
]

result = analyze_portfolio(portfolio)
print(result)