# Tests

This directory contains test files for the recommendation system.

## Test Files

- **test_logic.py** - Tests the core recommendation logic
- **test_api.py** - Tests the FastAPI endpoints
- **test_frontend.py** - Tests the React frontend components

## Running Tests

```bash
# Test the backend logic
cd backend
python ../tests/test_logic.py

# Test the API endpoints
python ../tests/test_api.py

# Test the frontend (if needed)
cd frontend
npm test
```

## Test Coverage

- **Backend Logic**: Recommendation algorithm, similarity calculations
- **API Endpoints**: Request/response validation, error handling
- **Frontend**: Component rendering, user interactions
- **Integration**: End-to-end recommendation flow 