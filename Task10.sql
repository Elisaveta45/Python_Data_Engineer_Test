SELECT Employee.name
FROM Employee
LEFT JOIN Department ON Employee.department_id = Department.id
WHERE Departmen.id is NULL
UNION
SELECT Department.name
FROM Employee
RIGHT JOIN Department ON Employee.department_id = Department.id
WHERE Employee.department_id is NULL

SELECT Department.name, COUNT(*)
FROM Employee
LEFT JOIN Department
ON Employee.department_id = Department.id
GROUP BY(Department.name)
HAVING COUNT(*) < 3;
