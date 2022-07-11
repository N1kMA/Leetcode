select t.worker_title from worker w
left join title t on w.worker_id = t.worker_ref_id
where salary  = (select max(salary) from worker)

--https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1