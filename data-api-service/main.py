import os
from fastapi import FastAPI
from cassandra.cluster import Cluster

app = FastAPI()

# Read the Cassandra host from the environment variable or fallback to 'localhost'
cassandra_host = os.getenv("CASSANDRA_HOST", "localhost")
cluster = Cluster([cassandra_host])
session = cluster.connect("analytics")

@app.get("/events/")
async def get_events():
    rows = session.execute("SELECT * FROM events")
    return [dict(row._asdict()) for row in rows]
