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
