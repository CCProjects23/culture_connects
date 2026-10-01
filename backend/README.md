# 🔙 Culture Connects – Backend

Django + Django REST Framework. Modularer Monolith mit Domänen-Apps unter
[`apps/`](./apps) (users, profiles, topics, matching, debates, reputation,
moderation, ai) – siehe [ROADMAP.md](../ROADMAP.md) und [AGENT.md](../AGENT.md).

## Setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Konfiguration erfolgt über Umgebungsvariablen aus der Repo-`.env`
(siehe [../.env.example](../.env.example)). Ohne `DATABASE_URL` wird lokal
automatisch SQLite genutzt.

## Entwicklung

```bash
python manage.py migrate
python manage.py runserver
```

- API-Root: http://localhost:8000/api/
- Health-Check: http://localhost:8000/api/health
- Admin (Moderation): http://localhost:8000/admin/

Admin-Benutzer anlegen:

```bash
python manage.py createsuperuser
```

## Struktur

```text
backend/
├── config/        # settings, urls, wsgi/asgi, Health-/API-Views
├── apps/          # Domänen-Apps (modularer Monolith)
├── manage.py
└── requirements.txt
```
