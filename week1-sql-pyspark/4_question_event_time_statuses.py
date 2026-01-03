# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.functions import max as _max
from pyspark.sql.window import Window
from datetime import date

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

# Define schema
order_events_schema = StructType([
    StructField("event_id", IntegerType(), nullable=False),
    StructField("order_id", IntegerType(), nullable=True),
    StructField("status", StringType(), nullable=True),
    StructField("event_time", DateType(), nullable=True)
])

# Data
order_events_data = [(1, 1, "open", date(2024, 1, 1)),
                     (2, 2, "open", date(2024, 1, 2)),
                     (3, 3, "submitted", date(2024, 1, 3)),
                     (4, 1, "open", date(2024, 1, 4)),
                     (5, 1, "pending", date(2024, 1, 5)),
                     (6, 2, "open", date(2024, 1, 6)),
                     (7, 2, "processing", date(2024, 1, 7)),
                     (8, 3, "open", date(2024, 1, 8)),
                     (9, 1, "open", date(2024, 1, 9)),
                     (10, 1, "closed", date(2024, 1, 10)),
                     (11, 2, "closed", date(2024, 1, 11)),
                     (12, 3, "pending", date(2024, 1, 12))]

# Create DataFrame
order_events_df = spark.createDataFrame(order_events_data,
                                        schema=order_events_schema)

w = Window.partitionBy(col("order_id")).orderBy(col("event_time"))

changed_events_df = order_events_df.withColumn("is_change", when((col("status") != lag("status").over(w))
                                                                   | (lag(col("status")).over(w).isNull()) ,1).otherwise(0))\
.orderBy(["order_id", "event_time"])

ordered_events_df = changed_events_df.withColumn("grp",
                                                 sum("is_change").over(w))

grouped_events_df = ordered_events_df.groupBy(
    ["order_id", "status",
     "grp"]).agg(min(col("event_time")).alias("event_time"))

final_df = grouped_events_df.withColumn(
    "changed_date", coalesce(lead("event_time").over(w),
                             current_date())).orderBy("order_id", "event_time")
display(final_df)
