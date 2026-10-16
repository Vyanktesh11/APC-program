from student.marks import total, percentage
from student.grade import calculate_grade
from student.attendance import eligible

marks = [80, 75, 90, 85, 88]
percent = percentage(marks)
print("Total:", total(marks))
print("Percentage:", percent)
print("Grade:", calculate_grade(percent))
print("Attendance eligible:", eligible(80, 90))
