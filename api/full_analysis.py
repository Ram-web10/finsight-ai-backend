from fastapi import APIRouter
from services.full_pipeline import analyze_full_report

router = APIRouter()


@router.post("/analysis/full-report")
def full_report(payload: dict):

    pdf_path = payload.get("pdf_path")

    return analyze_full_report(pdf_path)