
-- create
CREATE TABLE ORDER_EVENTS (
    event_id   INT PRIMARY KEY,
    order_id   INT,
    status     VARCHAR(20),
    event_time DATE
);

INSERT INTO ORDER_EVENTS (event_id, order_id, status, event_time) VALUES
(1, 1, 'open', '2024-01-01'),
(2, 2, 'open', '2024-01-02'),
(3, 3, 'submitted', '2024-01-03'),
(4, 1, 'open', '2024-01-04'),
(5, 1, 'pending', '2024-01-05'),
(6, 2, 'open', '2024-01-06'),
(7, 2, 'processing', '2024-01-07'),
(8, 3, 'open', '2024-01-08'),
(9, 1, 'open', '2024-01-09'),
(10, 1, 'closed', '2024-01-10'),
(11, 2, 'closed', '2024-01-11'),
(12, 3, 'pending', '2024-01-12');

-- fetch 

with changed_events as (
  select *,
  case when status!= lag(status) over(partition by order_id order by event_id) or lag(status) over(partition by order_id 
  order by event_id) is NULL 
  then 1 else 0 end as is_change
  from ORDER_EVENTS
  order by order_id
),
ordered_events as (
  select *,
  sum(is_change) over(partition by order_id order by event_id)
  from changed_events
),
grouped_events as (
  select order_id,
  status,
  min(event_time) as event_time 
  from ordered_events
  group by order_id, status
  order by order_id, event_time
)
select * ,
coalesce(lead(event_time) over(partition by order_id order by event_time), current_timestamp::DATE) as status_change
from grouped_events;






