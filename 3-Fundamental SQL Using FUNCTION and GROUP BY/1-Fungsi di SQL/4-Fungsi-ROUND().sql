select StudentID,
    FirstName,
    LastName,
    round(Semester1, 1) as Semester1,
    round(Semester2, 0) as Semester2,
    MarkGrowth
from students;