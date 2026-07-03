from typing import Dict, List


def generate_swot(
    financial_data: Dict,
    ratios: Dict,
    financial_score: Dict,
    red_flags: List,
    recommendation: Dict,
) -> Dict:
    """
    Generate a SWOT analysis based on financial metrics,
    ratios, score, red flags and recommendation.
    """

    strengths = []
    weaknesses = []
    opportunities = []
    threats = []

    score = financial_score.get("score", 0)

    roe = ratios.get("ROE")
    roce = ratios.get("ROCE")
    current_ratio = ratios.get("Current Ratio")
    debt_equity = ratios.get("Debt to Equity")

    # -----------------------
    # Strengths
    # -----------------------

    if score >= 80:
        strengths.append("Overall financial health is excellent.")

    if roe is not None and roe >= 15:
        strengths.append(f"Strong Return on Equity ({roe:.2f}%).")

    if roce is not None and roce >= 15:
        strengths.append(f"Efficient capital utilization (ROCE {roce:.2f}%).")

    if current_ratio is not None and current_ratio >= 1.5:
        strengths.append("Healthy liquidity position.")

    if debt_equity is not None and debt_equity <= 1:
        strengths.append("Low debt burden.")

    # -----------------------
    # Weaknesses
    # -----------------------

    if score < 60:
        weaknesses.append("Overall financial health needs improvement.")

    if roe is not None and roe < 10:
        weaknesses.append("Weak shareholder returns.")

    if current_ratio is not None and current_ratio < 1:
        weaknesses.append("Short-term liquidity is weak.")

    if debt_equity is not None and debt_equity > 2:
        weaknesses.append("Company is highly leveraged.")

    # -----------------------
    # Opportunities
    # -----------------------

    opportunities.append(
        "Improve profitability through operational efficiency."
    )

    opportunities.append(
        "Expand into new markets and product segments."
    )

    if recommendation.get("recommendation") == "BUY":
        opportunities.append(
            "Strong financial position supports long-term growth."
        )

    # -----------------------
    # Threats
    # -----------------------

    if len(red_flags) > 0:
        threats.append(
            "Existing financial red flags require management attention."
        )

    threats.append(
        "Economic slowdown may reduce future earnings."
    )

    threats.append(
        "Competitive pressure could impact margins."
    )

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "opportunities": opportunities,
        "threats": threats,
    }