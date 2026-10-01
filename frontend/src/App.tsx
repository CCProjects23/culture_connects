import { useEffect, useState } from "react";
import { API_BASE_URL, fetchHealth } from "./lib/api";
import "./App.css";

type BackendState =
  | { kind: "loading" }
  | { kind: "ok"; service: string }
  | { kind: "error"; message: string };

function App() {
  const [backend, setBackend] = useState<BackendState>({ kind: "loading" });

  useEffect(() => {
    fetchHealth()
      .then((data) => setBackend({ kind: "ok", service: data.service }))
      .catch((error: unknown) =>
        setBackend({
          kind: "error",
          message: error instanceof Error ? error.message : "unknown error",
        }),
      );
  }, []);

  return (
    <main className="app">
      <h1>🌐 Culture Connects</h1>
      <p className="tagline">
        Strukturierte Debatten mit KI-gestützter Reflexion.
      </p>

      <section className="status-card">
        <h2>Backend-Verbindung</h2>
        {backend.kind === "loading" && <p>Prüfe Verbindung …</p>}
        {backend.kind === "ok" && (
          <p className="ok">✅ Verbunden mit {backend.service}</p>
        )}
        {backend.kind === "error" && (
          <p className="error">❌ Keine Verbindung: {backend.message}</p>
        )}
        <code>{API_BASE_URL}</code>
      </section>
    </main>
  );
}

export default App;
