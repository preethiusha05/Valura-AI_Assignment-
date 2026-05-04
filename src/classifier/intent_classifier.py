import json
from src.services.llm import call_llm
from src.models.schemas import ClassificationResult


def classify_intent(query: str, history: list = None) -> ClassificationResult:
    """
    Classifies user query into intent, agent, and extracts entities.
    """

    prompt = f"""
You are an AI classifier for a financial assistant.

Classify the user query into:
1. intent
2. agent
3. entities (tickers, amount, time_period if any)
4. safety_verdict (safe / risky)

Available agents:
- portfolio_health
- market_research
- investment_strategy
- financial_calculator
- support

Return ONLY valid JSON like:
{{
  "intent": "...",
  "agent": "...",
  "entities": {{}},
  "safety_verdict": "safe"
}}

User query:
{query}
"""

    try:
        response = call_llm(prompt)

        data = json.loads(response)

        return ClassificationResult(**data)

    except Exception:
        # fallback if LLM fails
        return ClassificationResult(
            intent="unknown",
            agent="support",
            entities={},
            safety_verdict="safe"
        )