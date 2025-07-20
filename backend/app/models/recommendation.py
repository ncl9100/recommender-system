from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class RecommendationRequest(BaseModel):
    """Request model for getting recommendations"""
    source_category: str = Field(..., description="Category of user preferences (e.g., 'books')")
    target_category: str = Field(..., description="Category to get recommendations for (e.g., 'movies')")
    preferences: List[str] = Field(..., description="List of user preferences in source category")
    limit: int = Field(default=5, ge=1, le=20, description="Number of recommendations to return")

class RecommendationItem(BaseModel):
    """Model for a single recommendation item"""
    id: str
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None
    rating: Optional[float] = None
    year: Optional[int] = None
    similarity_score: float = Field(..., description="Similarity score (0-1)")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

class RecommendationResponse(BaseModel):
    """Response model for recommendations"""
    recommendations: List[RecommendationItem]
    source_category: str
    target_category: str
    total_count: int = Field(..., description="Total number of recommendations found")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "recommendations": [
                    {
                        "id": "movie_1",
                        "title": "The Lord of the Rings",
                        "description": "Epic fantasy adventure",
                        "genre": "Fantasy",
                        "rating": 8.9,
                        "year": 2001,
                        "similarity_score": 0.85,
                        "metadata": {"director": "Peter Jackson"}
                    }
                ],
                "source_category": "books",
                "target_category": "movies",
                "total_count": 1
            }
        }
    } 