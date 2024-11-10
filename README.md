# Microservices Project

## Overview

This project consists of three main microservices that work together to provide a scalable data processing and analytics solution. Each service has a unique purpose:

1. **Data API Service**: Provides an API interface for interacting with data stored in the Cassandra database, accessible at `http://localhost:8001`.
2. **Ingestion Service**: Responsible for ingesting data from various sources (e.g., Kafka) and storing it in the Cassandra database.
3. **Processing Service**: Utilizes Apache Spark to process large datasets and perform analytics.

## Project Structure

- **`docker-compose.yml`**: Main Docker Compose configuration file that defines the services, networks, and volumes used in the project.
- **`scripts/`**: Contains the `init_cassandra.cql` file to initialize the Cassandra database with a keyspace and table structure.


## Services Overview

The project consists of the following services:

1. **Zookeeper**: Manages and coordinates the Kafka cluster.
2. **Kafka**: Acts as the message broker for streaming data between services.
3. **Cassandra**: Serves as the primary database for storing processed data.
4. **Ingestion Service**: Produces data messages to Kafka.
5. **Processing Service**: Consumes messages from Kafka, processes them, and saves them to Cassandra.
6. **Data API Service**: Provides an HTTP API for querying data stored in Cassandra.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Ensure that ports `2181`, `9092`, `9042`, `8000`, and `8001` are available.

## Setup and Running the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdeslam272/microservices-project.git
   cd microservices-project

## The networks
To enable communication and connectivity checks between containers, install the necessary packages inside each container:
apt-get update
apt-get install -y iputils-ping

To Run Docker Exec with root privileges:
docker exec -u 0 -it <container_name> bash

Network Connectivity Observations:
After testing, the following connectivity was observed between containers:

- microservices-project-ingestion-service-1:

Can ping microservices-project-zookeeper-1 (network: microservices-project_default)
Cannot ping microservices-project-cassandra-1
Can ping microservices-project-kafka-1 (network: microservices-project_default)
Cannot ping microservices-project-data-api-service-1
Cannot ping microservices-project-processing-service-1
- microservices-project-data-api-service-1:

Cannot ping microservices-project-zookeeper-1
Can ping microservices-project-cassandra-1 (network: microservices-project_kafka_network)
Cannot ping microservices-project-kafka-1
Cannot ping microservices-project-ingestion-service-1
Can ping microservices-project-processing-service-1 (network: microservices-project_kafka_network)
- microservices-project-processing-service-1:

Cannot ping microservices-project-zookeeper-1
Can ping microservices-project-cassandra-1 (network: microservices-project_kafka_network)
Cannot ping microservices-project-kafka-1
Cannot ping microservices-project-ingestion-service-1
Can ping microservices-project-data-api-service-1 (network: microservices-project_kafka_network)
- microservices-project-kafka-1:

Can ping microservices-project-zookeeper-1 (network: microservices-project_default)
Cannot ping microservices-project-cassandra-1
Can ping microservices-project-ingestion-service-1 (network: microservices-project_default)
Cannot ping microservices-project-data-api-service-1
Cannot ping microservices-project-processing-service-1
- microservices-project-zookeeper-1:

Can ping microservices-project-kafka-1 (network: microservices-project_default)
Cannot ping microservices-project-cassandra-1
Can ping microservices-project-ingestion-service-1 (network: microservices-project_default)
Cannot ping microservices-project-data-api-service-1
Cannot ping microservices-project-processing-service-1
- microservices-project-cassandra-1:

Cannot ping microservices-project-zookeeper-1
Cannot ping microservices-project-kafka-1
Cannot ping microservices-project-ingestion-service-1
Can ping microservices-project-data-api-service-1 (network: microservices-project_kafka_network)
Can ping microservices-project-processing-service-1 (network: microservices-project_kafka_network)


## Expected Connectivity for the Project
- Zookeeper: Should be accessible only by Kafka.
- Kafka: Should be accessible by:
  Zookeeper (for coordination)
  Ingestion Service (to produce messages)
  Processing Service (to consume messages)
- Cassandra: Should be accessible by:
  Processing Service (to save processed data)
  Data API Service (to read data)
  Ingestion Service: Should be able to communicate with Kafka to publish messages.
- Processing Service: Should be able to:
  Communicate with Kafka (for reading messages)
  Write to Cassandra (to save processed data)
- Data API Service: Should be able to read data from Cassandra.

## Check Cassandra: Access the Cassandra container and verify if the event was inserted:

```bash
docker exec -it microservices-project-cassandra-1 cqlsh


## Run the Query: In the cqlsh shell:

```cql
USE analytics;
SELECT * FROM events;


##  Ensure Data is Being Sent to Kafka
First, we need to confirm that the data is being sent to Kafka and processed correctly by the processing-service. Let's do the following:

Check Kafka Topics:
Make sure Kafka is receiving the events.

```bash
# Enter the Kafka container
docker exec -it microservices-project-kafka-1 /bin/bash

# List Kafka topics to confirm the "clickstream" topic exists
kafka-topics --list --bootstrap-server kafka:9092
