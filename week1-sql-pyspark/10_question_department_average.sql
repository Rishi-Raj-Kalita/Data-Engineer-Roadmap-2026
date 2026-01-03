
-- create
CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department_name VARCHAR(50)
);

INSERT INTO EMPLOYEE (emp_id, name, salary, department_name) VALUES
(1, 'Alice', 60000, 'Engineering'),
(2, 'Bob', 50000, 'Engineering'),
(3, 'Charlie', 40000, 'HR'),
(4, 'Diana', 45000, 'HR'),
(5, 'Eve', 70000, 'Sales');


-- fetch 
with department_avg_salary as (
  select department_name,
  avg(salary)  as avg_salary
  from EMPLOYEE
  group by department_name
)
select department_name
from department_avg_salary
where avg_salary = (select max(avg_salary) from department_avg_salary);


