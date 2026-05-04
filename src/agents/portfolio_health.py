from typing import Dict, List


def analyze_portfolio(portfolio: List[Dict]) -> Dict:
    """
    portfolio = [
        {"ticker": "AAPL", "value": 5000},
        {"ticker": "NVDA", "value": 15000}
    ]
    """

    # Handle empty portfolio
    if not portfolio:
        return {
            "message": "You don’t have any investments yet. A good starting point is to diversify across stocks, ETFs, and bonds based on your risk level.",
            "disclaimer": "This is not investment advice."
        }

    total_value = sum(p["value"] for p in portfolio)

    # Sort by value (descending)
    sorted_portfolio = sorted(portfolio, key=lambda x: x["value"], reverse=True)

    top_position_pct = (sorted_portfolio[0]["value"] / total_value) * 100

    top_3_value = sum(p["value"] for p in sorted_portfolio[:3])
    top_3_positions_pct = (top_3_value / total_value) * 100

    # Risk flag
    if top_position_pct > 50:
        flag = "high"
    elif top_position_pct > 25:
        flag = "medium"
    else:
        flag = "low"

    # Dummy performance (you can improve later)
    total_return_pct = 10.0
    annualized_return_pct = 7.5

    # Benchmark (dummy for now)
    benchmark_return = 8.0
    alpha = total_return_pct - benchmark_return

    # Observations
    observations = []

    if flag == "high":
        observations.append({
            "severity": "warning",
            "text": f"{sorted_portfolio[0]['ticker']} makes up {round(top_position_pct,2)}% of your portfolio — very concentrated."
        })

    if alpha > 0:
        observations.append({
            "severity": "info",
            "text": f"You are outperforming the benchmark by {round(alpha,2)}%."
        })

    return {
        "concentration_risk": {
            "top_position_pct": round(top_position_pct, 2),
            "top_3_positions_pct": round(top_3_positions_pct, 2),
            "flag": flag
        },
        "performance": {
            "total_return_pct": total_return_pct,
            "annualized_return_pct": annualized_return_pct
        },
        "benchmark_comparison": {
            "benchmark": "S&P 500",
            "portfolio_return_pct": total_return_pct,
            "benchmark_return_pct": benchmark_return,
            "alpha_pct": round(alpha, 2)
        },
        "observations": observations,
        "disclaimer": "This is not investment advice."
    }