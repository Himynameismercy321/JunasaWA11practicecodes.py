Junasa_grade = int(input("Enter your grade: "))

match Junasa_grade:
    case n if 90 <= n <= 100:
        print("Excellent")

    case n if 80 <= n <= 89:
        print("very good")

    case n if 75 <= n <= 79:
        print("passed")

    case n if 0 <= n <= 74:
        print("Failed")

    case _:
        print("Invalid input")
