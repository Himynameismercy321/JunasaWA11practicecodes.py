class_record = {
    "Liza": {
        "StudID": "S001",
        "Grade": [90, 85, 66, 82, 83, 90, 92]
    },
    "Jeremy": {
        "StudID": "S002",
        "Grade": [72, 75, 69, 80, 84, 75, 50]
    }
}

search = input("Enter student name or ID: ").title()

found = False

for student in class_record:
    if student == search or class_record[student]["StudID"] == search.upper():
        found = True

        print("\nStudent found")
        print("===============")
        print("Student Name:", student)
        print("Student ID:", class_record[student]["StudID"])

        grades = class_record[student]["Grade"]

        total = 0
        highest = grades[0]
        lowest = grades[0]

        for grade in grades:
            total += grade

            if grade > highest:
                highest = grade

            if grade < lowest:
                lowest = grade

        average = total / len(grades)

        print("Grades:", grades)
        print("Average:", round(average, 2))
        print("Highest grade:", highest)
        print("Lowest grade:", lowest)

        if lowest < 60:
            print("==========================")
            print("Candidate for intervention")
        else:
            print("======================")
            print("No intervention needed")

if found == False:
    print("Student not found.")





