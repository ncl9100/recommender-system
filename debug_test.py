#!/usr/bin/env python3
"""
Debug script to test the API with the exact data from frontend
"""

import requests
import json

def test_with_frontend_data():
    """Test with the exact data the frontend is sending"""
    
    # Test data matching what the frontend sends
    test_data = {
        "source_category": "books",
        "target_category": "movies", 
        "preferences": ["diary of a wimpy kid"],
        "limit": 6
    }
    
    print("🧪 Testing with frontend data...")
    print(f"Request data: {json.dumps(test_data, indent=2)}")
    
    try:
        # Make the request
        response = requests.post(
            "http://localhost:8000/recommend",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print("\n✅ SUCCESS! Recommendations received:")
            print(f"Found {len(result['recommendations'])} recommendations")
            
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"  {i}. {rec['title']} (Score: {rec['similarity_score']:.2f})")
                
        else:
            print(f"\n❌ ERROR {response.status_code}:")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

def test_available_books():
    """Test what books are available in the dataset"""
    print("\n📚 Available books in dataset:")
    books = [
        "The Hobbit", "1984", "The Great Gatsby", "To Kill a Mockingbird",
        "Pride and Prejudice", "The Catcher in the Rye", "Brave New World", "The Alchemist"
    ]
    for i, book in enumerate(books, 1):
        print(f"  {i}. {book}")

if __name__ == "__main__":
    test_available_books()
    test_with_frontend_data() 