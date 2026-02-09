# Stage 1: build
FROM python:3.10-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.10-slim
WORKDIR /app

# Installer pip et Gunicorn directement dans runtime
RUN pip install --no-cache-dir gunicorn

# Copier packages Python du builder (optionnel si packages dans requirements)
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copier le code source
COPY app/ .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "api:app"]
