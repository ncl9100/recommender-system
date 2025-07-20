import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Any
import json
import os

from ..models.recommendation import RecommendationItem

class RecommenderService:
    """Service for generating recommendations based on similarity"""
    
    def __init__(self):
        self.data = self._load_sample_data()
        self.vectorizers = {}
        self.similarity_matrices = {}
        self._build_similarity_matrices()
    
    def _load_sample_data(self) -> Dict[str, pd.DataFrame]:
        """Load sample datasets for different categories from JSON files"""
        data = {}
        
        # Define data file paths
        data_files = {
            "books": "data/books.json",
            "movies": "data/movies.json",
            "songs": "data/songs.json", 
            "games": "data/games.json"
        }
        
        # Load data from JSON files
        for category, file_path in data_files.items():
            try:
                # Get the absolute path to the data file
                current_dir = os.path.dirname(os.path.abspath(__file__))
                data_file = os.path.join(current_dir, "..", "..", file_path)
                
                if os.path.exists(data_file):
                    with open(data_file, 'r', encoding='utf-8') as f:
                        items = json.load(f)
                    data[category] = pd.DataFrame(items)
                else:
                    # Fallback to hardcoded data if file doesn't exist
                    data[category] = self._get_fallback_data(category)
                    
            except Exception as e:
                print(f"Warning: Could not load {file_path}, using fallback data: {e}")
                data[category] = self._get_fallback_data(category)
        
        return data
    
    def _get_fallback_data(self, category: str) -> pd.DataFrame:
        """Fallback data if JSON files are not available"""
        
        if category == "books":
            books_data = [
                {"id": "book_1", "title": "The Hobbit", "genre": "Fantasy", "year": 1937, "rating": 4.3, "description": "Fantasy adventure novel"},
                {"id": "book_2", "title": "1984", "genre": "Sci-Fi", "year": 1949, "rating": 4.2, "description": "Dystopian political fiction"},
                {"id": "book_3", "title": "The Great Gatsby", "genre": "Drama", "year": 1925, "rating": 3.9, "description": "American classic novel"},
                {"id": "book_4", "title": "To Kill a Mockingbird", "genre": "Drama", "year": 1960, "rating": 4.3, "description": "Coming-of-age story"},
                {"id": "book_5", "title": "Pride and Prejudice", "genre": "Romance", "year": 1813, "rating": 4.3, "description": "Classic romance novel"},
                {"id": "book_6", "title": "The Catcher in the Rye", "genre": "Drama", "year": 1951, "rating": 3.8, "description": "Coming-of-age novel"},
                {"id": "book_7", "title": "Brave New World", "genre": "Sci-Fi", "year": 1932, "rating": 3.9, "description": "Dystopian science fiction"},
                {"id": "book_8", "title": "The Alchemist", "genre": "Fantasy", "year": 1988, "rating": 3.9, "description": "Philosophical novel"},
            ]
            return pd.DataFrame(books_data)
            
        elif category == "movies":
            movies_data = [
                {"id": "movie_1", "title": "The Lord of the Rings", "genre": "Fantasy", "year": 2001, "rating": 8.9, "description": "Epic fantasy adventure"},
                {"id": "movie_2", "title": "Harry Potter", "genre": "Fantasy", "year": 2001, "rating": 7.6, "description": "Magical school adventure"},
                {"id": "movie_3", "title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "rating": 8.7, "description": "Cyberpunk action thriller"},
                {"id": "movie_4", "title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8, "description": "Mind-bending thriller"},
                {"id": "movie_5", "title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "rating": 9.3, "description": "Prison drama about hope"},
                {"id": "movie_6", "title": "Pulp Fiction", "genre": "Crime", "year": 1994, "rating": 8.9, "description": "Quirky crime anthology"},
                {"id": "movie_7", "title": "The Godfather", "genre": "Crime", "year": 1972, "rating": 9.2, "description": "Epic crime drama"},
                {"id": "movie_8", "title": "Titanic", "genre": "Romance", "year": 1997, "rating": 7.9, "description": "Epic romance disaster"},
            ]
            return pd.DataFrame(movies_data)
            
        elif category == "songs":
            songs_data = [
                {"id": "song_1", "title": "Bohemian Rhapsody", "genre": "Rock", "year": 1975, "rating": 4.8, "description": "Epic rock opera"},
                {"id": "song_2", "title": "Imagine", "genre": "Pop", "year": 1971, "rating": 4.7, "description": "Peace anthem"},
                {"id": "song_3", "title": "Hotel California", "genre": "Rock", "year": 1976, "rating": 4.6, "description": "Classic rock ballad"},
                {"id": "song_4", "title": "Stairway to Heaven", "genre": "Rock", "year": 1971, "rating": 4.7, "description": "Epic rock masterpiece"},
                {"id": "song_5", "title": "Billie Jean", "genre": "Pop", "year": 1983, "rating": 4.5, "description": "Pop dance hit"},
                {"id": "song_6", "title": "Like a Rolling Stone", "genre": "Rock", "year": 1965, "rating": 4.6, "description": "Folk rock classic"},
                {"id": "song_7", "title": "Smells Like Teen Spirit", "genre": "Rock", "year": 1991, "rating": 4.5, "description": "Grunge anthem"},
                {"id": "song_8", "title": "Yesterday", "genre": "Pop", "year": 1965, "rating": 4.4, "description": "Beatles classic"},
            ]
            return pd.DataFrame(songs_data)
            
        elif category == "games":
            games_data = [
                {"id": "game_1", "title": "The Legend of Zelda", "genre": "Adventure", "year": 1986, "rating": 4.8, "description": "Classic adventure game"},
                {"id": "game_2", "title": "Final Fantasy VII", "genre": "RPG", "year": 1997, "rating": 4.7, "description": "Epic RPG adventure"},
                {"id": "game_3", "title": "Super Mario Bros", "genre": "Platformer", "year": 1985, "rating": 4.6, "description": "Classic platformer"},
                {"id": "game_4", "title": "Tetris", "genre": "Puzzle", "year": 1984, "rating": 4.5, "description": "Classic puzzle game"},
                {"id": "game_5", "title": "Minecraft", "genre": "Sandbox", "year": 2011, "rating": 4.7, "description": "Creative sandbox game"},
                {"id": "game_6", "title": "The Witcher 3", "genre": "RPG", "year": 2015, "rating": 4.8, "description": "Epic fantasy RPG"},
                {"id": "game_7", "title": "Portal", "genre": "Puzzle", "year": 2007, "rating": 4.6, "description": "Innovative puzzle game"},
                {"id": "game_8", "title": "Red Dead Redemption 2", "genre": "Adventure", "year": 2018, "rating": 4.7, "description": "Western adventure game"},
            ]
            return pd.DataFrame(games_data)
        
        return pd.DataFrame()
    
    def _build_similarity_matrices(self):
        """Build similarity matrices for each category"""
        for category, df in self.data.items():
            # Create a new vectorizer for each category
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
            
            # Combine title, genre, and description for similarity calculation
            text_data = df['title'] + ' ' + df['genre'] + ' ' + df['description'].fillna('')
            
            # Create TF-IDF vectors
            tfidf_matrix = vectorizer.fit_transform(text_data)
            
            # Store vectorizer for this category
            self.vectorizers[category] = vectorizer
            
            # Calculate cosine similarity
            similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            
            self.similarity_matrices[category] = similarity_matrix
    
    def _find_similar_items(self, preference: str, source_df: pd.DataFrame, source_vectorizer) -> List[tuple]:
        """Find similar items for a preference, even if not exact match"""
        
        # First try exact match
        matching_items = source_df[source_df['title'].str.contains(preference, case=False, na=False)]
        
        if not matching_items.empty:
            # Use exact matches
            results = []
            for _, item in matching_items.iterrows():
                item_idx = source_df.index.get_loc(item.name)
                results.append((item_idx, 1.0))
            return results
        
        # If no exact match, use TF-IDF similarity
        try:
            # Create vector for the preference
            preference_vector = source_vectorizer.transform([preference])
            
            # Get all source items as vectors
            source_text = source_df['title'] + ' ' + source_df['genre'] + ' ' + source_df['description'].fillna('')
            source_vectors = source_vectorizer.transform(source_text)
            
            # Calculate similarities
            similarities = cosine_similarity(preference_vector, source_vectors)[0]
            
            # Get top 3 most similar items
            top_indices = np.argsort(similarities)[::-1][:3]
            results = [(idx, similarities[idx]) for idx in top_indices if similarities[idx] > 0.1]
            
            return results
            
        except Exception as e:
            # Fallback to simple text similarity
            results = []
            for idx, item in source_df.iterrows():
                item_text = f"{item['title']} {item['genre']} {item['description']}".lower()
                preference_lower = preference.lower()
                
                # Simple word overlap similarity
                item_words = set(item_text.split())
                pref_words = set(preference_lower.split())
                
                if pref_words:
                    overlap = len(item_words.intersection(pref_words))
                    similarity = overlap / len(pref_words)
                    if similarity > 0:
                        results.append((idx, similarity))
            
            # Sort by similarity and return top 3
            results.sort(key=lambda x: x[1], reverse=True)
            return results[:3]
    
    def get_recommendations(self, source_category: str, target_category: str, 
                          preferences: List[str], limit: int = 5) -> List[RecommendationItem]:
        """Get recommendations based on user preferences"""
        
        # Validate categories
        if source_category not in self.data or target_category not in self.data:
            raise ValueError(f"Invalid category. Available: {list(self.data.keys())}")
        
        # Validate preferences
        if not preferences or len(preferences) == 0:
            raise ValueError("At least one preference is required")
        
        # Filter out empty preferences
        valid_preferences = [p.strip() for p in preferences if p.strip()]
        if not valid_preferences:
            raise ValueError("At least one non-empty preference is required")
        
        # Find similar items in source category based on preferences
        source_df = self.data[source_category]
        target_df = self.data[target_category]
        
        # Get vectorizers for both categories
        source_vectorizer = self.vectorizers[source_category]
        target_vectorizer = self.vectorizers[target_category]
        
        # Calculate similarity scores for preferences
        preference_scores = []
        
        for preference in valid_preferences:
            similar_items = self._find_similar_items(preference, source_df, source_vectorizer)
            preference_scores.extend(similar_items)
        
        # If no similar items found, use all items with low scores
        if not preference_scores:
            for idx in range(len(source_df)):
                preference_scores.append((idx, 0.1))
        
        # Calculate cross-category similarity
        recommendations = []
        
        for target_idx, target_item in target_df.iterrows():
            target_text = f"{target_item['title']} {target_item['genre']} {target_item['description']}"
            
            total_score = 0
            max_score = 0
            
            for source_idx, source_score in preference_scores:
                source_item = source_df.iloc[source_idx]
                source_text = f"{source_item['title']} {source_item['genre']} {source_item['description']}"
                
                # Check for exact title matches first (highest priority)
                for preference in valid_preferences:
                    preference_lower = preference.lower()
                    target_title_lower = target_item['title'].lower()
                    
                    # If preference contains a word that matches target title, give high score
                    pref_words = set(preference_lower.split())
                    target_words = set(target_title_lower.split())
                    
                    # Check for word overlap between preference and target title
                    title_overlap = len(pref_words.intersection(target_words))
                    if title_overlap > 0:
                        # Boost score significantly for title matches
                        title_score = min(0.9, 0.3 + (title_overlap * 0.2))
                        max_score = max(max_score, title_score)
                
                # Use improved text similarity approach for cross-category
                source_words = set(source_text.lower().split())
                target_words = set(target_text.lower().split())
                
                # Calculate improved similarity
                intersection = len(source_words.intersection(target_words))
                union = len(source_words.union(target_words))
                
                # Use both Jaccard and word overlap similarity
                jaccard_similarity = intersection / union if union > 0 else 0
                overlap_similarity = intersection / len(source_words) if len(source_words) > 0 else 0
                
                # Combine similarities with better weighting
                combined_similarity = (jaccard_similarity * 0.4) + (overlap_similarity * 0.6)
                
                # Apply source score as weight
                weighted_score = combined_similarity * source_score
                total_score += weighted_score
                max_score = max(max_score, weighted_score)
            
            # Use the maximum score found (better than average)
            final_score = max_score if max_score > 0 else (total_score / len(preference_scores) if preference_scores else 0)
            
            if final_score > 0:
                recommendations.append({
                    'id': target_item['id'],
                    'title': target_item['title'],
                    'description': target_item['description'],
                    'genre': target_item['genre'],
                    'rating': target_item['rating'],
                    'year': target_item['year'],
                    'similarity_score': float(final_score),
                    'metadata': {}
                })
        
        # Sort by similarity score and return top recommendations
        recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        return [RecommendationItem(**rec) for rec in recommendations[:limit]] 