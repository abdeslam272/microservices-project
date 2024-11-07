# Dockerfile for processing service
FROM bitnami/spark:latest

# Switch to root user for installing ca-certificates
USER root

# Fix missing directories and install CA certificates
RUN mkdir -p /var/lib/apt/lists/partial && apt-get update && apt-get install -y ca-certificates && update-ca-certificates

# Switch back to the default user (spark or identified user)
USER spark  

WORKDIR /app

# Copy the processing script
COPY processing.py /app/

# Run the Spark job with the required packages
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3", "/app/processing.py"]
