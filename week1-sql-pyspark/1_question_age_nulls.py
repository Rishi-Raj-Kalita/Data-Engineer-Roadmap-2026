# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

emp_schema = StructType([
    StructField("Id", IntegerType(), nullable=False),
    StructField("Name", StringType(), nullable=True),
    StructField("Age", IntegerType(), nullable=True)
])

# Data (equivalent to SQL INSERT statements)
emp_data = [(1, "Dinesh", 30), (2, "Ramesh", 28), (3, "Suresh", None),
            (4, "Vaibhav", 24), (5, "Pallavi", None), (6, "Mohan", None),
            (7, "Anand", 31)]

# Create DataFrame
emp_df = spark.createDataFrame(emp_data, schema=emp_schema)

w = Window.orderBy("id")

ordered_df = emp_df.withColumn("is_new_group",
                               when(col("age").isNull(), 0).otherwise(1))

grouped_df = ordered_df.withColumn("g", sum("is_new_group").over(w))

w2 = Window.partitionBy("g").orderBy("id")

final_df = grouped_df.withColumn("new_age",
                                 first_value("age").over(w2)).select(
                                     ["id", "name", "new_age"])

display(final_df)
