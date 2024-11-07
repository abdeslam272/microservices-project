# Dockerfile for processing service
FROM bitnami/spark:latest

# Fix missing directories and install CA certificates
RUN mkdir -p /var/lib/apt/lists/partial && apt-get update && apt-get install -y ca-certificates && update-ca-certificates

WORKDIR /app

# Copy the processing script
COPY processing.py /app/

# Run the Spark job with the required packages
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3", "/app/processing.py"]
