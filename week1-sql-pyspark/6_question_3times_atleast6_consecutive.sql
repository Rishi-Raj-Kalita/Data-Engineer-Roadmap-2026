
-- create
CREATE TABLE USER_ACTIVITY (
    user_id INT,
    activity_date DATE
);


INSERT INTO USER_ACTIVITY (user_id, activity_date) VALUES
(1, '2024-01-05'),
(1, '2024-01-12'),
(1, '2024-01-20'),
(1, '2024-02-03'),
(1, '2024-02-15'),
(1, '2024-02-28'),
(1, '2024-03-10'),
(1, '2024-03-18'),
(1, '2024-03-25'),
(1, '2024-04-02'),
(1, '2024-04-14'),
(1, '2024-04-22'),
(1, '2024-05-08'),
(1, '2024-05-16'),
(1, '2024-05-30'),
(1, '2024-06-05'),
(1, '2024-06-12'),
(1, '2024-06-25'),

(2, '2024-01-10'),
(2, '2024-01-15'),
(2, '2024-01-25'),
(2, '2024-02-05'),
(2, '2024-02-20'),
(2, '2024-03-08'),
(2, '2024-03-15'),
(2, '2024-04-12'),
(2, '2024-04-18'),
(2, '2024-04-25'),

(3, '2024-01-08'),
(3, '2024-01-16'),
(3, '2024-01-24'),
(3, '2024-02-12'),
(3, '2024-02-18'),
(3, '2024-02-25'),
(3, '2024-03-05'),
(3, '2024-03-20'),
(3, '2024-03-28'),
(3, '2024-04-10'),
(3, '2024-04-15'),
(3, '2024-04-28'),
(3, '2024-05-12'),
(3, '2024-05-20'),
(3, '2024-05-25'),
(3, '2024-06-08'),
(3, '2024-06-18'),
(3, '2024-06-22'),
(3, '2024-07-05'),
(3, '2024-07-15'),
(3, '2024-07-25');

-- fetch 

with monthly_user_activity as (
  select user_id,
  date_trunc('month', activity_date) as month 
  from USER_ACTIVITY
),
grouped_user_activity as (
  select user_id,
  month 
  from monthly_user_activity
  group by user_id,month 
  having count(*)>=3
),
ordered_user_activty as (
  select user_id, 
  month - INTERVAL '1 Month' * ROW_NUMBER() over(partition by user_id order by month) as grp 
  from grouped_user_activity
)
select user_id from ordered_user_activty
group by user_id,grp having count(*)>=6;





