from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="Smart Canteen API",
    version="1.0.0",
    description="Backend API untuk Proyek Smart Canteen UI"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Selamat datang di Smart Canteen API v1"}