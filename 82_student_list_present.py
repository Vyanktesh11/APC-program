students = []

n = int(input("Enter number of students: "))

for i in range(n):
    students.append(input("Enter student name: "))

while True:
    print("1.Total Students")
    print("2.Search Student")
    print("3.Add Student")
    print("4.Remove Student")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Total Students:", len(students))

    elif choice == 2:
        name = input("Enter student name: ")
        if name in students:
            print("Present")
        else:
            print("Absent")

    elif choice == 3:
        name = input("Enter new student: ")
        students.append(name)

    elif choice == 4:
        name = input("Enter absent student: ")
        if name in students:
            students.remove(name)
        else:
            print("Student not found")

    elif choice == 5:
        break

    else:
        print("Invalid Choice")