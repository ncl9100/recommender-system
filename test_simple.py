#!/usr/bin/env python3
"""
Simple test script to verify the recommender system works
"""

import requests
import json

def test_recommendations():
    """Test the recommendation API"""
    
    # Test data
    test_data = {
        "source_category": "books",
        "target_category": "movies", 
        "preferences": ["The Hobbit"],
        "limit": 3
    }
    
    try:
        # Make the request
        response = requests.post(
            "http://localhost:8000/recommend",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ SUCCESS! Recommendations received:")
            print(f"Found {len(result['recommendations'])} recommendations")
            
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"  {i}. {rec['title']} (Score: {rec['similarity_score']:.2f})")
                
        else:
            print("❌ ERROR:")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    print("🧪 Testing Recommender System...")
    test_recommendations() 