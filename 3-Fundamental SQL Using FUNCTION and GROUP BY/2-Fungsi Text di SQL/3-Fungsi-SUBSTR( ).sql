select StudentID,
    SUBSTR(FirstName, 2, 3) as initial
from students;