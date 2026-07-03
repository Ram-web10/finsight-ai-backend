from typing import Dict, List
from services.stock_service import get_stock_data


# ==========================================================
# SIMPLE IN-MEMORY PORTFOLIO (can upgrade to DB later)
# ==========================================================

PORTFOLIO = []


def add_stock(symbol: str, quantity: int, buy_price: float):
    """
    Add stock to portfolio
    """

    PORTFOLIO.append({
        "symbol": symbol.upper(),
        "quantity": quantity,
        "buy_price": buy_price
    })

    return {"message": "Stock added successfully", "portfolio": PORTFOLIO}


def get_portfolio():
    """
    Return full portfolio with live valuation
    """

    enriched = []
    total_investment = 0
    total_current_value = 0

    for item in PORTFOLIO:

        stock_data = get_stock_data(item["symbol"])

        current_price = stock_data.get("currentPrice") if stock_data else None

        investment = item["quantity"] * item["buy_price"]
        current_value = item["quantity"] * (current_price or 0)

        total_investment += investment
        total_current_value += current_value

        enriched.append({
            "symbol": item["symbol"],
            "quantity": item["quantity"],
            "buy_price": item["buy_price"],
            "current_price": current_price,
            "investment": investment,
            "current_value": current_value,
            "pnl": current_value - investment,
            "pnl_percent": ((current_value - investment) / investment * 100)
            if investment else 0
        })

    return {
        "stocks": enriched,
        "total_investment": total_investment,
        "total_current_value": total_current_value,
        "total_pnl": total_current_value - total_investment,
        "total_pnl_percent": ((total_current_value - total_investment) / total_investment * 100)
        if total_investment else 0
    }