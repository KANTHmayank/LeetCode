# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
INNER JOIN Employee d
ON e.managerid = d.Id
WHERE e.salary > d.salary;