from typing import Dict

# ==========================================================
# FINANCIAL SCORING ENGINE (INSTITUTIONAL STYLE)
# ==========================================================

def calculate_financial_score(data: Dict, ratios: Dict) -> Dict:
    """
    Advanced financial health scoring system.
    Returns structured rating + breakdown.
    """

    score = 0

    # ======================================================
    # PROFITABILITY (30 marks)
    # ======================================================

    net_profit = data.get("Net Profit")
    revenue = data.get("Revenue")
    roe = ratios.get("ROE")

    if net_profit and revenue:
        profit_margin = (net_profit / revenue) * 100
    else:
        profit_margin = None

    profitability_score = 0

    if profit_margin is not None:
        if profit_margin > 20:
            profitability_score += 15
        elif profit_margin > 10:
            profitability_score += 10
        elif profit_margin > 0:
            profitability_score += 5

    if roe is not None:
        if roe > 20:
            profitability_score += 15
        elif roe > 10:
            profitability_score += 10
        elif roe > 0:
            profitability_score += 5

    score += min(profitability_score, 30)

    # ======================================================
    # STABILITY (30 marks)
    # ======================================================

    current_ratio = ratios.get("Current Ratio")
    equity = data.get("Shareholders Equity")
    assets = data.get("Total Assets")

    stability_score = 0

    if current_ratio is not None:
        if current_ratio >= 2:
            stability_score += 15
        elif current_ratio >= 1:
            stability_score += 10
        else:
            stability_score += 5

    if equity and assets:
        equity_ratio = equity / assets

        if equity_ratio > 0.5:
            stability_score += 15
        elif equity_ratio > 0.3:
            stability_score += 10
        elif equity_ratio > 0.1:
            stability_score += 5

    score += min(stability_score, 30)

    # ======================================================
    # DEBT RISK (20 marks)
    # ======================================================

    debt_equity = ratios.get("Debt to Equity")
    borrowings = data.get("Borrowings")

    debt_score = 20

    if debt_equity is not None:
        if debt_equity < 0.5:
            debt_score = 20
        elif debt_equity < 1:
            debt_score = 15
        elif debt_equity < 2:
            debt_score = 10
        else:
            debt_score = 5

    if borrowings and assets:
        debt_ratio = borrowings / assets

        if debt_ratio > 0.6:
            debt_score = min(debt_score, 10)
        elif debt_ratio > 0.4:
            debt_score = min(debt_score, 15)

    score += debt_score

    # ======================================================
    # GROWTH (20 marks)
    # ======================================================

    revenue_growth = ratios.get("Revenue Growth")
    profit_growth = ratios.get("Profit Growth")

    growth_score = 0

    if revenue_growth is not None:
        if revenue_growth > 15:
            growth_score += 10
        elif revenue_growth > 5:
            growth_score += 5

    if profit_growth is not None:
        if profit_growth > 15:
            growth_score += 10
        elif profit_growth > 5:
            growth_score += 5

    score += min(growth_score, 20)

    # ======================================================
    # FINAL RATING
    # ======================================================

    if score >= 85:
        rating = "AAA"
    elif score >= 75:
        rating = "AA"
    elif score >= 65:
        rating = "A"
    elif score >= 50:
        rating = "B"
    elif score >= 35:
        rating = "C"
    else:
        rating = "D"

    # ======================================================
    # RETURN STRUCTURE
    # ======================================================

    return {
        "score": round(score, 2),
        "rating": rating,
        "breakdown": {
            "profitability": round(profitability_score, 2),
            "stability": round(stability_score, 2),
            "debt_risk": round(debt_score, 2),
            "growth": round(growth_score, 2),
        }
    }