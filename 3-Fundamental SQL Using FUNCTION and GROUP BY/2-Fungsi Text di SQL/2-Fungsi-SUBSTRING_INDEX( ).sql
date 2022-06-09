select StudentID,
    SUBSTRING_INDEX(Email, '@', 1) as name
from students;