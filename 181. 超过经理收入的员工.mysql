-- 281014
-- MySql
-- Write your MySQL query statement below
select Name as Employee
from
(
    select 
        Id,
        Name,
        Salary as salary_a,
        ManagerID
    from Employee
    # where ManagerID is not NULL
)A
left join
(
    select 
        Id,
        Salary as salary_b
    from Employee 
    # where ManagerID is null
)B
on A. ManagerID = B.Id
where salary_a > salary_b

