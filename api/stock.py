from fastapi import APIRouter, HTTPException
from services.stock_service import get_stock_data

router = APIRouter()

@router.get("/stock/{symbol}")
def stock_quote(symbol: str):

    data = get_stock_data(symbol)

    if not data:
        raise HTTPException(status_code=404, detail="Stock not found")

    return data

from fastapi import APIRouter, HTTPException
from services.stock_service import get_stock_data, get_stock_history

router = APIRouter()


@router.get("/stock/{symbol}")
def stock_quote(symbol: str):
    return get_stock_data(symbol)


@router.get("/stock/{symbol}/history")
def stock_history(symbol: str, period: str = "1y"):

    data = get_stock_history(symbol, period)

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    return data