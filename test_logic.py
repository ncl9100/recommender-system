#!/usr/bin/env python3
"""
Test script to verify recommendation logic
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.services.recommender import RecommenderService

def test_minecraft_recommendation():
    """Test the minecraft movie -> minecraft game recommendation"""
    print("🧪 Testing Minecraft recommendation logic...")
    
    # Initialize recommender
    recommender = RecommenderService()
    
    # Test: "minecraft movie" -> games
    print("\n📽️ Testing: 'minecraft movie' -> games")
    recommendations = recommender.get_recommendations(
        source_category="movies",
        target_category="games", 
        preferences=["minecraft movie"],
        limit=5
    )
    
    print(f"Found {len(recommendations)} recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec.title} (Score: {rec.similarity_score:.3f})")
        if "minecraft" in rec.title.lower():
            print(f"     ✅ MINECRAFT GAME FOUND with score {rec.similarity_score:.3f}")
    
    # Test: "minecraft" -> games (should also work)
    print("\n🎮 Testing: 'minecraft' -> games")
    recommendations2 = recommender.get_recommendations(
        source_category="movies",
        target_category="games",
        preferences=["minecraft"],
        limit=5
    )
    
    print(f"Found {len(recommendations2)} recommendations:")
    for i, rec in enumerate(recommendations2, 1):
        print(f"  {i}. {rec.title} (Score: {rec.similarity_score:.3f})")
        if "minecraft" in rec.title.lower():
            print(f"     ✅ MINECRAFT GAME FOUND with score {rec.similarity_score:.3f}")

def test_other_recommendations():
    """Test other recommendation scenarios"""
    print("\n🧪 Testing other recommendation scenarios...")
    
    recommender = RecommenderService()
    
    # Test: "harry potter" books -> movies
    print("\n📚 Testing: 'harry potter' books -> movies")
    recommendations = recommender.get_recommendations(
        source_category="books",
        target_category="movies",
        preferences=["harry potter"],
        limit=3
    )
    
    print(f"Found {len(recommendations)} recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec.title} (Score: {rec.similarity_score:.3f})")
    
    # Test: "fantasy" books -> games
    print("\n🎮 Testing: 'fantasy' books -> games")
    recommendations2 = recommender.get_recommendations(
        source_category="books",
        target_category="games",
        preferences=["fantasy"],
        limit=3
    )
    
    print(f"Found {len(recommendations2)} recommendations:")
    for i, rec in enumerate(recommendations2, 1):
        print(f"  {i}. {rec.title} (Score: {rec.similarity_score:.3f})")

if __name__ == "__main__":
    print("🔍 Testing Recommendation System Logic")
    print("=" * 50)
    
    try:
        test_minecraft_recommendation()
        test_other_recommendations()
        print("\n✅ All tests completed!")
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc() 