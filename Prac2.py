studentsL = {"Ana": [98,85,82],
           "kirk":[72,73,78]}

students = {"Ana:": (98,85,82),
            "Charlie kirk:": (98,85,88)}

for name,grade in students.items():
    print(name,*grade)