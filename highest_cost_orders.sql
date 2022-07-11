with q as
(select cust_id, order_date,  sum(total_order_cost) as day_cost from orders
group by cust_id, order_date
having order_date>= '2019-02-01' and order_date <= '2019-05-01')
select first_name, day_cost, order_date from q 
left join customers c on c.id = q.cust_id
where day_cost = (select max(day_cost) from q)

--https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1