## SQL Questions

### Question 8: SQL Join Types Analysis

#### Problem Statement

You are given two tables, **Table A** and **Table B**, each containing integer values (with duplicates and NULLs).
Your task is to understand how different SQL joins behave by writing queries and identifying the output for:

* LEFT JOIN
* RIGHT JOIN
* INNER JOIN
* FULL OUTER JOIN
* CROSS JOIN

---

## Database Schema

### Table A

| Column Name | Data Type |
| ----------- | --------- |
| value       | INT       |

### Table B

| Column Name | Data Type |
| ----------- | --------- |
| value       | INT       |

---

## Table Setup

```sql
CREATE TABLE A (
    value INT
);

CREATE TABLE B (
    value INT
);
```

---

## Sample Input Data

### Table A Data

```sql
INSERT INTO A (value) VALUES
(1),
(1),
(NULL),
(NULL),
(2),
(3),
(4);
```

Table A

| value |
| ----- |
| 1     |
| 1     |
| NULL  |
| NULL  |
| 2     |
| 3     |
| 4     |

---

### Table B Data

```sql
INSERT INTO B (value) VALUES
(2),
(1),
(2),
(NULL),
(3);
```

Table B

| value |
| ----- |
| 2     |
| 1     |
| 2     |
| NULL  |
| 3     |

---

## Join Outputs

### INNER JOIN

Returns only matching values present in **both** tables.

```sql
SELECT A.value AS a_value, B.value AS b_value
FROM A
INNER JOIN B
ON A.value = B.value;
```

| a_value | b_value |
| ------- | ------- |
| 1       | 1       |
| 1       | 1       |
| 2       | 2       |
| 2       | 2       |
| 3       | 3       |

---

### LEFT JOIN

Returns all rows from **Table A**, and matching rows from **Table B**.

```sql
SELECT A.value AS a_value, B.value AS b_value
FROM A
LEFT JOIN B
ON A.value = B.value;
```

| a_value | b_value |
| ------- | ------- |
| 1       | 1       |
| 1       | 1       |
| NULL    | NULL    |
| NULL    | NULL    |
| 2       | 2       |
| 2       | 2       |
| 3       | 3       |
| 4       | NULL    |

---

### RIGHT JOIN

Returns all rows from **Table B**, and matching rows from **Table A**.

```sql
SELECT A.value AS a_value, B.value AS b_value
FROM A
RIGHT JOIN B
ON A.value = B.value;
```

| a_value | b_value |
| ------- | ------- |
| 2       | 2       |
| 2       | 2       |
| 1       | 1       |
| 1       | 1       |
| NULL    | NULL    |
| 3       | 3       |

---

### FULL OUTER JOIN

Returns all rows when there is a match in **either** table.

```sql
SELECT A.value AS a_value, B.value AS b_value
FROM A
FULL OUTER JOIN B
ON A.value = B.value;
```

| a_value | b_value |
| ------- | ------- |
| 1       | 1       |
| 1       | 1       |
| 2       | 2       |
| 2       | 2       |
| 3       | 3       |
| 4       | NULL    |
| NULL    | NULL    |
| NULL    | NULL    |

---

### CROSS JOIN

Returns the **cartesian product** of both tables.

```sql
SELECT A.value AS a_value, B.value AS b_value
FROM A
CROSS JOIN B;
```

* Total rows = rows in A × rows in B
* 7 × 5 = **35 rows**

| a_value | b_value |
| ------- | ------- |
| 1       | 2       |
| 1       | 1       |
| 1       | 2       |
| 1       | NULL    |
| 1       | 3       |
| ...     | ...     |

---

## Key Observations (Interview Important)

* `NULL = NULL` **does not match** in joins
* Duplicate values multiply the number of matching rows
* LEFT and RIGHT joins preserve rows from one side
* FULL OUTER JOIN keeps all unmatched rows
* CROSS JOIN can explode data size and must be used carefully

---