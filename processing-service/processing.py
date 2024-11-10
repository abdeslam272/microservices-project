from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Initialize SparkSession with necessary configurations
spark = SparkSession.builder \
    .appName("StreamProcessor") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

# Define the schema of the incoming data from Kafka
schema = StructType().add("user_id", StringType()).add("event", StringType())

# Consume messages from Kafka topic "clickstream"
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "clickstream") \
    .load()

# Convert Kafka binary value to string
df = df.selectExpr("CAST(value AS STRING)")

# Parse the JSON message
json_df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Write processed data to Cassandra
query = json_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="events", keyspace="analytics") \
    .outputMode("append") \
    .start()

# Wait for the streaming to be processed (it will run indefinitely)
query.awaitTermination()
