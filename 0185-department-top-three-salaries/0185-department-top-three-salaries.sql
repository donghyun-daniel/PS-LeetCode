SELECT 
    DEPT.name AS Department,
    EMP1.name AS Employee,
    EMP1.salary AS Salary
FROM 
    Employee AS EMP1
    JOIN Department AS DEPT ON EMP1.departmentId = DEPT.id
WHERE 
    (
        SELECT COUNT(DISTINCT EMP2.salary)
        FROM 
            Employee AS EMP2
        WHERE 
            EMP2.departmentId = EMP1.departmentId 
            AND EMP2.salary > EMP1.salary
    ) < 3
ORDER BY 
    DEPT.name, EMP1.salary DESC