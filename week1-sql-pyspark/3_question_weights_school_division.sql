
-- create
CREATE TABLE STUDENTS (
    school_name   VARCHAR(10),
    student_name  VARCHAR(10),
    weight        INT
);

INSERT INTO STUDENTS (school_name, student_name, weight) VALUES
('A', 'S1', 30),
('A', 'S2', 60),
('B', 'S3', 70);


-- fetch 


with ordered as (
  select *,
  count(*) over() as total_students,
  count(*) over(partition by school_name) as total_students_by_school,
  sum(weight) over(partition by school_name) as wt_by_school
  from students 
)
select school_name,
student_name,
weight,
((100.00*total_students_by_school*weight)/(total_students*wt_by_school)) as division
from ordered;
