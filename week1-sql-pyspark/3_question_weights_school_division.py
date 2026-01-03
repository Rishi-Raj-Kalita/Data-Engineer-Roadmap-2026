# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.functions import max as _max
from pyspark.sql.window import Window
from datetime import date

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Define schema
students_schema = StructType([
    StructField("school_name", StringType(), nullable=True),
    StructField("student_name", StringType(), nullable=True),
    StructField("weight", IntegerType(), nullable=True)
])

# Data
students_data = [("A", "S1", 30), ("A", "S2", 60), ("B", "S3", 70)]

# Create DataFrame
students_df = spark.createDataFrame(students_data, schema=students_schema)

w1 = Window.partitionBy()
df = students_df.withColumn("total_students", count("*").over(w1))

w2 = Window.partitionBy("school_name")
df = df.withColumn("total_students_by_school",
                   count("*").over(w2)).withColumn("wt_by_school",
                                                   sum("weight").over(w2))

df = df.withColumn(
    "division", ((100.00 * col("total_students_by_school") * col("weight")) /
                 (col("total_students") * col("wt_by_school"))))

df = df.select("school_name", "student_name", "weight", "division")

display(df)
