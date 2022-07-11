select distinct(user_id) from (
select id, user_id, item, created_at, revenue, previous_created_at from (
select *, lag(created_at) over(PARTITION BY user_id order by user_id, created_at) as previous_created_at from
amazon_transactions order by user_id, created_at) as q
where extract(day from created_at) - extract(day from previous_created_at) <= 7) s
--https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1