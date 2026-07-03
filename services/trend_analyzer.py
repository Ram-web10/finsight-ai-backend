from typing import Dict, List

# ==========================================================
# GROWTH CALCULATION
# ==========================================================

def calculate_growth(current, previous):
    if current is None or previous is None:
        return None
    if previous == 0:
        return None

    return ((current - previous) / abs(previous)) * 100


# ==========================================================
# TREND ANALYSIS ENGINE
# ==========================================================

def analyze_trends(financial_history: List[Dict]) -> Dict:

    if len(financial_history) < 2:
        return {"message": "Need at least 2 years of data"}

    latest = financial_history[-1]
    previous = financial_history[-2]

    trends = {
        "Revenue Growth %": calculate_growth(
            latest.get("Revenue"),
            previous.get("Revenue")
        ),
        "Profit Growth %": calculate_growth(
            latest.get("Net Profit"),
            previous.get("Net Profit")
        ),
        "Asset Growth %": calculate_growth(
            latest.get("Total Assets"),
            previous.get("Total Assets")
        ),
        "Equity Growth %": calculate_growth(
            latest.get("Shareholders Equity"),
            previous.get("Shareholders Equity")
        ),
    }

    summary = []

    if trends["Revenue Growth %"] and trends["Revenue Growth %"] > 10:
        summary.append("Strong revenue growth")

    if trends["Profit Growth %"] and trends["Profit Growth %"] > 10:
        summary.append("Strong profit expansion")

    if trends["Revenue Growth %"] and trends["Revenue Growth %"] < 0:
        summary.append("Revenue declining - risk signal")

    trends["summary"] = summary

    return trends