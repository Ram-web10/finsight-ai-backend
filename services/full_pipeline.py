from services.pdf_reader import extract_text
from services.page_locator import locate_financial_pages
from services.table_extractor import extract_tables
from services.financial_parser import (
    extract_financial_data,
    extract_financial_data_from_tables
)
from services.field_mapper import map_fields
from services.ratio_calculator import calculate_ratios
from services.financial_scorer import calculate_financial_score
from services.trend_analyzer import analyze_trends
from services.red_flag_detector import detect_red_flags
from services.swot_generator import generate_swot
from services.chart_generator import generate_charts
from services.report_generator import generate_report
from services.investment_engine import generate_investment_recommendation

from services.news_service import fetch_news
from services.sentiment_engine import aggregate_sentiment
from services.signal_engine import generate_signal


# ==========================================================
# MASTER AI PIPELINE
# ==========================================================

def analyze_full_report(pdf_path: str):

    # -----------------------------
    # 1. Extract PDF Text
    # -----------------------------
    text = extract_text(pdf_path)

    # -----------------------------
    # 2. Locate Important Pages
    # -----------------------------
    pages = locate_financial_pages(pdf_path)

    # -----------------------------
    # 3. Extract Tables
    # -----------------------------
    tables = []
    for page in pages.get("financial_pages", []):
        tables.extend(extract_tables(pdf_path, page["page"]))

    # -----------------------------
    # 4. Extract Financial Data
    # -----------------------------
    text_data = extract_financial_data(text)
    table_data = extract_financial_data_from_tables(tables)

    # Merge data
    financial_data = {**text_data, **table_data}

    # -----------------------------
    # 5. Map Fields
    # -----------------------------
    mapped_data = map_fields(financial_data)

    # -----------------------------
    # 6. Ratios
    # -----------------------------
    ratios = calculate_ratios(mapped_data)

    # -----------------------------
    # 7. Score
    # -----------------------------
    financial_score = calculate_financial_score(mapped_data, ratios)

    # -----------------------------
    # 8. Trends (placeholder if multi-year exists later)
    # -----------------------------
    trends = analyze_trends([
        mapped_data,
        mapped_data
    ])

    # -----------------------------
    # 9. Red Flags
    # -----------------------------
    red_flags = detect_red_flags(mapped_data, ratios)

    # -----------------------------
    # 10. Recommendation
    # -----------------------------
    recommendation = generate_investment_recommendation(
        mapped_data, ratios, financial_score
    )

    # -----------------------------
    # 11. SWOT
    # -----------------------------
    swot = generate_swot(
        mapped_data,
        ratios,
        financial_score,
        red_flags,
        recommendation
    )

    # -----------------------------
    # 12. Charts
    # -----------------------------
    charts = generate_charts(mapped_data, ratios)

    # -----------------------------
    # 13. AI News + Sentiment
    # -----------------------------
    company_name = mapped_data.get("Company", "Stock")

    news = fetch_news(company_name)
    sentiment = aggregate_sentiment(news)

    # -----------------------------
    # 14. AI SIGNAL ENGINE
    # -----------------------------
    signal = generate_signal(
        financial_score=financial_score,
        ratios=ratios,
        sentiment=sentiment,
        trends=trends
    )

    # -----------------------------
    # 15. REPORT GENERATION
    # -----------------------------
    report = generate_report({
        "company": mapped_data,
        "financial_data": mapped_data,
        "ratios": ratios,
        "financial_health": financial_score,
        "investment": recommendation,
        "red_flags": red_flags,
        "swot": swot,
        "ai_analysis": signal,
    })

    # -----------------------------
    # FINAL OUTPUT
    # -----------------------------
    return {
        "company": mapped_data,
        "financial_data": mapped_data,
        "ratios": ratios,
        "financial_score": financial_score,
        "trends": trends,
        "red_flags": red_flags,
        "recommendation": recommendation,
        "swot": swot,
        "charts": charts,
        "news": news,
        "sentiment": sentiment,
        "signal": signal,
        "report": report
    }