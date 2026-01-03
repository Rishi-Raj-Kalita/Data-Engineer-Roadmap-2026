# SQL Questions

## Question 5: Tiered Reward System Analysis

### Problem Statement
Write an SQL query to identify users who qualify for a tiered reward system. The system is based on both the frequency of logins and the amount spent on the platform within the last 30 days.

### Setup

```sql
CREATE TABLE USERS (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    registration_date DATE
);

CREATE TABLE ACTIVITY_LOGS (
    log_id INT PRIMARY KEY,
    user_id INT,
    activity_date DATE,
    activity_type VARCHAR(20)
);

CREATE TABLE TRANSACTIONS (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    transaction_date DATE,
    amount DECIMAL(10, 2)
);


INSERT INTO USERS (user_id, user_name, registration_date) VALUES
(1, 'Alice', '2024-01-15'),
(2, 'Bob', '2024-02-20'),
(3, 'Charlie', '2024-03-10'),
(4, 'Diana', '2024-04-05'),
(5, 'Eve', '2024-05-12');


INSERT INTO ACTIVITY_LOGS (log_id, user_id, activity_date, activity_type) VALUES
(1, 1, '2025-12-21', 'login'),
(2, 1, '2025-12-23', 'login'),
(3, 1, '2025-12-25', 'login'),
(4, 2, '2025-12-22', 'login'),
(5, 2, '2025-12-24', 'login'),
(6, 3, '2025-12-21', 'login'),
(7, 3, '2025-12-26', 'login'),
(8, 4, '2025-12-23', 'login'),
(9, 5, '2025-12-25', 'login'),
(10, 1, '2025-12-26', 'login'),
(11, 1, '2025-12-27', 'login'),
(12, 1, '2025-12-28', 'login'),
(13, 1, '2025-12-29', 'login');


INSERT INTO TRANSACTIONS (transaction_id, user_id, transaction_date, amount) VALUES
(1, 1, '2025-12-22', 150.00),
(2, 1, '2025-12-24', 200.00),
(3, 2, '2025-12-23', 75.00),
(4, 2, '2025-12-25', 300.00),
(5, 3, '2025-12-21', 600.00),
(6, 4, '2025-12-24', 1200.00),
(7, 5, '2025-12-26', 50.00);

```

```python
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DateType, DecimalType
)
from datetime import date

# USERS schema
users_schema = StructType([
    StructField("user_id", IntegerType(), nullable=False),
    StructField("user_name", StringType(), nullable=True),
    StructField("registration_date", DateType(), nullable=True)
])

# USERS data
users_data = [
    (1, "Alice", date(2024, 1, 15)),
    (2, "Bob", date(2024, 2, 20)),
    (3, "Charlie", date(2024, 3, 10)),
    (4, "Diana", date(2024, 4, 5)),
    (5, "Eve", date(2024, 5, 12))
]

users_df = spark.createDataFrame(users_data, schema=users_schema)


# ACTIVITY_LOGS schema
activity_logs_schema = StructType([
    StructField("log_id", IntegerType(), nullable=False),
    StructField("user_id", IntegerType(), nullable=True),
    StructField("activity_date", DateType(), nullable=True),
    StructField("activity_type", StringType(), nullable=True)
])

# ACTIVITY_LOGS data
activity_logs_data = [
    (1, 1, date(2025, 12, 21), "login"),
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
    (13, 1, date(2025, 12, 29), "login")
]

activity_logs_df = spark.createDataFrame(activity_logs_data, schema=activity_logs_schema)


# TRANSACTIONS schema
transactions_schema = StructType([
    StructField("transaction_id", IntegerType(), nullable=False),
    StructField("user_id", IntegerType(), nullable=True),
    StructField("transaction_date", DateType(), nullable=True),
    StructField("amount", IntegerType(), nullable=True)
])

# TRANSACTIONS data
transactions_data = [
    (1, 1, date(2025, 12, 22), 150),
    (2, 1, date(2025, 12, 24), 200),
    (3, 2, date(2025, 12, 23), 75),
    (4, 2, date(2025, 12, 25), 300),
    (5, 3, date(2025, 12, 21), 600),
    (6, 4, date(2025, 12, 24), 1200),
    (7, 5, date(2025, 12, 26), 50)
]

transactions_df = spark.createDataFrame(transactions_data, schema=transactions_schema)
```


### Database Schema

#### Table 1: USERS
| Column Name       | Data Type | Description                    |
|-------------------|-----------|--------------------------------|
| user_id           | INT       | Primary Key - User identifier  |
| user_name         | VARCHAR   | Name of the user              |
| registration_date | DATE      | User registration date        |

#### Table 2: ACTIVITY_LOGS
| Column Name    | Data Type | Description                           |
|----------------|-----------|---------------------------------------|
| log_id         | INT       | Primary Key - Log entry identifier   |
| user_id        | INT       | Foreign Key - User identifier        |
| activity_date  | DATE      | Date of the activity                 |
| activity_type  | VARCHAR   | Type of activity (login, purchase)  |

#### Table 3: TRANSACTIONS
| Column Name      | Data Type | Description                        |
|------------------|-----------|----------------------------------- |
| transaction_id   | INT       | Primary Key - Transaction identifier|
| user_id          | INT       | Foreign Key - User identifier      |
| transaction_date | DATE      | Date of the transaction            |
| amount           | DECIMAL   | Transaction amount in USD          |

### Sample Data

#### USERS Table
| user_id | user_name | registration_date |
|---------|-----------|-------------------|
| 1       | Alice     | 2024-01-15        |
| 2       | Bob       | 2024-02-20        |
| 3       | Charlie   | 2024-03-10        |
| 4       | Diana     | 2024-04-05        |
| 5       | Eve       | 2024-05-12        |

#### ACTIVITY_LOGS Table
| log_id | user_id | activity_date | activity_type |
|--------|---------|---------------|---------------|
| 1      | 1       | 2025-12-21    | login         |
| 2      | 1       | 2025-12-23    | login         |
| 3      | 1       | 2025-12-25    | login         |
| 4      | 2       | 2025-12-22    | login         |
| 5      | 2       | 2025-12-24    | login         |
| 6      | 3       | 2025-12-21    | login         |
| 7      | 3       | 2025-12-26    | login         |
| 8      | 4       | 2025-12-23    | login         |
| 9      | 5       | 2025-12-25    | login         |

#### TRANSACTIONS Table
| transaction_id | user_id | transaction_date | amount |
|----------------|---------|------------------|--------|
| 1              | 1       | 2025-12-22       | 150.00 |
| 2              | 1       | 2025-12-24       | 200.00 |
| 3              | 2       | 2025-12-23       | 75.00  |
| 4              | 2       | 2025-12-25       | 300.00 |
| 5              | 3       | 2025-12-21       | 600.00 |
| 6              | 4       | 2025-12-24       | 1200.00|
| 7              | 5       | 2025-12-26       | 50.00  |

### Reward Tier Criteria (Last 30 Days)
- **Bronze**: Logged in at least 5 times AND spent over $100
- **Silver**: Logged in at least 10 times AND spent over $500  
- **Gold**: Logged in at least 20 times AND spent over $1000

### Expected Output Columns
- user_id
- user_name  
- reward_tier (Bronze, Silver, Gold)

### Requirements
- Calculate login frequency and total spending within the last 30 days
- Assign highest qualifying tier to each user
- Rank users by highest tier first, then alphabetically by name within each tier
- Only include users who qualify for at least one tier