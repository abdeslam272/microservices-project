# Dockerfile for data API service
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install fastapi cassandra-driver uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
