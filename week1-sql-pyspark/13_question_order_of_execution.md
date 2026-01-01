Here is the **question formatted in the same clean, structured style** as your previous SQL questions.
This works well for **interview prep, README, or YouTube content**.

---

## SQL Questions

### Question 12: Order of Execution in SQL Query

#### Problem Statement

Write the **logical order of execution** of different clauses in an SQL query.
Explain how a SQL engine processes a query containing clauses such as `FROM`, `JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`, and `LIMIT`.

---

## Sample SQL Query

```sql
SELECT
    e.department_name,
    COUNT(*) AS emp_count
FROM employee e
JOIN salary s
    ON e.emp_id = s.emp_id
WHERE s.salary > 50000
GROUP BY e.department_name
HAVING COUNT(*) > 5
ORDER BY emp_count DESC
LIMIT 3;
```

---

## Task

* Identify the **order in which SQL clauses are executed**
* Explain how `JOIN` and `WHERE` are evaluated
* Clarify the difference between **logical execution order** and **written order**
* Mention where **window functions** are evaluated (if applicable)

---

## Expected Output

A list showing the **logical execution order**, for example:

1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

---


