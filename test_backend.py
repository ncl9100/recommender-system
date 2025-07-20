#!/usr/bin/env python3
"""
Simple test script for the recommender system backend
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_categories():
    """Test the categories endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/categories")
        print(f"✅ Categories: {response.status_code}")
        print(f"   Available categories: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Categories failed: {e}")
        return False

def test_recommendations():
    """Test the recommendations endpoint"""
    try:
        data = {
            "source_category": "books",
            "target_category": "movies",
            "preferences": ["The Hobbit", "1984"],
            "limit": 3
        }
        
        response = requests.post(f"{BASE_URL}/recommend", json=data)
        print(f"✅ Recommendations: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   Found {len(result['recommendations'])} recommendations")
            for i, rec in enumerate(result['recommendations'][:2]):
                print(f"   {i+1}. {rec['title']} (Score: {rec['similarity_score']:.2f})")
        else:
            print(f"   Error: {response.text}")
        
        return True
    except Exception as e:
        print(f"❌ Recommendations failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Recommender System Backend")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health),
        ("Categories", test_categories),
        ("Recommendations", test_recommendations),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Backend is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the backend server.")

if __name__ == "__main__":
    main() 