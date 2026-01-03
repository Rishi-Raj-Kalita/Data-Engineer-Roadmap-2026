with ordered as (
  select value,
  row_number() over() as rn
  from NUMBERS
),
numbered as (
  select value,
  rn,
  case when value!=coalesce(lag(value) over(order by rn),-1) then 1 else 0 end as is_new_group 
  from ordered
),
grouped as (
  select value, 
  is_new_group,
  sum(is_new_group) over(order by rn) as g 
  from numbered
)
select value 
from grouped
group by g, value
having count(*)>=3;