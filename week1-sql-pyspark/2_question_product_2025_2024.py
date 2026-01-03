# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.functions import max as _max
from pyspark.sql.window import Window
from datetime import date

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

sales_schema = StructType([
    StructField("Product_ID", IntegerType(), nullable=True),
    StructField("Date", DateType(), nullable=True),
    StructField("Sales", IntegerType(), nullable=True)
])

# Data
sales_data = [(1, date(2024, 10, 12), 100), (2, date(2025, 1, 25), 200),
              (2, date(2024, 8, 1), 300), (3, date(2024, 1, 12), 150),
              (3, date(2025, 2, 12), 200), (5, date(2025, 3, 12), 250),
              (2, date(2024, 3, 12), 350), (1, date(2025, 5, 12), 120),
              (5, date(2025, 6, 12), 260)]

# Create DataFrame
sales_df = spark.createDataFrame(sales_data, schema=sales_schema)

df = sales_df.withColumn("year", date_format(col("date"), "yyyy"))

df_a = df.filter("year=2024").groupBy("product_id").agg(
    sum(col("sales")).alias("sales_a"))
df_b = df.filter("year=2025").groupBy("product_id").agg(
    sum(col("sales")).alias("sales_b"))

df_final = df_a.alias("a").join(df_b.alias("b"), df_a["product_id"]==df_b["product_id"], "fullouter")\
.select(coalesce("a.product_id", "b.product_id").alias("product_id"), col("sales_a").alias("sales_2024"),
                                                                                               col("sales_b").alias("sales_2025"))

display(df_final)
