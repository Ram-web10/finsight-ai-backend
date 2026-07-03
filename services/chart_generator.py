from typing import Dict, List


def generate_charts(financial_data: Dict, ratios: Dict) -> Dict:
    """
    Generate chart-ready JSON for the frontend.
    """

    revenue = financial_data.get("Revenue")
    profit = financial_data.get("Net Profit")
    assets = financial_data.get("Total Assets")
    liabilities = financial_data.get("Total Liabilities")
    equity = financial_data.get("Shareholders Equity")

    # -----------------------------
    # Financial Overview
    # -----------------------------

    financial_overview: List[Dict] = []

    if revenue is not None:
        financial_overview.append({
            "name": "Revenue",
            "value": revenue
        })

    if profit is not None:
        financial_overview.append({
            "name": "Net Profit",
            "value": profit
        })

    if assets is not None:
        financial_overview.append({
            "name": "Assets",
            "value": assets
        })

    if liabilities is not None:
        financial_overview.append({
            "name": "Liabilities",
            "value": liabilities
        })

    if equity is not None:
        financial_overview.append({
            "name": "Equity",
            "value": equity
        })

    # -----------------------------
    # Ratio Overview
    # -----------------------------

    ratio_chart: List[Dict] = []

    for key, value in ratios.items():

        if isinstance(value, (int, float)):

            ratio_chart.append({
                "ratio": key,
                "value": round(value, 2)
            })

    return {

        "financial_overview": financial_overview,

        "ratio_chart": ratio_chart

    }