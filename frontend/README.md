# 🖥️ Culture Connects – Frontend

React + TypeScript + Vite (SPA). Spricht die Backend-REST-API über
`VITE_API_BASE_URL`.

## Setup

```bash
cd frontend
npm install
cp .env.example .env   # bei Bedarf API-URL anpassen
```

## Entwicklung

```bash
npm run dev      # Dev-Server auf http://localhost:5173
npm run build    # Typecheck + Produktions-Build
npm run lint     # oxlint
npm run preview  # Build lokal ansehen
```

Der Startscreen zeigt den Verbindungsstatus zum Backend-Health-Endpoint
(`/api/health`) – ein schneller Smoke-Test, dass Frontend und Backend
zusammenspielen.

## Struktur

```text
frontend/
├── src/
│   ├── lib/api.ts   # API-Client (Health-Check)
│   ├── App.tsx      # Startscreen + Backend-Status
│   └── main.tsx
├── index.html
└── vite.config.ts
```
