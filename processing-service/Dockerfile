# Dockerfile for processing service
FROM bitnami/spark:latest
WORKDIR /app
COPY processing.py /app/
CMD ["spark-submit", "/app/processing.py"]
