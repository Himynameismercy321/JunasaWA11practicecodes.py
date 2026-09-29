print("WELCOME TO JOCKS HOTEL")

while True:
    Junasa_lots = ["A1", "A2", "A5", "B1", "B3"]

    Junasa_lot = input(
        "Available parking lots (A1, A2, A5, B1, B3): "
    ).upper()

    Junasa_found = False

    for Junasa_available_lot in Junasa_lots:
        if Junasa_available_lot == Junasa_lot:
            Junasa_found = True
            break

    if Junasa_found:
        print("Parking lot is available.")
    else:
        print("Parking lot is not available.")

    Junasa_again = input("Check another lot? (Y/N): ")

    if Junasa_again.upper() != "Y":
        print("Thank you and enjoy your stay!")
        break