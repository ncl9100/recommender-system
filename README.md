# 🎯 Cross-Category Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.0+-blue.svg)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)](https://typescriptlang.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A machine learning-powered recommendation system that suggests items across different categories (movies, books, songs, games) based on user preferences.

## ✨ Features

- **Cross-Category Recommendations**: Get movie suggestions based on your favorite books, or game recommendations from your music preferences
- **ML-Powered Similarity**: Uses TF-IDF vectorization and cosine similarity for intelligent matching
- **Modern Web Interface**: Beautiful React frontend with real-time recommendations
- **RESTful API**: FastAPI backend with automatic documentation
- **Smart Fallbacks**: Always returns recommendations, even for unknown inputs

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/recommender-system.git
cd recommender-system
```

2. **Start the backend**
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. **Start the frontend** (in a new terminal)
```bash
cd frontend
npm install
npm run dev
```

4. **Open your browser**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🎯 How It Works

### Example Use Cases
- **"I like Harry Potter books"** → Get movie recommendations
- **"I enjoy Minecraft"** → Find similar games
- **"I love rock music"** → Discover related books
- **"I play adventure games"** → Get movie suggestions

### Algorithm
1. **Input Processing**: Analyzes user preferences using TF-IDF vectorization
2. **Similarity Matching**: Finds similar items within the source category
3. **Cross-Category Mapping**: Maps source similarities to target category
4. **Score Calculation**: Combines multiple similarity metrics for final ranking
5. **Result Ranking**: Returns top recommendations with similarity scores

## 📊 API Endpoints

### Get Recommendations
```http
POST /recommend
Content-Type: application/json

{
  "source_category": "books",
  "target_category": "movies", 
  "preferences": ["Harry Potter", "Lord of the Rings"],
  "limit": 5
}
```

### Available Categories
- `books` - Literature and novels
- `movies` - Films and TV shows  
- `songs` - Music and audio
- `games` - Video games and interactive media

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **Pydantic**: Data validation

### Frontend  
- **React 18**: Modern UI framework
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool
- **Tailwind CSS**: Utility-first styling
- **Axios**: HTTP client

### Machine Learning
- **TF-IDF Vectorization**: Text feature extraction
- **Cosine Similarity**: Vector similarity measurement
- **Jaccard Similarity**: Set-based similarity for cross-category matching

## 📁 Project Structure

```
recommender-system/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # API endpoints
│   │   ├── models/         # Data models
│   │   └── services/       # ML recommendation logic
│   └── data/               # JSON datasets
├── frontend/               # React frontend
│   └── src/
│       ├── components/     # UI components
│       ├── services/       # API client
│       └── types/          # TypeScript types
└── README.md              # This file
```

## 🧪 Testing

### Test the Backend
```bash
cd backend
python ../test_logic.py
```

### Test the API
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{
    "source_category": "movies",
    "target_category": "games",
    "preferences": ["minecraft"],
    "limit": 3
  }'
```

## 🚀 Deployment

### Local Development
```bash
# Start both servers
./start.sh  # Linux/Mac
# or
start.bat   # Windows
```

### Production Deployment
1. **Backend**: Deploy to Heroku, Railway, or AWS
2. **Frontend**: Build and deploy to Vercel, Netlify, or GitHub Pages
3. **Database**: Consider PostgreSQL for larger datasets

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] **Larger Datasets**: Integrate with TMDB, Spotify, and RAWG APIs
- [ ] **User Accounts**: Save preferences and recommendation history
- [ ] **Collaborative Filtering**: User-based recommendations
- [ ] **Rating System**: Allow users to rate recommendations
- [ ] **Advanced ML**: Deep learning models for better similarity
- [ ] **Mobile App**: React Native version
- [ ] **Real-time Updates**: WebSocket for live recommendations

## 📞 Support

If you have any questions or need help:
- Create an issue on GitHub
- Check the API documentation at `/docs`
- Review the test files for usage examples

---

**Built with ❤️ using FastAPI, React, and Machine Learning** 