# SQL Questions

## Question 1: Fill NULL Age Values with Previous Non-NULL Values

### Problem Statement
Write a query to fill each NULL Age value with the most recent non-NULL Age from the previous rows (ordered by ID).

### Setup

```sql
CREATE TABLE EMP (
    Id INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);

INSERT INTO EMP (Id, Name, Age) VALUES
(1, 'Dinesh', 30),
(2, 'Ramesh', 28),
(3, 'Suresh', NULL),
(4, 'Vaibhav', 24),
(5, 'Pallavi', NULL),
(6, 'Mohan', NULL),
(7, 'Anand', 31);
```

```python
# Define schema
emp_schema = StructType([
    StructField("Id", IntegerType(), nullable=False),
    StructField("Name", StringType(), nullable=True),
    StructField("Age", IntegerType(), nullable=True)
])

# Data (equivalent to SQL INSERT statements)
emp_data = [
    (1, "Dinesh", 30),
    (2, "Ramesh", 28),
    (3, "Suresh", None),
    (4, "Vaibhav", 24),
    (5, "Pallavi", None),
    (6, "Mohan", None),
    (7, "Anand", 31)
]

# Create DataFrame
emp_df = spark.createDataFrame(emp_data, schema=emp_schema)
```


### Input Table: EMP

| Id | Name    | Age  |
|----|---------|------|
| 1  | Dinesh  | 30   |
| 2  | Ramesh  | 28   |
| 3  | Suresh  | NULL |
| 4  | Vaibhav | 24   |
| 5  | Pallavi | NULL |
| 6  | Mohan   | NULL |
| 7  | Anand   | 31   |

### Expected Output

| Id | Name    | Age |
|----|---------|-----|
| 1  | Dinesh  | 30  |
| 2  | Ramesh  | 28  |
| 3  | Suresh  | 28  |
| 4  | Vaibhav | 24  |
| 5  | Pallavi | 24  |
| 6  | Mohan   | 24  |
| 7  | Anand   | 31  |

### Requirements
- Fill NULL Age values with the most recent non-NULL Age from previous rows
- Order by ID for processing
- Maintain original data structure