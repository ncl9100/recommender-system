from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import traceback
import logging

from .services.recommender import RecommenderService
from .models.recommendation import RecommendationRequest, RecommendationResponse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Recommender System API",
    description="A recommendation engine for movies, books, songs, and games",
    version="1.0.0"
)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommender service
try:
    recommender_service = RecommenderService()
    logger.info("RecommenderService initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize RecommenderService: {e}")
    logger.error(traceback.format_exc())
    recommender_service = None

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Recommender System API", "version": "1.0.0"}

@app.get("/categories")
async def get_categories():
    """Get available categories for recommendations"""
    return {
        "categories": ["movies", "books", "songs", "games"],
        "description": "Available content categories for recommendations"
    }

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """Get recommendations based on user preferences"""
    try:
        logger.info(f"Received recommendation request: {request}")
        
        if recommender_service is None:
            raise HTTPException(status_code=500, detail="RecommenderService not initialized")
        
        recommendations = recommender_service.get_recommendations(
            source_category=request.source_category,
            target_category=request.target_category,
            preferences=request.preferences,
            limit=request.limit
        )
        
        logger.info(f"Generated {len(recommendations)} recommendations")
        
        return RecommendationResponse(
            recommendations=recommendations,
            source_category=request.source_category,
            target_category=request.target_category,
            total_count=len(recommendations)
        )
    except Exception as e:
        logger.error(f"Error in get_recommendations: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "recommender-api"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 