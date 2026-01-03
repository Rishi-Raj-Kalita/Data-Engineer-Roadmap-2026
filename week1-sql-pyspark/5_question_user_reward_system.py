# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.functions import max as _max
from pyspark.sql.window import Window
from datetime import date

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# USERS schema
users_schema = StructType([
    StructField("user_id", IntegerType(), nullable=False),
    StructField("user_name", StringType(), nullable=True),
    StructField("registration_date", DateType(), nullable=True)
])

# USERS data
users_data = [(1, "Alice", date(2024, 1, 15)), (2, "Bob", date(2024, 2, 20)),
              (3, "Charlie", date(2024, 3, 10)), (4, "Diana", date(2024, 4,
                                                                   5)),
              (5, "Eve", date(2024, 5, 12))]

users_df = spark.createDataFrame(users_data, schema=users_schema)

# ACTIVITY_LOGS schema
activity_logs_schema = StructType([
    StructField("log_id", IntegerType(), nullable=False),
    StructField("user_id", IntegerType(), nullable=True),
    StructField("activity_date", DateType(), nullable=True),
    StructField("activity_type", StringType(), nullable=True)
])

# ACTIVITY_LOGS data
activity_logs_data = [(1, 1, date(2025, 12, 21), "login"),
                      (2, 1, date(2025, 12, 23), "login"),
                      (3, 1, date(2025, 12, 25), "login"),
                      (4, 2, date(2025, 12, 22), "login"),
                      (5, 2, date(2025, 12, 24), "login"),
                      (6, 3, date(2025, 12, 21), "login"),
                      (7, 3, date(2025, 12, 26), "login"),
                      (8, 4, date(2025, 12, 23), "login"),
                      (9, 5, date(2025, 12, 25), "login"),
                      (10, 1, date(2025, 12, 26), "login"),
                      (11, 1, date(2025, 12, 27), "login"),
                      (12, 1, date(2025, 12, 28), "login"),
                      (13, 1, date(2025, 12, 29), "login")]

activity_logs_df = spark.createDataFrame(activity_logs_data,
                                         schema=activity_logs_schema)

# TRANSACTIONS schema
transactions_schema = StructType([
    StructField("transaction_id", IntegerType(), nullable=False),
    StructField("user_id", IntegerType(), nullable=True),
    StructField("transaction_date", DateType(), nullable=True),
    StructField("amount", IntegerType(), nullable=True)
])

# TRANSACTIONS data
transactions_data = [(1, 1, date(2025, 12, 22), 150),
                     (2, 1, date(2025, 12, 24), 200),
                     (3, 2, date(2025, 12, 23), 75),
                     (4, 2, date(2025, 12, 25), 300),
                     (5, 3, date(2025, 12, 21), 600),
                     (6, 4, date(2025, 12, 24), 1200),
                     (7, 5, date(2025, 12, 26), 50)]

transactions_df = spark.createDataFrame(transactions_data,
                                        schema=transactions_schema)

login_metrics_df = activity_logs_df.filter(col("activity_date")>= date_sub(current_date(), 30))\
.groupBy("user_id").count().withColumnRenamed("count", "login_counts")


transaction_metrics_df = transactions_df.filter(col("transaction_date")>= date_sub(current_date(), 30))\
.groupBy("user_id").agg(sum("amount").alias("total_transactions"))


user_metrics_df = users_df.alias("u").join(login_metrics_df.alias("l"), col("u.user_id")==col("l.user_id"), "left")\
.join(transaction_metrics_df.alias("t"), col("t.user_id")==col("u.user_id"))


final_df = user_metrics_df.withColumn("tier", when((col("login_counts")>=20) & (col("total_transactions")>=1000),"Gold")
                                     .when((col("login_counts")>=10) & (col("total_transactions")>=500),"Silver")
                                     .when((col("login_counts")>=5) & (col("total_transactions")>=100),"Bronze").otherwise(None))\
.filter(col("tier").isNotNull())

final_df = final_df.orderBy(
    when(col("tier") == "Gold", 1).when(col("tier") == "Silver",
                                        2).when(col("tier") == "Bronze", 3),
    col("user_name"))

display(final_df)
