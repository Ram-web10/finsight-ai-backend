from fastapi import APIRouter
from services.portfolio_service import add_stock, get_portfolio

router = APIRouter()


@router.post("/portfolio/add")
def add(symbol: str, quantity: int, buy_price: float):
    return add_stock(symbol, quantity, buy_price)


@router.get("/portfolio")
def portfolio():
    return get_portfolio()