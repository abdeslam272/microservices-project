from fastapi import FastAPI
from cassandra.cluster import Cluster

app = FastAPI()
cluster = Cluster(["cassandra"])
session = cluster.connect("analytics")

@app.get("/events/")
async def get_events():
    rows = session.execute("SELECT * FROM events")
    return [dict(row._asdict()) for row in rows]
