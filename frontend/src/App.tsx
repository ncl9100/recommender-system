import React, { useState } from 'react';
import { RecommendationForm } from './components/RecommendationForm';
import { RecommendationList } from './components/RecommendationList';
import { recommenderApi } from './services/api';
import { RecommendationItem } from './types';

function App() {
  const [recommendations, setRecommendations] = useState<RecommendationItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [sourceCategory, setSourceCategory] = useState('');
  const [targetCategory, setTargetCategory] = useState('');

  const handleGetRecommendations = async (
    sourceCat: string,
    targetCat: string,
    preferences: string[]
  ) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await recommenderApi.getRecommendations({
        source_category: sourceCat,
        target_category: targetCat,
        preferences,
        limit: 6,
      });
      
      setRecommendations(response.recommendations);
      setSourceCategory(sourceCat);
      setTargetCategory(targetCat);
    } catch (err) {
      console.error('Error getting recommendations:', err);
      setError('Failed to get recommendations. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            Recommender System
          </h1>
          <p className="text-lg text-gray-600">
            Discover new content based on your preferences
          </p>
        </div>

        {/* Error Message */}
        {error && (
          <div className="max-w-2xl mx-auto mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {/* Recommendation Form */}
        <div className="mb-8">
          <RecommendationForm onSubmit={handleGetRecommendations} loading={loading} />
        </div>

        {/* Recommendations */}
        {recommendations.length > 0 && (
          <div className="mt-8">
            <RecommendationList
              recommendations={recommendations}
              sourceCategory={sourceCategory}
              targetCategory={targetCategory}
            />
          </div>
        )}

        {/* Footer */}
        <div className="mt-12 text-center text-gray-500">
          <p>Built with FastAPI, React, and Machine Learning</p>
        </div>
      </div>
    </div>
  );
}

export default App; 