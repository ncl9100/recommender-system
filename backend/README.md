# Recommender System Backend

FastAPI-based backend for the recommender system with machine learning capabilities.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Root endpoint
- `GET /categories` - Get available categories
- `POST /recommend` - Get recommendations
- `GET /health` - Health check

## Development

The backend uses:
- **FastAPI** for the web framework
- **scikit-learn** for ML algorithms
- **pandas** for data manipulation
- **numpy** for numerical operations

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/              # Pydantic models
│   └── services/            # Business logic
├── data/                    # Data files
└── requirements.txt         # Python dependencies
``` 