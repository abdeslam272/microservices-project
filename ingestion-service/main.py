from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.post("/event/")
async def send_event(event: dict):
    producer.send("clickstream", event)
    return {"status": "event sent"}
