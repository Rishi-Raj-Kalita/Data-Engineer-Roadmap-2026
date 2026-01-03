# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.sql.functions import *
from pyspark.sql.functions import max as _max
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

employee_schema = StructType([
    StructField("emp_id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=True),
    StructField("salary", IntegerType(), nullable=True),
    StructField("department_name", StringType(), nullable=True)
])

# Data
employee_data = [(1, "Alice", 60000, "Engineering"),
                 (2, "Bob", 50000, "Engineering"), (3, "Charlie", 40000, "HR"),
                 (4, "Diana", 45000, "HR"), (5, "Eve", 70000, "Sales")]

# Create DataFrame
employee_df = spark.createDataFrame(employee_data, schema=employee_schema)

department_avg_salary = employee_df.groupBy("department_name").agg(
    avg(col("salary")).alias("avg_salary"))

max_department_avg_salary_df = department_avg_salary.agg(
    _max("avg_salary").alias("max_avg_salary"))

max_department_avg_salary_value = max_department_avg_salary_df.collect(
)[0]["max_avg_salary"]

final_df = department_avg_salary.filter(
    col("avg_salary") == max_department_avg_salary_value)

display(final_df)
