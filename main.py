from add_student import add_student
from view_students import view_students
from delete_student import delete_student

students = []

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students(students)
    elif ch == "3":
        students = delete_student(students)
    elif ch == "4":
        break