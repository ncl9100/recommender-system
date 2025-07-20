export interface RecommendationItem {
  id: string;
  title: string;
  description?: string;
  genre?: string;
  rating?: number;
  year?: number;
  similarity_score: number;
  metadata: Record<string, any>;
}

export interface RecommendationRequest {
  source_category: string;
  target_category: string;
  preferences: string[];
  limit: number;
}

export interface RecommendationResponse {
  recommendations: RecommendationItem[];
  source_category: string;
  target_category: string;
  total_count: number;
}

export interface Category {
  name: string;
  displayName: string;
  description: string;
} 