Junasa_patient = {
    "Junasa": (130, 190, 250, 130, 100, 70, 80),
    "Pascual": (90, 100, 70, 80, 150, 300, 200),
    "Jade": (80, 60, 100, 150, 180, 200, 250),
}

for name, reading in Junasa_patient.items():

    highest_reading = max(reading)
    lowest_reading = min(reading)

    Junasa_average = highest_reading / len(reading)
    Junasa_difference = highest_reading  - lowest_reading

    Junasa_high_reading = 0
    Junasa_normal_reading = 0

    print("\n", name)

    for item in reading:
        if item > 120:
            print(item, "High")
            Junasa_high_reading += 1
        else:
            print(item, "Normal")
            Junasa_normal_reading += 1

    print("Highest reading:", highest_reading)
    print("Lowest reading:", lowest_reading)
    print("Average:", int(Junasa_average))
    print("Difference:", Junasa_difference)
    print("Number of high readings:", Junasa_high_reading)