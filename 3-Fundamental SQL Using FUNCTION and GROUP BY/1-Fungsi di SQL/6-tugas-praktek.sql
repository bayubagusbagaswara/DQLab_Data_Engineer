select StudentID,
    FirstName,
    LastName,
    MOD(Semester1, 2) as Semester1,
    Semester2,
    EXP(MarkGrowth)
from students;