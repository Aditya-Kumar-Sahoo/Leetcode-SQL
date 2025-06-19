# Write your MySQL query statement below
Select a.name, b.bonus
From Employee a
Left Join Bonus b on a.empId = b.empId
Where b.bonus < 1000 or b.bonus IS NULL;