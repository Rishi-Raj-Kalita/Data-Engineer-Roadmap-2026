
-- create
CREATE TABLE USERS (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    registration_date DATE
);

CREATE TABLE ACTIVITY_LOGS (
    log_id INT PRIMARY KEY,
    user_id INT,
    activity_date DATE,
    activity_type VARCHAR(20)
);

CREATE TABLE TRANSACTIONS (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    transaction_date DATE,
    amount DECIMAL(10, 2)
);


INSERT INTO USERS (user_id, user_name, registration_date) VALUES
(1, 'Alice', '2024-01-15'),
(2, 'Bob', '2024-02-20'),
(3, 'Charlie', '2024-03-10'),
(4, 'Diana', '2024-04-05'),
(5, 'Eve', '2024-05-12');


INSERT INTO ACTIVITY_LOGS (log_id, user_id, activity_date, activity_type) VALUES
(1, 1, '2025-12-21', 'login'),
(2, 1, '2025-12-23', 'login'),
(3, 1, '2025-12-25', 'login'),
(4, 2, '2025-12-22', 'login'),
(5, 2, '2025-12-24', 'login'),
(6, 3, '2025-12-21', 'login'),
(7, 3, '2025-12-26', 'login'),
(8, 4, '2025-12-23', 'login'),
(9, 5, '2025-12-25', 'login'),
(10, 1, '2025-12-26', 'login'),
(11, 1, '2025-12-27', 'login'),
(12, 1, '2025-12-28', 'login'),
(13, 1, '2025-12-29', 'login');


INSERT INTO TRANSACTIONS (transaction_id, user_id, transaction_date, amount) VALUES
(1, 1, '2025-12-22', 150.00),
(2, 1, '2025-12-24', 200.00),
(3, 2, '2025-12-23', 75.00),
(4, 2, '2025-12-25', 300.00),
(5, 3, '2025-12-21', 600.00),
(6, 4, '2025-12-24', 1200.00),
(7, 5, '2025-12-26', 50.00);

-- fetch 

WITH login_metrics AS (
    SELECT
        user_id,
        COUNT(*) AS total_logins
    FROM activity_logs
    WHERE activity_date >= current_date - interval '30 day'
    GROUP BY user_id
),
transaction_metrics AS (
    SELECT
        user_id,
        SUM(amount) AS total_transactions
    FROM transactions
    WHERE transaction_date >= current_date - interval '30 day'
    GROUP BY user_id
),
user_metrics AS (
    SELECT
        u.user_id,
        u.user_name,
        COALESCE(l.total_logins, 0) AS total_logins,
        COALESCE(t.total_transactions, 0) AS total_transactions
    FROM users u
    LEFT JOIN login_metrics l
        ON u.user_id = l.user_id
    LEFT JOIN transaction_metrics t
        ON u.user_id = t.user_id
),
tiered_users as (
  select user_id,
  user_name,
  case
  when total_logins>=20 and total_transactions>=1000 then 'Gold'
  when total_logins>=10 and total_transactions>=500 then 'Silver'
  when total_logins>=5 and total_transactions>=100 then 'Bronze'
  else NULL
  end
  as tier 
  from user_metrics
)
select user_id,
user_name,
tier
from tiered_users
where tier is not NULL
order by 
  case
  when tier='Gold' then 1 
  when tier='Silver' then 2 
  when tier='Bronze' then 3 
  END, 
  user_name;











