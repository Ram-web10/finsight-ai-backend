from textblob import TextBlob
from typing import List, Dict


def analyze_sentiment(text: str) -> Dict:
    """
    Returns sentiment score for a single text.
    """

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        sentiment = "POSITIVE"
    elif polarity < -0.2:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"

    return {
        "text": text,
        "polarity": round(polarity, 3),
        "sentiment": sentiment
    }


def aggregate_sentiment(news_list: List[Dict]) -> Dict:
    """
    Aggregate sentiment across multiple news articles.
    """

    results = []
    total = 0

    for news in news_list:
        combined_text = news.get("title", "") + " " + news.get("description", "")
        sentiment = analyze_sentiment(combined_text)

        total += sentiment["polarity"]
        results.append(sentiment)

    avg = total / len(news_list) if news_list else 0

    if avg > 0.2:
        overall = "POSITIVE"
    elif avg < -0.2:
        overall = "NEGATIVE"
    else:
        overall = "NEUTRAL"

    return {
        "overall_sentiment": overall,
        "average_score": round(avg, 3),
        "details": results
    }

import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')