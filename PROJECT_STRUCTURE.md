# Project Structure

```
recommender-system/
├── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── main.py                  # FastAPI application entry point
│   │   ├── models/
│   │   │   └── recommendation.py    # Pydantic models for API
│   │   └── services/
│   │       └── recommender.py       # Core recommendation logic
│   ├── data/                        # JSON datasets
│   │   ├── books.json
│   │   ├── movies.json
│   │   ├── songs.json
│   │   └── games.json
│   └── requirements.txt              # Python dependencies
├── frontend/                         # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── RecommendationForm.tsx
│   │   │   └── RecommendationList.tsx
│   │   ├── services/
│   │   │   └── api.ts               # API client
│   │   ├── types/
│   │   │   └── index.ts             # TypeScript types
│   │   └── App.tsx                  # Main React component
│   ├── package.json                 # Node.js dependencies
│   └── vite.config.ts               # Vite configuration
├── README.md                        # Project documentation
├── start.bat                        # Windows startup script
├── start.sh                         # Linux/Mac startup script
├── .gitignore                       # Git ignore rules
└── test_*.py                        # Test scripts
```

## Key Components

### Backend (FastAPI)
- **main.py**: API endpoints and server setup
- **recommender.py**: ML recommendation algorithm using TF-IDF and cosine similarity
- **recommendation.py**: Data models for API requests/responses
- **data/*.json**: Sample datasets for each category

### Frontend (React + TypeScript)
- **RecommendationForm.tsx**: User input form for preferences
- **RecommendationList.tsx**: Display recommendation results
- **api.ts**: HTTP client for backend communication
- **App.tsx**: Main application component

### Data Flow
1. User selects source/target categories
2. User enters preferences in source category
3. Frontend sends request to backend API
4. Backend processes preferences using ML algorithm
5. Backend returns recommendations with similarity scores
6. Frontend displays results with visual indicators

### Technologies Used
- **Backend**: FastAPI, scikit-learn, pandas, numpy
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **ML**: TF-IDF vectorization, cosine similarity, Jaccard similarity
- **Data**: JSON files with structured content metadata 