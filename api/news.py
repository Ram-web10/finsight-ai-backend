from fastapi import APIRouter
from services.news_service import fetch_news
from services.sentiment_engine import aggregate_sentiment

router = APIRouter()


@router.get("/news/{query}")
def get_news_sentiment(query: str):

    news = fetch_news(query)
    sentiment = aggregate_sentiment(news)

    return {
        "query": query,
        "news": news,
        "sentiment": sentiment
    }