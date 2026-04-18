# Global list to store students
students_list = []


# Class definition
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id


# Function to collect student data
def collect_students():
    for i in range(3):  # minimum 3 students
        print(f"\nEnter details for student {i + 1}")
        
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")

        student = Student(name, age, student_id)

        # Add to global list
        students_list.append(student)


# # 🔁 Separate function instead of lambda
# def get_age(student):
#     return student.age

# Function to display sorted students
def display_students():
    # Sort students by age
    # sorted_students = sorted(students_list, key=get_age)
    sorted_students = sorted(students_list, key=lambda s: s.age)

    print("\nStudent List (sorted by age):")
    for student in sorted_students:
        print(f"Name: {student.name}, Age: {student.age}")


# Entry point
if __name__ == "__main__":
    collect_students()
    display_students()