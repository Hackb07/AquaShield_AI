from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schemas import (
    PredictionRequest, PredictionResponse, 
    SimulationRequest, SimulationResponse,
    ChatRequest, ChatResponse
)
from app.models.models import PredictionHistory, ChatHistory
from app.services.ai_service import AIService
from app.services.simulation_service import SimulationService
from app.services.chatbot_service import ChatbotService

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict_flood(request: PredictionRequest, db: Session = Depends(get_db)):
    # Get ML Prediction
    risk, score = AIService.predict_flood_risk(
        rainfall=request.rainfall,
        humidity=request.humidity,
        temperature=request.temperature
    )

    # Save to db
    db_prediction = PredictionHistory(
        user_id=request.user_id,
        rainfall=request.rainfall,
        humidity=request.humidity,
        temperature=request.temperature,
        risk_level=risk,
        probability_score=score
    )
    db.add(db_prediction)
    db.commit()

    return {"risk_level": risk, "probability_score": score}

@router.post("/simulate", response_model=SimulationResponse)
def run_simulation(request: SimulationRequest):
    # Run simulation
    heatmap = SimulationService.run_flood_simulation(
        center_lat=request.center_lat,
        center_lng=request.center_lng,
        radius_km=request.radius_km
    )

    # Returns heatmap data
    return {"heatmap_data": heatmap}

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest, db: Session = Depends(get_db)):
    # Process chatbot message
    bot_reply = await ChatbotService.process_chat(
        message=request.message,
        target_lang=request.preferred_language
    )

    # Save to db
    if request.user_id:
        db_chat = ChatHistory(
            user_id=request.user_id,
            user_message=request.message,
            bot_response=bot_reply,
            language=request.preferred_language
        )
        db.add(db_chat)
        db.commit()

    return {"response": bot_reply, "detected_language": request.preferred_language}
