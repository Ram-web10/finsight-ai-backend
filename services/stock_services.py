import yfinance as yf

def get_stock_data(symbol: str):
    stock = yf.Ticker(symbol)
    info = stock.info

    return {
        "symbol": symbol.upper(),
        "shortName": info.get("shortName"),
        "currentPrice": info.get("regularMarketPrice"),
    }


def get_stock_history(symbol: str, period: str = "1y"):
    """
    Returns real historical stock prices
    period: 1d,5d,1mo,6mo,1y,5y,max
    """

    stock = yf.Ticker(symbol)

    hist = stock.history(period=period)

    if hist.empty:
        return []

    data = []

    for index, row in hist.iterrows():
        data.append({
            "date": index.strftime("%Y-%m-%d"),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
        })

    return data