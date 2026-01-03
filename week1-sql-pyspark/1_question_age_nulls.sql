
-- create
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

-- fetch 
with ordered as (
  select *,
  case when age is not null then 1 else 0 end as is_new_group
  from EMP 
),
grouped as (
  select *,
  sum(is_new_group) over(order by id) as g 
  from ordered
)
select 
id, 
name,
first_value(age) over(partition by g order by id) as age
from grouped;


