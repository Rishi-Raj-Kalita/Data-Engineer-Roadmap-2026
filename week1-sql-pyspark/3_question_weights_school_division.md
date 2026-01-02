# SQL Questions

## Question 3: School Food Distribution System

### Problem Statement
There are few schools in the city. The mid day meal kitchen prepares 100 kgs of food. The food has to be divided among schools according to the number of students in the school. The school further distributes the food according to the weight of each student.

### Setup

```sql
CREATE TABLE STUDENTS (
    school_name   VARCHAR(10),
    student_name  VARCHAR(10),
    weight        INT
);

INSERT INTO STUDENTS (school_name, student_name, weight) VALUES
('A', 'S1', 30),
('A', 'S2', 60),
('B', 'S3', 70);
```

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define schema
students_schema = StructType([
    StructField("school_name", StringType(), nullable=True),
    StructField("student_name", StringType(), nullable=True),
    StructField("weight", IntegerType(), nullable=True)
])

# Data
students_data = [
    ("A", "S1", 30),
    ("A", "S2", 60),
    ("B", "S3", 70)
]

# Create DataFrame
students_df = spark.createDataFrame(students_data, schema=students_schema)
```


### Input Table: STUDENTS

| school_name | student_name | weight |
|-------------|--------------|--------|
| A           | S1           | 30     |
| A           | S2           | 60     |
| B           | S3           | 70     |

### Distribution Logic
1. **School Level**: Food is distributed to schools based on student count
2. **Student Level**: Within each school, food is distributed based on student weight

### Expected Output Example

| school_name | student_name | weight | food_allocated |
|-------------|--------------|--------|----------------|
| A           | S1           | 30     | 22.22          |
| A           | S2           | 60     | 44.45          |
| B           | S3           | 70     | 33.33          |

### Calculation Breakdown
- **School A**: 2 students → gets 66.66 kg (2/3 of total food)
  - S1: 30 kg weight → gets 22.22 kg (30/90 of school A's allocation)
  - S2: 60 kg weight → gets 44.44 kg (60/90 of school A's allocation)
- **School B**: 1 student → gets 33.33 kg (1/3 of total food)
  - S3: 70 kg weight → gets 33.33 kg (all of school B's allocation)

### Requirements
- Total food available: 100 kg
- Calculate food allocation for each student
- Use proportional distribution at both school and student levels