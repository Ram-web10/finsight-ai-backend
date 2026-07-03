from typing import Dict


# ==========================================================
# AI BUY / SELL SIGNAL ENGINE
# ==========================================================

def generate_signal(
    financial_score: Dict,
    ratios: Dict,
    sentiment: Dict,
    trends: Dict,
    portfolio_item: Dict = None
) -> Dict:

    score = financial_score.get("score", 0)

    sentiment_score = sentiment.get("average_score", 0)
    sentiment_label = sentiment.get("overall_sentiment", "NEUTRAL")

    revenue_growth = trends.get("Revenue Growth %")
    profit_growth = trends.get("Profit Growth %")

    # ======================================================
    # SIGNAL SCORE CALCULATION
    # ======================================================

    signal_score = 0

    # Financial strength
    if score >= 80:
        signal_score += 40
    elif score >= 60:
        signal_score += 25
    elif score >= 40:
        signal_score += 10
    else:
        signal_score -= 20

    # Sentiment impact
    if sentiment_label == "POSITIVE":
        signal_score += 25
    elif sentiment_label == "NEGATIVE":
        signal_score -= 25

    signal_score += sentiment_score * 20  # amplify sentiment

    # Growth impact
    if revenue_growth and revenue_growth > 10:
        signal_score += 15

    if profit_growth and profit_growth > 10:
        signal_score += 15

    # Risk adjustment
    debt_equity = ratios.get("Debt to Equity")

    if debt_equity and debt_equity > 2:
        signal_score -= 20

    # ======================================================
    # FINAL SIGNAL DECISION
    # ======================================================

    if signal_score >= 60:
        signal = "BUY"
        confidence = min(95, 60 + signal_score)
    elif signal_score >= 30:
        signal = "HOLD"
        confidence = 60 + signal_score / 2
    else:
        signal = "SELL"
        confidence = max(40, 60 - abs(signal_score))

    return {
        "signal": signal,
        "confidence": round(confidence, 2),
        "signal_score": round(signal_score, 2),
        "reasoning": {
            "financial_score": score,
            "sentiment": sentiment_label,
            "sentiment_score": sentiment_score,
            "growth_revenue": revenue_growth,
            "growth_profit": profit_growth,
            "debt_to_equity": debt_equity
        }
    }