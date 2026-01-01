## SQL Questions

### Question 10: Find the Department with the Highest Average Salary

#### Problem Statement

You are given an `EMPLOYEE` table containing employee details across multiple departments.
Write an SQL query to identify the **department that has the highest average salary**.

---

## Database Schema

### Table: EMPLOYEE

| Column Name     | Data Type | Description                              |
| --------------- | --------- | ---------------------------------------- |
| emp_id          | INT       | Unique identifier for each employee      |
| name            | VARCHAR   | Name of the employee                     |
| salary          | INT       | Employee salary                          |
| department_name | VARCHAR   | Department to which the employee belongs |

---

## Table Setup

```sql
CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department_name VARCHAR(50)
);
```

---

## Sample Input Data

```sql
INSERT INTO EMPLOYEE (emp_id, name, salary, department_name) VALUES
(1, 'Alice', 60000, 'Engineering'),
(2, 'Bob', 50000, 'Engineering'),
(3, 'Charlie', 40000, 'HR'),
(4, 'Diana', 45000, 'HR'),
(5, 'Eve', 70000, 'Sales');
```

---

## EMPLOYEE Table

| emp_id | name    | salary | department_name |
| ------ | ------- | ------ | --------------- |
| 1      | Alice   | 60000  | Engineering     |
| 2      | Bob     | 50000  | Engineering     |
| 3      | Charlie | 40000  | HR              |
| 4      | Diana   | 45000  | HR              |
| 5      | Eve     | 70000  | Sales           |

---

## Expected Output

| department_name |
| --------------- |
| Sales           |

---


