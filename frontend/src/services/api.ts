import axios from 'axios';
import { RecommendationRequest, RecommendationResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const recommenderApi = {
  async getCategories() {
    const response = await api.get('/categories');
    return response.data;
  },

  async getRecommendations(request: RecommendationRequest): Promise<RecommendationResponse> {
    const response = await api.post('/recommend', request);
    return response.data;
  },

  async healthCheck() {
    const response = await api.get('/health');
    return response.data;
  },
};

export default api; 