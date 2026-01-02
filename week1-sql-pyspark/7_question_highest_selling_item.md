## SQL Questions

### Question 7: Highest Selling Item on a Given Date

#### Problem Statement

You are given order-level and order-item-level data.
Write an SQL query to identify the **item name with the highest total sales amount** for a given date (for example, **1st January 2025**).

Sales should be calculated using the **total amount at the item level**, aggregated across all orders placed on the given date.

---

## Database Schema

### Table 1: ORDERS

| Column Name | Data Type | Description                       |
| ----------- | --------- | --------------------------------- |
| id          | INT       | Primary Key - Order identifier    |
| price       | DECIMAL   | Total order price                 |
| discount    | DECIMAL   | Discount applied on the order     |
| net_amt     | DECIMAL   | Net payable amount after discount |
| order_date  | DATE      | Date when the order was placed    |

---

### Table 2: ORDER_DETAILS

| Column Name | Data Type | Description                           |
| ----------- | --------- | ------------------------------------- |
| id          | INT       | Primary Key - Order item identifier   |
| item_name   | VARCHAR   | Name of the item                      |
| qty         | INT       | Quantity of the item ordered          |
| amount      | DECIMAL   | Total price for the item (qty × rate) |
| order_id    | INT       | Foreign Key referencing ORDERS(id)    |

---

## Table Setup

```sql
CREATE TABLE ORDERS (
    id INT PRIMARY KEY,
    price DECIMAL(10, 2),
    discount DECIMAL(10, 2),
    net_amt DECIMAL(10, 2),
    order_date DATE
);

CREATE TABLE ORDER_DETAILS (
    id INT PRIMARY KEY,
    item_name VARCHAR(50),
    qty INT,
    amount DECIMAL(10, 2),
    order_id INT
);
```

---

## Sample Input Data

### ORDERS Table

```sql
INSERT INTO ORDERS (id, price, discount, net_amt, order_date) VALUES
(1, 500, 50, 450, '2025-01-01'),
(2, 800, 100, 700, '2025-01-01'),
(3, 300, 0, 300, '2025-01-02');
```

---

### ORDER_DETAILS Table

```sql
INSERT INTO ORDER_DETAILS (id, item_name, qty, amount, order_id) VALUES
(1, 'Laptop', 1, 400, 1),
(2, 'Mouse', 2, 100, 1),
(3, 'Laptop', 1, 700, 2),
(4, 'Keyboard', 1, 300, 3);
```

---

```python
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DecimalType, DateType
)
from datetime import date

# ORDERS schema
orders_schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("price", DecimalType(10, 2), nullable=True),
    StructField("discount", DecimalType(10, 2), nullable=True),
    StructField("net_amt", DecimalType(10, 2), nullable=True),
    StructField("order_date", DateType(), nullable=True)
])

# ORDERS data
orders_data = [
    (1, 500.00, 50.00, 450.00, date(2025, 1, 1)),
    (2, 800.00, 100.00, 700.00, date(2025, 1, 1)),
    (3, 300.00, 0.00, 300.00, date(2025, 1, 2))
]

orders_df = spark.createDataFrame(orders_data, schema=orders_schema)


# ORDER_DETAILS schema
order_details_schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("item_name", StringType(), nullable=True),
    StructField("qty", IntegerType(), nullable=True),
    StructField("amount", DecimalType(10, 2), nullable=True),
    StructField("order_id", IntegerType(), nullable=True)
])

# ORDER_DETAILS data
order_details_data = [
    (1, "Laptop", 1, 400.00, 1),
    (2, "Mouse", 2, 100.00, 1),
    (3, "Laptop", 1, 700.00, 2),
    (4, "Keyboard", 1, 300.00, 3)
]

order_details_df = spark.createDataFrame(order_details_data, schema=order_details_schema)
```


## Expected Output (for 1st January 2025)

| item_name |
| --------- |
| Laptop    |

---

## Requirements

* Consider only orders placed on the given date (e.g., `2025-01-01`)
* Aggregate sales using **order_details.amount**
* Identify the item with the **highest total sales amount**
* Handle multiple orders and multiple items per order
