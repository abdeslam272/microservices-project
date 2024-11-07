# Dockerfile for processing service
FROM bitnami/spark:latest
WORKDIR /app
COPY processing.py /app/
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3", "/app/processing.py"]
