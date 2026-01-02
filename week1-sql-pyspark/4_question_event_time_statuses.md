# SQL Questions

## Question 4: Order Status Timeline Analysis

### Problem Statement
Write a query to track order status changes over time. For each order, show the duration of each status by calculating start and end times for each status period.

### Setup

```sql
CREATE TABLE ORDER_EVENTS (
    event_id   INT PRIMARY KEY,
    order_id   INT,
    status     VARCHAR(20),
    event_time DATE
);

INSERT INTO ORDER_EVENTS (event_id, order_id, status, event_time) VALUES
(1, 1, 'open', '2024-01-01'),
(2, 2, 'open', '2024-01-02'),
(3, 3, 'submitted', '2024-01-03'),
(4, 1, 'open', '2024-01-04'),
(5, 1, 'pending', '2024-01-05'),
(6, 2, 'open', '2024-01-06'),
(7, 2, 'processing', '2024-01-07'),
(8, 3, 'open', '2024-01-08'),
(9, 1, 'open', '2024-01-09'),
(10, 1, 'closed', '2024-01-10'),
(11, 2, 'closed', '2024-01-11'),
(12, 3, 'pending', '2024-01-12');

```

```python
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
order_events_data = [
    (1, 1, "open", date(2024, 1, 1)),
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
    (12, 3, "pending", date(2024, 1, 12))
]

# Create DataFrame
order_events_df = spark.createDataFrame(order_events_data, schema=order_events_schema)
```


### Input Table: ORDER_EVENTS

| Event ID | Order ID | Status  | Event Time |
|----------|----------|---------|------------|
| 1        | 1        | open       | 2024-01-01 |
| 2        | 2        | open       | 2024-01-02 |
| 3        | 3        | submitted  | 2024-01-03 |
| 4        | 1        | open       | 2024-01-04 |
| 5        | 1        | pending    | 2024-01-05 |
| 6        | 2        | open       | 2024-01-06 |
| 7        | 2        | processing | 2024-01-07 |
| 8        | 3        | open       | 2024-01-08 |
| 9        | 1        | open       | 2024-01-09 |
| 10       | 1        | closed     | 2024-01-10 |
| 11       | 2        | closed     | 2024-01-11 |
| 12       | 3        | pending    | 2024-01-12 |

### Expected Output

| Order ID | Status  | Start Time | End Time           |
|----------|---------|------------|--------------------|
| 1        | open       | 2024-01-01 | 2024-01-05         |
| 1        | pending    | 2024-01-05 | 2024-01-09         |
| 1        | open       | 2024-01-09 | 2024-01-10         |
| 1        | closed     | 2024-01-10 | current_timestamp  |
| 2        | open       | 2024-01-02 | 2024-01-07         |
| 2        | processing | 2024-01-07 | 2024-01-11         |
| 2        | closed     | 2024-01-11 | current_timestamp  |
| 3        | submitted  | 2024-01-03 | 2024-01-08         |
| 3        | open       | 2024-01-08 | 2024-01-12         |
| 3        | pending    | 2024-01-12 | current_timestamp  |

### Requirements
- Track status changes for each order over time
- Calculate start time as the first occurrence of each status
- Calculate end time as the start of the next status (or current_timestamp if it's the last status)
- Handle multiple events with the same status for an order
- Show timeline periods for each distinct status phase