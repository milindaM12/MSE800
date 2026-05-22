numbers = [1, 2, 3, 4, 5]
sq = {str(n):n**2 for n in numbers}
#print(sq)

# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}

# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}

# Dictionary 3
student3 = {
    "name": "azwan",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

# Store dictionaries inside a list
students = [student1, student2, student3]

# Merge dictionaries only if name contains "azw"
merged_students = {}

for student in students:
    if "azw" in student["name"].lower():
        merged_students.update(student)

print(merged_students)