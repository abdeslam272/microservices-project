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
- 
## to start the containers:
docker-compose up -d

## to start a spark shell with the container processing-service:
spark-shell --conf spark.jars.ivy=/tmp/.ivy

## Check Cassandra: Access the Cassandra container and verify if the event was inserted

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



## Project Overview
Ingestion Service (ingestion-service):

This service provides an API to ingest event data via HTTP requests. When an event is posted to this service, it sends the data to Kafka’s clickstream topic.
Technology: FastAPI (for API handling) and kafka-python (for Kafka integration).
Kafka:

Acts as the message broker to store and distribute the incoming events.
The ingestion service sends events to Kafka, and the processing service consumes them from Kafka to process further.
Processing Service (processing-service):

This service uses Spark to read events from the clickstream Kafka topic, processes the data in real time, and writes the results to Cassandra.
Spark processes each event, parses it, and stores it in a Cassandra table within the analytics keyspace.
Data API Service (data-api-service):

Provides an API to query processed data stored in Cassandra.
This allows you to retrieve stored events by making HTTP requests to this service, making it easy to view or analyze processed data.
Cassandra:

Stores the processed events in a table within a keyspace called analytics. The table events stores event details, allowing you to query data for further analysis or display.




Testing the Project
Here’s how to test each component and ensure that data flows correctly through the pipeline:

Start All Services:

Run docker-compose up -d --build to start all services in the background.
Ensure that all containers are up by checking docker-compose ps.
Verify Cassandra Initialization:

Cassandra should automatically create the analytics keyspace and events table upon startup, using the script in scripts/init_cassandra.cql.
To confirm, log into Cassandra with:
bash
Copier le code
docker exec -it <cassandra_container_id> cqlsh
Run DESCRIBE keyspaces; and USE analytics; to verify that the events table exists.
Test the Ingestion Service:

Send an event to the ingestion service to simulate real-time data ingestion:
bash
Copier le code
curl -X POST "http://localhost:8000/event/" -H "Content-Type: application/json" -d '{"user_id": "user123", "event": "page_view"}'
This should send the event to the clickstream topic in Kafka.
Check Kafka for Incoming Messages:

Verify that the event was added to Kafka’s clickstream topic:
Steps to Access the Kafka Container with PowerShell
Open PowerShell and ensure it’s running with appropriate permissions.

Run the following command to access the Kafka container using PowerShell’s path syntax:

powershell
Copier le code
docker exec -it microservices-project-kafka-1 sh
If your Kafka container image uses a Unix-based OS, sh should be available even if bash is not.

Once inside, locate the Kafka consumer script:

sh
Copier le code
ls /opt/bitnami/kafka/bin
Run the Kafka console consumer from within the container, using the correct path:

sh
Copier le code
./kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic clickstream --from-beginning

'''sh
cd /opt/bitnami/kafka/bin
./kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic clickstream --from-beginning

----------
Verify Spark Processing:

The processing-service should automatically consume messages from Kafka, process them, and store them in Cassandra.
Check logs for processing-service to ensure it’s reading from Kafka and writing to Cassandra:
bash
Copier le code
docker-compose logs processing-service
Look for messages indicating that the data is being processed and stored.
Test the Data API Service:

Once the data is processed and stored in Cassandra, you can retrieve it using the data API service:
bash

curl -X GET "http://localhost:8001/events/"
This should return a JSON response with the processed events from the events table in Cassandra.
Summary
Ingestion Service receives events and sends them to Kafka.
Kafka holds the events until they’re consumed.
Processing Service (Spark) consumes events from Kafka, processes them, and writes the output to Cassandra.
Data API Service provides a way to retrieve the stored, processed events from Cassandra.
Each service works together to form a complete pipeline for ingesting, processing, and accessing real-time event data. This setup is typical for a real-time analytics system, where data flows from ingestion, through processing, to storage, and finally, to API-based querying.
