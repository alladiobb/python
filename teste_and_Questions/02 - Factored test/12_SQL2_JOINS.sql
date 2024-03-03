-- You have two table in the database: employee and Department.
-- The table Employee has coluns named emp_id, emp_name, dept_id, and salary.
-- The table Department has columns named dept_id, dept_name, and dept_category.
-- You need to display all the employees, and any departmet that does not have 
-- any employees should show the value of employees as null.

-- Opção 1
SELECT e.emp_name, d.dept_name
FROM Employee e, Department d
WHERE e.dept_id = d.dept_id;

-- Opção 2
SELECT e.emp_name, d.dept_name
FROM Employee e, Department d ON e.dept_id = d.dept_id;

-- Opção 3
SELECT e.emp_name, d.dept_name
FROM Employee e
RIGHT OUTER JOIN Department d ON e.dept_id = d.dept_id;

-- Opção 4
SELECT e.emp_name, d.dept_name
FROM Employee e
JOIN Department d ON e.dept_id = d.dept_id;