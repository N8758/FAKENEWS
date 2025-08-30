import { useState } from "react";
import { predictNews } from "../api/predict";
import type { PredictResponse } from "../api/predict"; // ✅ type-only import

export function usePredict() {
  const [result, setResult] = useState<PredictResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function predict(text: string) {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await predictNews(text);
      setResult(res);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return { predict, result, loading, error };
}
