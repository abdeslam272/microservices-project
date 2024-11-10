# Use Bitnami's Spark base image as your starting point
FROM bitnami/spark:latest

# Set environment variables for Spark, Scala, and Kafka versions
ENV SPARK_VERSION=3.5.3
ENV SCALA_VERSION=2.12
ENV KAFKA_VERSION=0.10
ENV CASSANDRA_HOST=cassandra

# Switch to root user to install necessary packages
USER root

# Install the Spark Cassandra connector (for reading/writing to Cassandra)
RUN /opt/bitnami/spark/bin/spark-shell \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.0 \
    --conf "spark.jars.ivy=/tmp/.ivy2/" \
    --conf "spark.jars.repositories=https://repo1.maven.org/maven2,https://repos.spark-packages.org/" \
    -i /dev/null || true

# Switch back to the default non-root user
USER 1001

# Copy your application code into the container
COPY . /app
WORKDIR /app

# Set the default command to start the Spark job
CMD ["/opt/bitnami/scripts/spark/run.sh"]
