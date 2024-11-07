# Use Bitnami's Spark base image as your starting point
FROM bitnami/spark:latest

# Set environment variables
ENV SPARK_VERSION=3.5.3
ENV SCALA_VERSION=2.12
ENV KAFKA_VERSION=0.10

# Switch to root user to gain permissions for installing packages
USER root

# Add Kafka dependency for Spark (this setup is better at runtime)
RUN mkdir -p /tmp/.ivy2 && \
    /opt/bitnami/spark/bin/spark-shell \
    --packages org.apache.spark:spark-sql-kafka-0-10_${SCALA_VERSION}:${SPARK_VERSION} \
    --conf "spark.jars.ivy=/tmp/.ivy2/" \
    --conf "spark.jars.repositories=https://repo1.maven.org/maven2,https://repos.spark-packages.org/" \
    -i /dev/null || true

# Switch back to the default non-root user
USER 1001

# Copy your application code
COPY . /app
WORKDIR /app

# Set the default command to start Spark
CMD ["/opt/bitnami/scripts/spark/run.sh"]
