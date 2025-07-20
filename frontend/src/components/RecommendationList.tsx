import React from 'react';
import { Star, Calendar, Tag } from 'lucide-react';
import { RecommendationItem } from '../types';

interface RecommendationListProps {
  recommendations: RecommendationItem[];
  sourceCategory: string;
  targetCategory: string;
}

export const RecommendationList: React.FC<RecommendationListProps> = ({
  recommendations,
  sourceCategory,
  targetCategory,
}) => {
  if (recommendations.length === 0) {
    return (
      <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div className="text-center py-8">
          <h3 className="text-lg font-medium text-gray-600 mb-2">No recommendations found</h3>
          <p className="text-gray-500">
            Try adjusting your preferences or selecting different categories.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">
          Recommendations for you
        </h2>
        <p className="text-gray-600">
          Based on your {sourceCategory} preferences, here are some {targetCategory} you might enjoy:
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {recommendations.map((item) => (
          <div
            key={item.id}
            className="bg-gray-50 rounded-lg p-6 border border-gray-200 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between mb-3">
              <h3 className="text-lg font-semibold text-gray-800 line-clamp-2">
                {item.title}
              </h3>
              <div className="flex items-center text-yellow-500 ml-2">
                <Star className="w-4 h-4 fill-current" />
                <span className="ml-1 text-sm font-medium">
                  {item.similarity_score.toFixed(2)}
                </span>
              </div>
            </div>

            {item.description && (
              <p className="text-gray-600 text-sm mb-3 line-clamp-3">
                {item.description}
              </p>
            )}

            <div className="space-y-2">
              {item.genre && (
                <div className="flex items-center text-sm text-gray-500">
                  <Tag className="w-4 h-4 mr-2" />
                  <span>{item.genre}</span>
                </div>
              )}

              {item.year && (
                <div className="flex items-center text-sm text-gray-500">
                  <Calendar className="w-4 h-4 mr-2" />
                  <span>{item.year}</span>
                </div>
              )}

              {item.rating && (
                <div className="flex items-center text-sm text-gray-500">
                  <Star className="w-4 h-4 mr-2" />
                  <span>{item.rating}/5.0</span>
                </div>
              )}
            </div>

            <div className="mt-4 pt-3 border-t border-gray-200">
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-500">Match Score</span>
                <div className="flex items-center">
                  <div className="w-16 bg-gray-200 rounded-full h-2 mr-2">
                    <div
                      className="bg-primary-500 h-2 rounded-full"
                      style={{ width: `${item.similarity_score * 100}%` }}
                    ></div>
                  </div>
                  <span className="text-xs font-medium text-gray-700">
                    {Math.round(item.similarity_score * 100)}%
                  </span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}; 