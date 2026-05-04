from typing import Dict, Any
from src.agents.portfolio_health import analyze_portfolio


def route_request(classification: Dict, user_context: Dict) -> Dict[str, Any]:
    agent = classification.get("agent")

    # Portfolio Health Agent
    if agent == "portfolio_health":
        portfolio = user_context.get("portfolio", [])
        result = analyze_portfolio(portfolio)
        return {
            "agent": agent,
            "result": result,
            "classification": classification
        }

    # Stub for other agents
    return {
        "agent": agent,
        "result": {
            "message": f"{agent} is not implemented in this build."
        },
        "classification": classification
    }