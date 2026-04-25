FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir flask gunicorn

COPY app/ ./app/
COPY run.py .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "60", "run:app"]
