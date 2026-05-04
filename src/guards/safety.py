from typing import Dict

# Define harmful categories with keywords
BLOCKLIST = {
    "insider_trading": [
        "inside information",
        "non public information",
        "insider tip"
    ],
    "market_manipulation": [
        "pump and dump",
        "manipulate stock",
        "artificially inflate"
    ],
    "money_laundering": [
        "launder money",
        "wash money",
        "hide illegal funds"
    ],
    "guaranteed_returns": [
        "guaranteed profit",
        "risk free returns",
        "no loss investment"
    ],
    "reckless_advice": [
        "all in",
        "100% leverage",
        "bet everything"
    ]
}


def check_safety(query: str) -> Dict:
    """
    Checks if the query is harmful based on keyword matching.
    Returns a dict with blocked status and message.
    """
    query_lower = query.lower()

    for category, keywords in BLOCKLIST.items():
        for keyword in keywords:
            if keyword in query_lower:
                return {
                    "blocked": True,
                    "category": category,
                    "message": get_block_message(category)
                }

    return {
        "blocked": False,
        "category": None,
        "message": None
    }


def get_block_message(category: str) -> str:
    """
    Returns a professional response for each blocked category.
    """
    messages = {
        "insider_trading": "I can't assist with using non-public or insider information for trading.",
        "market_manipulation": "I can't help with manipulating markets or misleading other investors.",
        "money_laundering": "I can't assist with hiding or laundering funds.",
        "guaranteed_returns": "There are no guaranteed returns in investing. I can help you understand risks instead.",
        "reckless_advice": "I can't support extremely high-risk strategies like betting everything or excessive leverage."
    }

    return messages.get(category, "I'm unable to assist with that request.")