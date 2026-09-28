students = {
    "Ana": [98,88,87],
    "Kirk": [88,89,80],
    "Liza": [69,71,83]
}

highest = 0
name_highest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average", f"{average:.0f}")
    if average > highest:
        highest = average
        name_highest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print(f"Students {name_highest} got the highest average: {highest}")
print(f"There are {tally} grades which are below 75 ")