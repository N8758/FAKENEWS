// Defines the API response type and function to call backend /predict

export type PredictResponse = {
  label: string;
  confidence: number;
};

export async function predictNews(text: string): Promise<PredictResponse> {
  const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

  const response = await fetch(`${apiUrl}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.statusText}`);
  }

  return response.json() as Promise<PredictResponse>;
}
