from typing import Dict, List


def generate_investment_recommendation(
    financial_score: Dict,
    red_flags: List[str],
    ratios: Dict
) -> Dict:
    """
    Generate a BUY / HOLD / SELL recommendation.
    """

    score = financial_score.get("financial_health_score", 0)

    recommendation = ""
    confidence = 0
    risk = ""
    horizon = ""
    reasons = []
    concerns = []

    # -----------------------------
    # Recommendation
    # -----------------------------

    if score >= 85:
        recommendation = "BUY"
        confidence = 95
        risk = "Low"
        horizon = "Long Term"

    elif score >= 70:
        recommendation = "BUY"
        confidence = 85
        risk = "Moderate"
        horizon = "Medium to Long Term"

    elif score >= 55:
        recommendation = "HOLD"
        confidence = 75
        risk = "Moderate"
        horizon = "Medium Term"

    elif score >= 40:
        recommendation = "HOLD"
        confidence = 60
        risk = "High"
        horizon = "Short to Medium Term"

    else:
        recommendation = "SELL"
        confidence = 90
        risk = "Very High"
        horizon = "Avoid / Exit"

    # -----------------------------
    # Reasons
    # -----------------------------

    if ratios.get("roe") is not None and ratios["roe"] >= 20:
        reasons.append("Excellent Return on Equity")

    if ratios.get("net_profit_margin") is not None and ratios["net_profit_margin"] >= 15:
        reasons.append("Strong Profit Margin")

    if ratios.get("debt_to_equity") is not None and ratios["debt_to_equity"] < 0.5:
        reasons.append("Low Debt")

    if ratios.get("asset_turnover") is not None and ratios["asset_turnover"] >= 1:
        reasons.append("Efficient Asset Utilization")

    # -----------------------------
    # Concerns
    # -----------------------------

    for flag in red_flags:
        if flag != "No major financial red flags detected.":
            concerns.append(flag)

    return {
        "recommendation": recommendation,
        "confidence": confidence,
        "risk_level": risk,
        "investment_horizon": horizon,
        "reasons": reasons,
        "concerns": concerns
    }