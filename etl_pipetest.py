import os
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("DataLakeImplementation") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Read data directly from HDFS using Spark's built-in DataFrameReader
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("hdfs://namenode:8020/hdfs/path/to/data")

# Perform batch processing (example: simple transformation)
df_transformed = df.withColumnRenamed("old_column_name", "new_column_name")

# Save the transformed data back to HDFS
df_transformed.write.mode("overwrite").parquet(f"/hdfs/path/to/data/transformed")

# Create Hive table and run interactive queries
spark.sql("""
    CREATE EXTERNAL TABLE IF NOT EXISTS your_table_name (
        column1 STRING,
        column2 INT,
        ...
    )
    STORED AS PARQUET
    LOCATION '/hdfs/path/to/data/transformed'
""")

# Example query
result = spark.sql("SELECT * FROM your_table_name")
result.show()

# Stop the Spark session
spark.stop()
