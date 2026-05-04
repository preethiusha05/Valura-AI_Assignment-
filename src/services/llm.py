from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# If key exists → use real OpenAI
if api_key:
    client = OpenAI(api_key=api_key)

    def call_llm(prompt: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content

# If key missing → mock (VERY IMPORTANT for tests)
else:
    def call_llm(prompt: str) -> str:
        # simple mock response
        return """
        {
            "intent": "portfolio_health",
            "agent": "portfolio_health",
            "entities": {}
        }
        """