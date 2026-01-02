## SQL Questions

### Question 11: Find Numbers Appearing More Than 3 Times Consecutively

#### Problem Statement

You are given a table containing a sequence of numbers.
Write an SQL query to identify the numbers that appear **atleast 3 times consecutively**.

---

## Database Schema

### Table: NUMBERS

| Column Name | Data Type | Description         |
| ----------- | --------- | ------------------- |
| value       | INT       | Sequence of numbers |

---

## Table Setup

```sql
CREATE TABLE NUMBERS (
    value INT
);
```

---

## Sample Input Data

```sql
INSERT INTO NUMBERS (value) VALUES
(1),
(1),
(2),
(1),
(3),
(3),
(4),
(4),
(4);
```

```python
from pyspark.sql.types import StructType, StructField, IntegerType

# Define schema
numbers_schema = StructType([
    StructField("value", IntegerType(), nullable=True)
])

# Data
numbers_data = [
    (1,),
    (1,),
    (2,),
    (1,),
    (3,),
    (3,),
    (4,),
    (4,),
    (4,)
]

# Create DataFrame
numbers_df = spark.createDataFrame(numbers_data, schema=numbers_schema)
```


---

## NUMBERS Table

| value |
| ----- |
| 1     |
| 1     |
| 2     |
| 1     |
| 3     |
| 3     |
| 4     |
| 4     |
| 4     |

---

## Expected Output

| value |
| ----- |
| 4     |

---

## Requirements

* Identify numbers appearing **more than 3 times consecutively**
* Consider **consecutive order** as per table sequence
* Handle multiple qualifying numbers if present
* Do not rely on hardcoded row positions

