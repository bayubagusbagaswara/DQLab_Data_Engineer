select StudentID,
    Email,
    REPLACE(Email, 'yahoo', 'gmail') as New_Email
from students;