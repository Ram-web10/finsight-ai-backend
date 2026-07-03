from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# =========================
# APP INIT
# =========================
app = FastAPI(
    title="FinSight AI",
    description="AI Powered Equity Research & Financial Analysis Platform",
    version="1.0.0"
)

# =========================
# ROUTERS
# =========================
from api.upload import router as upload_router
from api.analysis import router as analysis_router
from api.stock import router as stock_router
from api.news import router as news_router
from api.portfolio import router as portfolio_router
from api.signal import router as signal_router
from api.full_analysis import router as full_analysis_router

app.include_router(upload_router)
app.include_router(analysis_router)
app.include_router(stock_router)
app.include_router(news_router)
app.include_router(portfolio_router)
app.include_router(signal_router)
app.include_router(full_analysis_router)

# =========================
# CORS (PRODUCTION SAFE)
# =========================
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://finsight-ai-frontend-seven.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "message": "Welcome to FinSight AI Backend",
        "status": "Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "FinSight AI Backend",
        "version": "1.0.0"
    }