from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Pydantic Models for Input/Output Validation ---

class PredictionRequest(BaseModel):
    user_id: Optional[int] = None # Optional for anonymous users
    rainfall: float
    humidity: float
    temperature: float

class PredictionResponse(BaseModel):
    risk_level: str
    probability_score: float

class SimulationRequest(BaseModel):
    center_lat: float
    center_lng: float
    radius_km: float

class RiskPoint(BaseModel):
    lat: float
    lng: float
    risk_score: float

class SimulationResponse(BaseModel):
    heatmap_data: List[RiskPoint]

class ChatRequest(BaseModel):
    user_id: Optional[int] = None
    message: str
    preferred_language: str = "en" # "en" or "ta"

class ChatResponse(BaseModel):
    response: str
    detected_language: str
