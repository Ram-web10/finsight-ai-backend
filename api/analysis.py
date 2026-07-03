from fastapi import APIRouter
from pydantic import BaseModel

from services.analysis_pipeline import analyze_report

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


class AnalysisRequest(BaseModel):
    pdf_path: str


@router.get("/")
def status():

    return {
        "status": "Analysis API Ready"
    }


@router.post("/")
def analyze(request: AnalysisRequest):

    return analyze_report(request.pdf_path)