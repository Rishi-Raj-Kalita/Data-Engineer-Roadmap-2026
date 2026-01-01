# SQL Questions

## Question 2: Product Sales by Year 

### Problem Statement
Write a query that returns, for each product_id, the total sales in calendar year 2024 and calendar year 2025 as separate columns.

### Setup

```sql
CREATE TABLE SALES (
    Product_ID INT,
    Date DATE,
    Sales INT
);

INSERT INTO SALES (Product_ID, Date, Sales) VALUES
(1, '2024-10-12', 100),
(2, '2025-01-25', 200),
(2, '2024-08-01', 300),
(3, '2024-01-12', 150),
(3, '2025-02-12', 200),
(5, '2025-03-12', 250),
(2, '2024-03-12', 350),
(1, '2025-05-12', 120),
(5, '2025-06-12', 260);
```

### Input Table: SALES

| Product ID | Date       | Sales |
|------------|------------|-------|
| 1          | 2024-10-12 | 100   |
| 2          | 2025-01-25 | 200   |
| 2          | 2024-08-01 | 300   |
| 3          | 2024-01-12 | 150   |
| 3          | 2025-02-12 | 200   |
| 5          | 2025-03-12 | 250   |
| 2          | 2024-03-12 | 350   |
| 1          | 2025-05-12 | 120   |
| 5          | 2025-06-12 | 260   |

### Expected Output Columns
- Product ID
- Sales_2024
- Sales_2025

### Requirements
- Group sales by product_id and year
- Show 2024 and 2025 sales as separate columns
- Handle products that may not have sales in both years