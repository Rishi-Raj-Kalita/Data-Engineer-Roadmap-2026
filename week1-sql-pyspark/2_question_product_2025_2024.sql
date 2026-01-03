
-- create
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


-- fetch 
with ordered_dates as (
  select *,
  extract("year" from date) as year
  from SALES
),
sales_a as (

  select product_id,
  sum(sales) as sales_sum
  from 
  ordered_dates
  where year = 2024
  group by product_id
),
sales_b as (
  select product_id,
  sum(sales) as sales_sum
  from ordered_dates
  where year = 2025 
  group by product_id
)
select coalesce(a.product_id, b.product_id),
a.sales_sum as sales_2024,
b.sales_sum as sales_2025
from sales_a as a 
full outer join sales_b as b 
on  a.product_id = b.product_id;


