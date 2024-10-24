class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student
        print(f"Student '{student.name}' added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("Students:")
        for student in self.students.values():
            print(f"- ID: {student.student_id}, Name: {student.name}, Age: {student.age}")

    def update_student(self, student_id, name=None, age=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            print(f"Student ID {student_id} updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print("Student not found.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student = Student(student_id, name, age)
            sms.add_student(student)
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            sms.update_student(student_id, name if name else None, age if age else None)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == '5':
            print("Exiting the student management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
