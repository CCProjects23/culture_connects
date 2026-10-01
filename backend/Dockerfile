# Culture Connects – Backend (Django)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Dev default; compose overrides the command to run migrations first.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
