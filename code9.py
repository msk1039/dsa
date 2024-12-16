class Student:
    def __init__(self, id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, student):
        index = self.hash_function(student.id)
        self.table[index].append(student)

    def get_student(self, id):
        index = self.hash_function(id)
        for student in self.table[index]:
            if student.id == id:
                return student
        return None


student_system = HashTable()

while True:
    print("\n1. Add student")
    print("2. Find student")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        id = int(input("Enter student ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        student = Student(id, name, age, grade)
        student_system.insert(student)
        print("Student added!")

    elif choice == 2:
        id = int(input("Enter student ID to find: "))
        student = student_system.get_student(id)
        if student:
            print(f"ID: {student.id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
        else:
            print("Student not found")

    elif choice == 3:
        break

    else:
        print("Invalid choice")