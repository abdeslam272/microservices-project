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

The container microservices-project-ingestion-service-1 can communicate with microservices-project-kafka-1, meaning they are on the same Docker network, and Docker's internal networking is working fine.

from microservices-project-ingestion-service-1 we can ping microservices-project-zookeeper-1 using network microservices-project_default
from microservices-project-ingestion-service-1 we can not ping microservices-project-cassandra-1
from microservices-project-ingestion-service-1 we can ping microservices-project-kafka-1 using network microservices-project_default
from microservices-project-ingestion-service-1 we can not ping microservices-project-data-api-service-1
from microservices-project-ingestion-service-1 we can not ping microservices-project-processing-service-1

from microservices-project-data-api-service-1 we can not ping microservices-project-zookeeper-1
from microservices-project-data-api-service-1 we can ping microservices-project-cassandra-1 using network microservices-project_kafka_network
from microservices-project-data-api-service-1 we can not ping microservices-project-kafka-1
from microservices-project-data-api-service-1 we can not ping microservices-project-ingestion-service-1
from microservices-project-data-api-service-1 we can ping microservices-project-processing-service-1 using network microservices-project_kafka_network

from microservices-project-processing-service-1 we can not ping microservices-project-zookeeper-1
from microservices-project-processing-service-1 we can ping microservices-project-cassandra-1 using network microservices-project_kafka_network
from microservices-project-processing-service-1 we can not ping microservices-project-kafka-1
from microservices-project-processing-service-1 we can not ping microservices-project-ingestion-service-1
from microservices-project-processing-service-1 we can ping microservices-project-data-api-service-1 using network microservices-project_kafka_network

from microservices-project-kafka-1 we can ping microservices-project-zookeeper-1 using network microservices-project_default
from microservices-project-kafka-1 we can not ping microservices-project-cassandra-1
from microservices-project-kafka-1 we can ping microservices-project-ingestion-service-1 using network microservices-project_default
from microservices-project-kafka-1 we can not ping microservices-project-data-api-service-1
from microservices-project-kafka-1 we can not ping microservices-project-processing-service-1

from microservices-project-zookeeper-1 we can ping microservices-project-kafka-1 using network microservices-project_default
from microservices-project-zookeeper-1 we can not ping microservices-project-cassandra-1
from microservices-project-zookeeper-1 we can ping microservices-project-ingestion-service-1 using network microservices-project_default
from microservices-project-zookeeper-1 we can not ping microservices-project-data-api-service-1
from microservices-project-zookeeper-1 we can not ping microservices-project-processing-service-1

from microservices-project-cassandra-1 we can not ping microservices-project-zookeeper-1
from microservices-project-cassandra-1 we can not ping microservices-project-kafka-1
from microservices-project-cassandra-1 we can not ping microservices-project-ingestion-service-1
from microservices-project-cassandra-1 we can ping microservices-project-data-api-service-1 using network microservices-project_kafka_network
from microservices-project-cassandra-1 we can ping microservices-project-processing-service-1 using network microservices-project_kafka_network



