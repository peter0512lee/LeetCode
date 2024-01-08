/* Write your T-SQL query statement below */
select w1.id as Id
from Weather as w1, Weather as w2
where w1.temperature > w2.temperature
and DATEDIFF(DAY, w2.recordDate, w1.recordDate) = 1