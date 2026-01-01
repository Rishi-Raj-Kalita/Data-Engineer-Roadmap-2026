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