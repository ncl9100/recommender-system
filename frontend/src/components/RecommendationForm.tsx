import React, { useState } from 'react';
import { BookOpen, Film, Music, Gamepad2 } from 'lucide-react';
import { Category } from '../types';

interface RecommendationFormProps {
  onSubmit: (sourceCategory: string, targetCategory: string, preferences: string[]) => void;
  loading: boolean;
}

const categories: Category[] = [
  { name: 'books', displayName: 'Books', description: 'Literature and novels' },
  { name: 'movies', displayName: 'Movies', description: 'Films and TV shows' },
  { name: 'songs', displayName: 'Songs', description: 'Music and audio' },
  { name: 'games', displayName: 'Games', description: 'Video games and interactive media' },
];

const categoryIcons = {
  books: BookOpen,
  movies: Film,
  songs: Music,
  games: Gamepad2,
};

export const RecommendationForm: React.FC<RecommendationFormProps> = ({ onSubmit, loading }) => {
  const [sourceCategory, setSourceCategory] = useState('books');
  const [targetCategory, setTargetCategory] = useState('movies');
  const [preferences, setPreferences] = useState<string[]>([]);
  const [preferenceInput, setPreferenceInput] = useState('');

  const handleAddPreference = () => {
    if (preferenceInput.trim()) {
      setPreferences([...preferences, preferenceInput.trim()]);
      setPreferenceInput('');
    }
  };

  const handleRemovePreference = (index: number) => {
    setPreferences(preferences.filter((_, i) => i !== index));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const validPreferences = preferences.filter(p => p.trim());
    if (validPreferences.length > 0) {
      onSubmit(sourceCategory, targetCategory, validPreferences);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold text-gray-800 mb-6">Get Recommendations</h2>
      
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Source Category */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            I like these (source category):
          </label>
          <div className="grid grid-cols-2 gap-3">
            {categories.map((category) => {
              const Icon = categoryIcons[category.name as keyof typeof categoryIcons];
              return (
                <button
                  key={category.name}
                  type="button"
                  onClick={() => setSourceCategory(category.name)}
                  className={`p-4 rounded-lg border-2 transition-colors ${
                    sourceCategory === category.name
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <Icon className="w-6 h-6 mx-auto mb-2" />
                  <div className="text-sm font-medium">{category.displayName}</div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Target Category */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Recommend me (target category):
          </label>
          <div className="grid grid-cols-2 gap-3">
            {categories.map((category) => {
              const Icon = categoryIcons[category.name as keyof typeof categoryIcons];
              return (
                <button
                  key={category.name}
                  type="button"
                  onClick={() => setTargetCategory(category.name)}
                  className={`p-4 rounded-lg border-2 transition-colors ${
                    targetCategory === category.name
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <Icon className="w-6 h-6 mx-auto mb-2" />
                  <div className="text-sm font-medium">{category.displayName}</div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Preferences */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Your preferences:
          </label>
          <div className="space-y-3">
            {preferences.map((pref, index) => (
              <div key={index} className="flex gap-2">
                <input
                  type="text"
                  value={pref}
                  onChange={(e) => {
                    const newPrefs = [...preferences];
                    newPrefs[index] = e.target.value;
                    setPreferences(newPrefs);
                  }}
                  placeholder={`Enter your favorite ${sourceCategory}...`}
                  className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
                />
                <button
                  type="button"
                  onClick={() => handleRemovePreference(index)}
                  className="px-3 py-2 text-red-600 hover:text-red-800"
                >
                  Remove
                </button>
              </div>
            ))}
            
            <div className="flex gap-2">
              <input
                type="text"
                value={preferenceInput}
                onChange={(e) => setPreferenceInput(e.target.value)}
                placeholder={`Add a ${sourceCategory} preference...`}
                className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
              <button
                type="button"
                onClick={handleAddPreference}
                className="px-4 py-2 bg-primary-500 text-white rounded-md hover:bg-primary-600"
              >
                Add
              </button>
            </div>
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={loading || preferences.filter(p => p.trim()).length === 0}
          className="w-full py-3 px-4 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Getting Recommendations...' : 'Get Recommendations'}
        </button>
      </form>
    </div>
  );
}; 