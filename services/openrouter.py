import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-4.1-mini"


def generate_financial_analysis(financial_data: dict, ratios: dict):

    prompt = f"""
You are a Senior Equity Research Analyst.

Analyze the following company's financial data.

Financial Data:
{financial_data}

Financial Ratios:
{ratios}

Generate a professional report with the following sections.

1. Executive Summary

2. Financial Health

3. Profitability Analysis

4. Liquidity Analysis

5. Leverage Analysis

6. Strengths

7. Weaknesses

8. Risks

9. Opportunities

10. Investment Recommendation

11. Overall Score out of 10

Keep the report concise but professional.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:

        return f"OpenRouter Error: {str(e)}"