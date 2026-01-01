## SQL Questions

### Question 9: Find the Second Highest Salary

#### Problem Statement

You are given an `EMPLOYEE` table containing employee details.
Write an SQL query to find the **second highest salary** from the table.

---

## Database Schema

### Table: EMPLOYEE

| Column Name | Data Type | Description                    |
| ----------- | --------- | ------------------------------ |
| emp_id      | INT       | Unique identifier for employee |
| name        | VARCHAR   | Name of the employee           |
| salary      | INT       | Employee salary                |

---

## Table Setup

```sql
CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
);
```

---

## Sample Input Data

```sql
INSERT INTO EMPLOYEE (emp_id, name, salary) VALUES
(1, 'Employee1', 20000),
(5, 'Employee2', 30000),
(3, 'Employee3', 40000);
```

---

## EMPLOYEE Table

| emp_id | name      | salary |
| ------ | --------- | ------ |
| 1      | Employee1 | 20000  |
| 5      | Employee2 | 30000  |
| 3      | Employee3 | 40000  |

---

## Expected Output

| salary |
| ------ |
| 30000  |

---

