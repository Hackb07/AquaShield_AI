import random
import math
from typing import List, Dict

class SimulationService:
    @staticmethod
    def run_flood_simulation(center_lat: float, center_lng: float, radius_km: float) -> List[Dict[str, float]]:
        """
        Mock grid-based flood spread simulation.
        Generates a heatmap of risk points around a center location.
        """
        heatmap = []
        # Generate roughly 30 data points around the center for the simulation
        num_points = 30
        
        for _ in range(num_points):
            # Generate random points within radius roughly (1 deg lat = ~111km)
            radius_in_deg = radius_km / 111.0
            
            # Random offset
            u = random.random()
            v = random.random()
            w = radius_in_deg * math.sqrt(u)
            t = 2 * math.pi * v
            x = w * math.cos(t)
            y = w * math.sin(t)
            
            # New coords
            pt_lat = center_lat + y
            pt_lng = center_lng + x
            
            # Calculate mock risk heavily weighting points closer to center if it was a source
            distance = math.sqrt(x**2 + y**2)
            risk = 1.0 - (distance / radius_in_deg)
            risk *= random.uniform(0.5, 1.0) # Introduce variance
            
            heatmap.append({
                "lat": pt_lat,
                "lng": pt_lng,
                "risk_score": round(max(0, risk), 2)
            })
            
        return heatmap
