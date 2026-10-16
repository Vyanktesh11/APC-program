from student import total_marks, percentage, grade

marks = [int(input(f"Marks in subject {i + 1}: ")) for i in range(5)]
percent = percentage(marks)
print("Total:", total_marks(marks))
print("Percentage:", percent)
print("Grade:", grade(percent))
