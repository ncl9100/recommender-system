#!/usr/bin/env python3
"""
Test script for the improved recommender system
"""

import requests
import json

def test_improved_system():
    """Test the improved system with various books"""
    
    test_cases = [
        {
            "name": "Diary of a Wimpy Kid (not in original dataset)",
            "data": {
                "source_category": "books",
                "target_category": "movies", 
                "preferences": ["Diary of a Wimpy Kid"],
                "limit": 3
            }
        },
        {
            "name": "The Hobbit (exact match)",
            "data": {
                "source_category": "books",
                "target_category": "movies", 
                "preferences": ["The Hobbit"],
                "limit": 3
            }
        },
        {
            "name": "Harry Potter (partial match)",
            "data": {
                "source_category": "books",
                "target_category": "movies", 
                "preferences": ["Harry Potter"],
                "limit": 3
            }
        },
        {
            "name": "Random book (should find similar)",
            "data": {
                "source_category": "books",
                "target_category": "movies", 
                "preferences": ["Some random book title"],
                "limit": 3
            }
        }
    ]
    
    print("🧪 Testing Improved Recommender System")
    print("=" * 50)
    
    for test_case in test_cases:
        print(f"\n📚 Testing: {test_case['name']}")
        print(f"Request: {json.dumps(test_case['data'], indent=2)}")
        
        try:
            response = requests.post(
                "http://localhost:8000/recommend",
                json=test_case['data'],
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ SUCCESS! Found {len(result['recommendations'])} recommendations")
                
                for i, rec in enumerate(result['recommendations'], 1):
                    print(f"  {i}. {rec['title']} (Score: {rec['similarity_score']:.3f})")
                    
            else:
                print(f"❌ ERROR {response.status_code}: {response.text}")
                
        except Exception as e:
            print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_improved_system() 