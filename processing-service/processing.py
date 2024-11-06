from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder.appName("StreamProcessor").getOrCreate()
schema = StructType().add("user_id", StringType()).add("event", StringType())

# Consume messages from Kafka topic "clickstream"
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "clickstream") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")
json_df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Processed output to Cassandra (example)
json_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="events", keyspace="analytics") \
    .start()
