FROM python:3.10-slim

WORKDIR /app

# Кэшируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY app/ ./app/
COPY run.py .

# Render автоматически передаёт PORT, фоллбэк для локалки
ENV PORT=8000
EXPOSE 8000

# Shell-форма CMD нужна для подстановки $PORT из окружения Render
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 1 --timeout 60 run:app"]
