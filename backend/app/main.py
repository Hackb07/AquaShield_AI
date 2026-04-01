from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AquaShield AI Backend",
    description="Multilingual AI-Powered Flood & Infrastructure Resilience Simulation Mobile Application API",
    version="1.0.0",
)

# Configure CORS for Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to AquaShield AI API"}

from app.routes import api

app.include_router(api.router, prefix="/api/v1")
