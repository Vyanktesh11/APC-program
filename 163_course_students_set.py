python_students = {"Rahul", "Amit", "Priya", "Sneha"}
java_students = {"Priya", "Sneha", "Rohan", "Neha"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)
