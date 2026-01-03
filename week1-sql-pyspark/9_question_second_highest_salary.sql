
-- create
CREATE TABLE EMPLOYEE (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
);

---


INSERT INTO EMPLOYEE (emp_id, name, salary) VALUES
(1, 'Employee1', 20000),
(5, 'Employee2', 30000),
(3, 'Employee3', 40000);

-- fetch 

with max_salary as (
  select max(salary) as maxi
  from EMPLOYEE
)
select max(salary) from employee
where salary!=(select maxi from max_salary);






