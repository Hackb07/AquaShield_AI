from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, unique=True, index=True) # Assuming anonymous use bound to device initially
    preferred_language = Column(String, default="en") # en or ta
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PredictionHistory(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    rainfall = Column(Float)
    humidity = Column(Float)
    temperature = Column(Float)
    risk_level = Column(String) # Low, Medium, High
    probability_score = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class ChatHistory(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_message = Column(String)
    bot_response = Column(String)
    language = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
