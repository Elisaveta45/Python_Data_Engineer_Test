SELECT Employee.name, Employee.id, Department.id
FROM Employee
LEFT JOIN Department ON Employee.department_id = Department.id
WHERE Departmen.id is NULL

SELECT Department.name, Employee.id, Department.id
FROM Employee
RIGHT JOIN Department ON Employee.department_id = Department.id
WHERE Employee.department_id is NULL

SELECT Department.name, Employee.id, Department.id, COUNT(Employee.id)
FROM Employee
RIGHT JOIN Department ON Employee.department_id = Department.id
GROUP BY(Department.id)
HAVING COUNT(Employee.id) < 3;