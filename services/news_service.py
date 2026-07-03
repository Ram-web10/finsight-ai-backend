import requests
from typing import List, Dict

# Free News API (you can replace later with NewsAPI key)
NEWS_API_URL = "https://newsapi.org/v2/everything"
API_KEY = "YOUR_NEWS_API_KEY"  # optional for now


def fetch_news(query: str) -> List[Dict]:
    """
    Fetch latest financial news for a stock/company.
    """

    # If no API key, fallback mock mode
    if API_KEY == "YOUR_NEWS_API_KEY":
        return [
            {
                "title": f"{query} shows strong quarterly performance",
                "description": "Company reports better than expected earnings growth.",
            },
            {
                "title": f"{query} faces market volatility concerns",
                "description": "Analysts warn about short-term pressure.",
            },
        ]

    params = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code != 200:
        return []

    articles = response.json().get("articles", [])

    return [
        {
            "title": a["title"],
            "description": a["description"]
        }
        for a in articles[:10]
    ]