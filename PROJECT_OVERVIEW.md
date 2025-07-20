# Recommender System - Project Overview

## 🎯 What This Project Does

This is a **cross-category recommendation engine** that suggests content in one category based on your preferences in another category. For example:
- You like certain books → Get movie recommendations
- You enjoy specific songs → Get game recommendations
- You love particular movies → Get book recommendations

## 🏗️ Architecture Overview

### Backend (Python/FastAPI)
The backend handles the **machine learning logic** and provides a REST API:

**Key Components:**
- **FastAPI** - Modern, fast web framework with automatic API docs
- **scikit-learn** - ML library for similarity calculations using TF-IDF and cosine similarity
- **pandas/numpy** - Data manipulation and numerical operations
- **Pydantic** - Data validation and serialization

**How the ML Works:**
1. **Text Vectorization**: Converts titles, genres, and descriptions into numerical vectors using TF-IDF
2. **Similarity Calculation**: Uses cosine similarity to find similar items across categories
3. **Cross-Category Mapping**: Maps preferences from source category to target category based on content similarity

### Frontend (React/TypeScript)
The frontend provides a **modern, responsive web interface**:

**Key Components:**
- **React 18** with TypeScript for type safety
- **Tailwind CSS** for rapid, responsive styling
- **Vite** for fast development and building
- **Axios** for API communication
- **Lucide React** for beautiful icons

**User Experience:**
1. User selects source category (what they like)
2. User selects target category (what they want recommendations for)
3. User enters their preferences
4. System returns personalized recommendations with similarity scores

## 🚀 Quick Start Guide

### Option 1: Automated Setup (Windows)
```bash
# Double-click or run:
start.bat
```

### Option 2: Automated Setup (Mac/Linux)
```bash
# Make executable and run:
chmod +x start.sh
./start.sh
```

### Option 3: Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 📊 Sample Data

The system includes sample data for 4 categories:

**Movies (8 items):**
- The Lord of the Rings, Harry Potter, The Matrix, Inception, etc.

**Books (8 items):**
- The Hobbit, 1984, The Great Gatsby, To Kill a Mockingbird, etc.

**Songs (8 items):**
- Bohemian Rhapsody, Imagine, Hotel California, Stairway to Heaven, etc.

**Games (8 items):**
- The Legend of Zelda, Final Fantasy VII, Super Mario Bros, Tetris, etc.

## 🔧 How the Recommendation Algorithm Works

### Step 1: Text Processing
- Combines title, genre, and description into a single text string
- Applies TF-IDF vectorization to convert text to numerical features
- Removes common stop words and focuses on meaningful terms

### Step 2: Similarity Calculation
- Uses cosine similarity to measure how similar two items are
- Higher similarity = more similar content characteristics
- Works across categories by comparing content features

### Step 3: Cross-Category Mapping
- Takes user preferences from source category
- Finds similar items in target category
- Ranks recommendations by similarity score
- Returns top matches with confidence scores

### Example Flow:
1. User likes "The Hobbit" (Fantasy book)
2. System finds similar fantasy content
3. Recommends "The Lord of the Rings" (Fantasy movie)
4. Shows similarity score (e.g., 0.85 = 85% match)

## 🎨 Features

### MVP Features (Phase 1) ✅
- [x] Cross-category recommendations
- [x] Similarity-based algorithm
- [x] Modern web interface
- [x] Real-time API responses
- [x] Sample dataset
- [x] Responsive design

### Future Features (Phase 2 & 3)
- [ ] User accounts and profiles
- [ ] Collaborative filtering
- [ ] Content-based filtering
- [ ] Rating system
- [ ] Recommendation history
- [ ] Larger datasets
- [ ] Advanced ML algorithms

## 🛠️ Development

### Backend Development
- **API Documentation**: Visit http://localhost:8000/docs
- **Hot Reload**: Changes auto-reload during development
- **Type Safety**: Pydantic models ensure data validation

### Frontend Development
- **Hot Reload**: Changes appear instantly
- **TypeScript**: Catches errors at compile time
- **Tailwind**: Rapid UI development with utility classes

### Testing
```bash
# Test backend API
python test_backend.py
```

## 📁 Project Structure

```
recommender-system/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── models/         # Pydantic data models
│   │   └── services/       # ML recommendation service
│   └── requirements.txt    # Python dependencies
├── frontend/               # React TypeScript frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API communication
│   │   └── types/          # TypeScript definitions
│   └── package.json       # Node.js dependencies
├── start.bat              # Windows startup script
├── start.sh               # Unix startup script
├── test_backend.py        # Backend testing script
└── README.md              # Main project documentation
```

## 🔍 API Endpoints

- `GET /` - Root endpoint
- `GET /categories` - Get available categories
- `POST /recommend` - Get recommendations
- `GET /health` - Health check

## 🎯 Learning Objectives

This project demonstrates:
1. **Full-Stack Development** - Backend + Frontend integration
2. **Machine Learning** - Similarity-based recommendation algorithms
3. **Modern Web Technologies** - FastAPI, React, TypeScript
4. **API Design** - RESTful API with automatic documentation
5. **Data Processing** - Text vectorization and similarity calculations
6. **User Experience** - Intuitive, responsive web interface

## 🚀 Deployment

### Local Development
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs

### Production Considerations
- Use production WSGI server (Gunicorn) for backend
- Build frontend with `npm run build`
- Set up proper CORS configuration
- Add environment variables for configuration
- Implement proper error handling and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

MIT License - feel free to use this project for learning and development! 

## **The Fix: Use Real Category Names**

In the Swagger UI, you need to replace the placeholder values with actual category names:

### **Step 1: Update the Request Body**

Replace the default JSON with this:

```json
{
  "source_category": "books",
  "target_category": "movies",
  "preferences": ["The Hobbit"],
  "limit": 3
}
```

### **Step 2: Click "Execute" Again**

After updating the JSON with real category names, click "Execute" again.

## **Expected Result**

You should now get a **200 OK** response with actual recommendations like:
```json
{
  "recommendations": [
    {
      "id": "movie_1",
      "title": "The Lord of the Rings",
      "description": "Epic fantasy adventure",
      "genre": "Fantasy",
      "rating": 8.9,
      "year": 2001,
      "similarity_score": 0.85,
      "metadata": {}
    }
  ],
  "source_category": "books",
  "target_category": "movies",
  "total_count": 1
}
```

## **Step 3: Test the Frontend**

Once the API works, go back to your frontend at **http://localhost:5173** and try getting recommendations there too!

**Try updating the JSON with real category names and let me know what response you get!** 