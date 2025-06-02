import json
import os

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks
        }

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Year: {self.year}")
        print(f"Marks: {self.marks}")


class StudentManager:
    filename = "students.json"

    @staticmethod
    def load_students():
        if os.path.exists(StudentManager.filename):
            with open(StudentManager.filename, "r") as file:
                data = json.load(file)
                return [Student(**student_data) for student_data in data]
        return []

    @staticmethod
    def save_students(students):
        data = [student.to_dict() for student in students]
        with open(StudentManager.filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def display_students():
        students = StudentManager.load_students()
        if not students:
            print("No students found")
        else:
            for student in students:
                student.display()

    @staticmethod
    def add_student():
        student_id = int(input("Enter student ID: "))
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        year = int(input("Enter year: "))
        marks = float(input("Enter marks: "))

        student = Student(student_id, name, branch, year, marks)
        students = StudentManager.load_students()
        students.append(student)
        StudentManager.save_students(students)
        print("Student added successfully.")

    @staticmethod
    def delete_student():
        student_id = int(input("Enter student ID to delete: "))
        students = StudentManager.load_students()
        students = [s for s in students if s.student_id != student_id]
        StudentManager.save_students(students)
        print("Student deleted successfully.")

    @staticmethod
    def update_student():
        student_id = int(input("Enter student ID to update: "))
        students = StudentManager.load_students()
        for student in students:
            if student.student_id == student_id:
                print("Current details:")
                student.display()
                student.name = input("Enter new name: ")
                student.branch = input("Enter new branch: ")
                student.marks = float(input("Enter new marks: "))
                StudentManager.save_students(students)
                print("Student updated successfully.")
                return
        print("Student not found.")

    @staticmethod
    def search_student():
        student_id = int(input("Enter student ID to search: "))
        students = StudentManager.load_students()
        for student in students:
            if student.student_id == student_id:
                student.display()
                return
        print("Student not found.")

    @staticmethod
    def menu():
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Update Student")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                StudentManager.add_student()
            elif choice == '2':
                StudentManager.display_students()
            elif choice == '3':
                StudentManager.search_student()
            elif choice == '4':
                StudentManager.delete_student()
            elif choice == '5':
                StudentManager.update_student()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    StudentManager.menu()
