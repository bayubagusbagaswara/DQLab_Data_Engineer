select StudentID,
    CONCAT(FirstName, LastName) as Name,
    Semester1,
    Semester2,
    MarkGrowth
from students;