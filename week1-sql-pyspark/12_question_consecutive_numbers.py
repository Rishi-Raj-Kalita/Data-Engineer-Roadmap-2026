# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Define schema
numbers_schema = StructType(
    [StructField("value", IntegerType(), nullable=True)])

# Data
numbers_data = [(1, ), (1, ), (2, ), (1, ), (3, ), (3, ), (4, ), (4, ), (4, )]

# Create DataFrame
numbers_df = spark.createDataFrame(numbers_data, schema=numbers_schema)

w = Window.orderBy(monotonically_increasing_id())

ordered = numbers_df.withColumn("rn", row_number().over(w)).orderBy("rn")

numbered = ordered.withColumn(
    "is_new_group",
    when(col("value") != coalesce(lag("value").over(w), lit(-1)),
         1).otherwise(0))

w2 = Window.orderBy("rn")
final = numbered.withColumn(
    "g",
    sum("is_new_group").over(w)).groupBy(
        ["g", "value"]).count().filter("count>=3").select("value").distinct()

display(final)
