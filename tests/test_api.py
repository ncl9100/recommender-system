#!/usr/bin/env python3
"""
Test script for FastAPI endpoints
"""

import requests
import json
import time

def test_api_endpoints():
    """Test the FastAPI endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing FastAPI endpoints...")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Root endpoint working")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure backend is running on port 8000")
        return
    
    # Test categories endpoint
    try:
        response = requests.get(f"{base_url}/categories")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Categories endpoint working: {data}")
        else:
            print(f"❌ Categories endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Categories endpoint error: {e}")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health endpoint working: {data}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health endpoint error: {e}")

def test_recommendation_endpoint():
    """Test the recommendation endpoint"""
    base_url = "http://localhost:8000"
    
    print("\n🧪 Testing recommendation endpoint...")
    
    # Test valid recommendation request
    test_data = {
        "source_category": "movies",
        "target_category": "games",
        "preferences": ["minecraft"],
        "limit": 3
    }
    
    try:
        response = requests.post(
            f"{base_url}/recommend",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data)
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Recommendation endpoint working")
            print(f"   Found {data['total_count']} recommendations")
            for i, rec in enumerate(data['recommendations'][:3], 1):
                print(f"   {i}. {rec['title']} (Score: {rec['similarity_score']:.3f})")
        else:
            print(f"❌ Recommendation endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Recommendation endpoint error: {e}")

def test_error_handling():
    """Test error handling in API"""
    base_url = "http://localhost:8000"
    
    print("\n🧪 Testing error handling...")
    
    # Test invalid category
    test_data = {
        "source_category": "invalid",
        "target_category": "games",
        "preferences": ["test"],
        "limit": 3
    }
    
    try:
        response = requests.post(
            f"{base_url}/recommend",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data)
        )
        
        if response.status_code == 500:
            print("✅ Correctly handled invalid category")
        else:
            print(f"❌ Should have returned 500 for invalid category: {response.status_code}")
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")

if __name__ == "__main__":
    print("🔍 Testing FastAPI Endpoints")
    print("=" * 50)
    
    # Wait a moment for server to start if needed
    print("⏳ Waiting for API to be ready...")
    time.sleep(2)
    
    test_api_endpoints()
    test_recommendation_endpoint()
    test_error_handling()
    
    print("\n✅ API testing completed!") 