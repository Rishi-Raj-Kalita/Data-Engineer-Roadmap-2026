# SQL Questions

## Question 6: Consecutive Monthly Activity Analysis

### Problem Statement
Write a SQL query to identify users who have been active on the platform for at least three times in a month for 6 such consecutive calendar months. Users meeting this criterion should be selected to receive a bonus sticker.

### Setup

```sql
CREATE TABLE USER_ACTIVITY (
    user_id INT,
    activity_date DATE
);


INSERT INTO USER_ACTIVITY (user_id, activity_date) VALUES
(1, '2024-01-05'),
(1, '2024-01-12'),
(1, '2024-01-20'),
(1, '2024-02-03'),
(1, '2024-02-15'),
(1, '2024-02-28'),
(1, '2024-03-10'),
(1, '2024-03-18'),
(1, '2024-03-25'),
(1, '2024-04-02'),
(1, '2024-04-14'),
(1, '2024-04-22'),
(1, '2024-05-08'),
(1, '2024-05-16'),
(1, '2024-05-30'),
(1, '2024-06-05'),
(1, '2024-06-12'),
(1, '2024-06-25'),

(2, '2024-01-10'),
(2, '2024-01-15'),
(2, '2024-01-25'),
(2, '2024-02-05'),
(2, '2024-02-20'),
(2, '2024-03-08'),
(2, '2024-03-15'),
(2, '2024-04-12'),
(2, '2024-04-18'),
(2, '2024-04-25'),

(3, '2024-01-08'),
(3, '2024-01-16'),
(3, '2024-01-24'),
(3, '2024-02-12'),
(3, '2024-02-18'),
(3, '2024-02-25'),
(3, '2024-03-05'),
(3, '2024-03-20'),
(3, '2024-03-28'),
(3, '2024-04-10'),
(3, '2024-04-15'),
(3, '2024-04-28'),
(3, '2024-05-12'),
(3, '2024-05-20'),
(3, '2024-05-25'),
(3, '2024-06-08'),
(3, '2024-06-18'),
(3, '2024-06-22'),
(3, '2024-07-05'),
(3, '2024-07-15'),
(3, '2024-07-25');

```

```python
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

# Define schema
user_activity_schema = StructType([
    StructField("user_id", IntegerType(), nullable=True),
    StructField("activity_date", DateType(), nullable=True)
])

# Data
user_activity_data = [
    (1, date(2024, 1, 5)), (1, date(2024, 1, 12)), (1, date(2024, 1, 20)),
    (1, date(2024, 2, 3)), (1, date(2024, 2, 15)), (1, date(2024, 2, 28)),
    (1, date(2024, 3, 10)), (1, date(2024, 3, 18)), (1, date(2024, 3, 25)),
    (1, date(2024, 4, 2)), (1, date(2024, 4, 14)), (1, date(2024, 4, 22)),
    (1, date(2024, 5, 8)), (1, date(2024, 5, 16)), (1, date(2024, 5, 30)),
    (1, date(2024, 6, 5)), (1, date(2024, 6, 12)), (1, date(2024, 6, 25)),

    (2, date(2024, 1, 10)), (2, date(2024, 1, 15)), (2, date(2024, 1, 25)),
    (2, date(2024, 2, 5)), (2, date(2024, 2, 20)), (2, date(2024, 3, 8)),
    (2, date(2024, 3, 15)), (2, date(2024, 4, 12)), (2, date(2024, 4, 18)),
    (2, date(2024, 4, 25)),

    (3, date(2024, 1, 8)), (3, date(2024, 1, 16)), (3, date(2024, 1, 24)),
    (3, date(2024, 2, 12)), (3, date(2024, 2, 18)), (3, date(2024, 2, 25)),
    (3, date(2024, 3, 5)), (3, date(2024, 3, 20)), (3, date(2024, 3, 28)),
    (3, date(2024, 4, 10)), (3, date(2024, 4, 15)), (3, date(2024, 4, 28)),
    (3, date(2024, 5, 12)), (3, date(2024, 5, 20)), (3, date(2024, 5, 25)),
    (3, date(2024, 6, 8)), (3, date(2024, 6, 18)), (3, date(2024, 6, 22)),
    (3, date(2024, 7, 5)), (3, date(2024, 7, 15)), (3, date(2024, 7, 25))
]

# Create DataFrame
user_activity_df = spark.createDataFrame(user_activity_data, schema=user_activity_schema)
```





### Database Schema

#### Table: USER_ACTIVITY
| Column Name    | Data Type | Description                    |
|----------------|-----------|--------------------------------|
| user_id        | INT       | Unique identifier for each user|
| activity_date  | DATE      | Date of the user's activity   |

### Sample Input Data

#### USER_ACTIVITY Table
| user_id | activity_date |
|---------|---------------|
| 1       | 2024-01-05    |
| 1       | 2024-01-12    |
| 1       | 2024-01-20    |
| 1       | 2024-02-03    |
| 1       | 2024-02-15    |
| 1       | 2024-02-28    |
| 1       | 2024-03-10    |
| 1       | 2024-03-18    |
| 1       | 2024-03-25    |
| 1       | 2024-04-02    |
| 1       | 2024-04-14    |
| 1       | 2024-04-22    |
| 1       | 2024-05-08    |
| 1       | 2024-05-16    |
| 1       | 2024-05-30    |
| 1       | 2024-06-05    |
| 1       | 2024-06-12    |
| 1       | 2024-06-25    |
| 2       | 2024-01-10    |
| 2       | 2024-01-15    |
| 2       | 2024-01-25    |
| 2       | 2024-02-05    |
| 2       | 2024-02-20    |
| 2       | 2024-03-08    |
| 2       | 2024-03-15    |
| 2       | 2024-04-12    |
| 2       | 2024-04-18    |
| 2       | 2024-04-25    |
| 3       | 2024-01-08    |
| 3       | 2024-01-16    |
| 3       | 2024-01-24    |
| 3       | 2024-02-12    |
| 3       | 2024-02-18    |
| 3       | 2024-02-25    |
| 3       | 2024-03-05    |
| 3       | 2024-03-20    |
| 3       | 2024-03-28    |
| 3       | 2024-04-10    |
| 3       | 2024-04-15    |
| 3       | 2024-04-28    |
| 3       | 2024-05-12    |
| 3       | 2024-05-20    |
| 3       | 2024-05-25    |
| 3       | 2024-06-08    |
| 3       | 2024-06-18    |
| 3       | 2024-06-22    |
| 3       | 2024-07-05    |
| 3       | 2024-07-15    |
| 3       | 2024-07-25    |

### Expected Output

| user_id |
|---------|
| 1       |
| 3       |

### Requirements
- Identify users active at least 3 times per month
- Find 6 consecutive calendar months of such activity
- Return only the user_id of qualifying users
- Consider calendar months (not rolling 30-day periods)