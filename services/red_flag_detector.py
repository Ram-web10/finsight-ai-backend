from typing import Dict, List


def detect_red_flags(data: Dict, ratios: Dict) -> List[str]:
    """
    Detects potential financial warning signs.
    Returns a list of red flags.
    """

    red_flags = []

    # -----------------------------
    # Profitability
    # -----------------------------

    if data.get("net_profit") is not None and data["net_profit"] < 0:
        red_flags.append("Company reported a net loss.")

    if ratios.get("net_profit_margin") is not None:
        if ratios["net_profit_margin"] < 5:
            red_flags.append("Very low net profit margin.")

    # -----------------------------
    # Leverage
    # -----------------------------

    if ratios.get("debt_to_equity") is not None:
        if ratios["debt_to_equity"] > 2:
            red_flags.append("High debt-to-equity ratio.")

    if ratios.get("debt_to_assets") is not None:
        if ratios["debt_to_assets"] > 0.60:
            red_flags.append("Large proportion of assets financed by debt.")

    # -----------------------------
    # Liquidity
    # -----------------------------

    cash = data.get("cash")
    liabilities = data.get("total_liabilities")

    if cash is not None and liabilities is not None:
        if cash < liabilities * 0.10:
            red_flags.append("Very low cash compared to liabilities.")

    # -----------------------------
    # Return Ratios
    # -----------------------------

    if ratios.get("roe") is not None:
        if ratios["roe"] < 8:
            red_flags.append("Weak Return on Equity.")

    if ratios.get("roa") is not None:
        if ratios["roa"] < 3:
            red_flags.append("Weak Return on Assets.")

    # -----------------------------
    # Assets
    # -----------------------------

    if data.get("equity") is not None:
        if data["equity"] <= 0:
            red_flags.append("Negative or zero shareholder equity.")

    if data.get("total_assets") is not None:
        if data["total_assets"] <= 0:
            red_flags.append("Invalid total assets value.")

    # -----------------------------
    # Overall
    # -----------------------------

    if len(red_flags) == 0:
        red_flags.append("No major financial red flags detected.")

    return red_flags