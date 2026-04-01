import random
from typing import Tuple

class AIService:
    @staticmethod
    def predict_flood_risk(rainfall: float, humidity: float, temperature: float) -> Tuple[str, float]:
        """
        Mock implementation of a flood prediction ML model.
        In reality, this would load a trained LSTM or XGBoost model from scikit-learn.
        """
        # Simple heuristic for the mock
        risk_score = (rainfall * 0.5) + (humidity * 0.3) + ((40 - temperature) * 0.2)
        
        # Normalize arbitrarily to a 0-1 probability
        normalized_probability = min(max(risk_score / 150.0, 0.0), 1.0)
        
        # Add random noise to simulate model variance
        normalized_probability *= random.uniform(0.9, 1.1)
        normalized_probability = min(max(normalized_probability, 0.0), 1.0)
        
        if normalized_probability > 0.75:
            risk_level = "High"
        elif normalized_probability > 0.4:
            risk_level = "Medium"
        else:
            risk_level = "Low"
            
        return risk_level, round(normalized_probability, 2)
