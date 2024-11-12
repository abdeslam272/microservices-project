from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType
import logging

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

# Log schema for debugging purposes
logger.info("Schema of the incoming data:")
json_df.printSchema()

# Write processed data to Cassandra with improved error handling and logging
try:
    query = json_df.writeStream \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="events", keyspace="analytics") \
        .outputMode("append") \
        .foreachBatch(lambda batch_df, batch_id: process_batch(batch_df, batch_id)) \
        .start()

    # Wait for the streaming to be processed (it will run indefinitely)
    query.awaitTermination()

except Exception as e:
    logger.error(f"Error occurred during streaming: {str(e)}")
    raise

# Function to process batches before writing to Cassandra (for better error handling)
def process_batch(batch_df, batch_id):
    try:
        # Verify that the schema is correct and matches Cassandra's schema
        logger.info(f"Processing batch {batch_id} with {batch_df.count()} records")

        # You could perform data validation here if needed, like checking for nulls or incorrect data types
        if batch_df.isEmpty():
            logger.warning(f"Batch {batch_id} is empty, skipping write.")
        else:
            # Write the data to Cassandra table
            batch_df.write \
                .format("org.apache.spark.sql.cassandra") \
                .options(table="events", keyspace="analytics") \
                .mode("append") \
                .save()
            logger.info(f"Batch {batch_id} written successfully to Cassandra.")

    except Exception as batch_error:
        logger.error(f"Error processing batch {batch_id}: {str(batch_error)}")
