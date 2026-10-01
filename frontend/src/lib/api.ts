/** Tiny API client for the Culture Connects backend. */

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api";

export interface HealthResponse {
  status: string;
  service: string;
  debug: boolean;
}

export async function fetchHealth(): Promise<HealthResponse> {
  const response = await fetch(`${API_BASE_URL}/health`, {
    headers: { Accept: "application/json" },
  });
  if (!response.ok) {
    throw new Error(`Backend responded with ${response.status}`);
  }
  return (await response.json()) as HealthResponse;
}

export { API_BASE_URL };
