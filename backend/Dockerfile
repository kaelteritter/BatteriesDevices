FROM python:3.11-slim

WORKDIR /app


COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY backend/ .

# Запуск: миграции + сервер
CMD ["sh", "-c", "alembic upgrade head && fastapi dev app/main.py --host 0.0.0.0 --port 8000"]