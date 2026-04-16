def delete_student(students):
    name = input("Enter name: ")
    return [s for s in students if s["name"] != name]