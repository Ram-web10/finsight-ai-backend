from typing import List, Dict


def compare_companies(companies: List[Dict]) -> Dict:
    """
    Compare multiple companies based on key financial metrics.

    Expected format:
    [
        {
            "company": "Apple",
            "financial_score": 92,
            "ratios": {
                "roe": 28,
                "net_profit_margin": 24,
                "debt_to_equity": 0.45
            }
        }
    ]
    """

    if len(companies) < 2:
        return {
            "error": "At least two companies are required for comparison."
        }

    ranking = sorted(
        companies,
        key=lambda x: x.get("financial_score", 0),
        reverse=True
    )

    comparison_table = []

    for company in ranking:

        ratios = company.get("ratios", {})

        comparison_table.append({
            "company": company.get("company"),
            "financial_score": company.get("financial_score"),
            "roe": ratios.get("roe"),
            "net_profit_margin": ratios.get("net_profit_margin"),
            "debt_to_equity": ratios.get("debt_to_equity"),
            "asset_turnover": ratios.get("asset_turnover")
        })

    best_company = ranking[0]["company"]

    return {
        "best_company": best_company,
        "ranking": comparison_table
    }