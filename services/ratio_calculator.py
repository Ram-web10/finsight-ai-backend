from typing import Dict, Optional

# ==========================================================
# SAFE DIVISION
# ==========================================================

def safe_divide(a: Optional[float], b: Optional[float]):
    if a is None or b is None:
        return None
    if b == 0:
        return None
    return a / b


# ==========================================================
# RATIO CALCULATION ENGINE
# ==========================================================

def calculate_ratios(data: Dict) -> Dict:
    """
    Compute key financial ratios from extracted data.
    """

    revenue = data.get("Revenue")
    net_profit = data.get("Net Profit")
    operating_profit = data.get("Operating Profit")

    assets = data.get("Total Assets")
    liabilities = data.get("Total Liabilities")
    equity = data.get("Shareholders Equity")

    current_assets = data.get("Current Assets")
    current_liabilities = data.get("Current Liabilities")

    borrowings = data.get("Borrowings")

    # -----------------------------
    # Profitability Ratios
    # -----------------------------

    profit_margin = safe_divide(net_profit, revenue)
    operating_margin = safe_divide(operating_profit, revenue)

    roe = safe_divide(net_profit, equity)
    roa = safe_divide(net_profit, assets)

    # -----------------------------
    # Liquidity Ratios
    # -----------------------------

    current_ratio = safe_divide(current_assets, current_liabilities)

    # -----------------------------
    # Leverage Ratios
    # -----------------------------

    debt_to_equity = safe_divide(borrowings, equity)

    debt_ratio = safe_divide(liabilities, assets)

    # -----------------------------
    # Growth placeholders (future)
    # -----------------------------

    ratios = {
        "Profit Margin": profit_margin * 100 if profit_margin else None,
        "Operating Margin": operating_margin * 100 if operating_margin else None,
        "ROE": roe * 100 if roe else None,
        "ROA": roa * 100 if roa else None,
        "Current Ratio": current_ratio,
        "Debt to Equity": debt_to_equity,
        "Debt Ratio": debt_ratio,
    }

    return ratios