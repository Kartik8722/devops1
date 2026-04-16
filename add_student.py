students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    students.append({"name": name, "age": age})
    print("Student added")