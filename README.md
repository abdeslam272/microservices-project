# Microservices Project

## Overview

This project consists of three main microservices that work together to provide a scalable data processing and analytics solution. Each service has a unique purpose:

1. **Data API Service**: Provides an API interface for interacting with data stored in the Cassandra database, accessible at `http://localhost:8001`.
2. **Ingestion Service**: Responsible for ingesting data from various sources (e.g., Kafka) and storing it in the Cassandra database.
3. **Processing Service**: Utilizes Apache Spark to process large datasets and perform analytics.

## Technologies Used

- **Docker** and **Docker Compose** for containerization and orchestration.
- **Apache Cassandra** for scalable, distributed data storage.
- **Apache Kafka** (if used) for data streaming.
- **Apache Spark** for distributed data processing.
- **Python** (FastAPI) for API development.

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



