from fastapi import APIRouter
from services.signal_engine import generate_signal

router = APIRouter()


@router.post("/signal")
def get_signal(payload: dict):

    return generate_signal(
        financial_score=payload.get("financial_score", {}),
        ratios=payload.get("ratios", {}),
        sentiment=payload.get("sentiment", {}),
        trends=payload.get("trends", {})
    )