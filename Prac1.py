students = {
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95
}
print("Student grades")
print("-----------------")
print("Ana", students["Ana"])
print("Ben", students["Ben"])

students["Ella"] = 88

students["Ben"] = 82
students["Diana"] = 91
name1 = input("Enter student name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdates student Grades")
print("--------------------------")


for name, grade in students.items():
    print(name, ":", grade)

search = input ("\nEnter student name to search: ")
if search in students:
    print(search, "has a agrade of", students[search])
else:
    print("Student not found.")