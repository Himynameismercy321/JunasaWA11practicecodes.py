Junasa_flavor = input("Enter your desired flavor (beef/pepperoni/hawaiian/cheese): ").lower()

if Junasa_flavor == "beef":
    print("========================")
    print("You chose beef flavored pizza")
    print("========================")

elif Junasa_flavor == "pepperoni":
    print("========================")
    print("You chose pepperoni pizza")
    print("========================")

elif Junasa_flavor == "hawaiian":
    print("========================")
    print("You chose Hawaiian pizza")
    print("========================")

elif Junasa_flavor == "cheese":
    print("========================")
    print("You chose cheese pizza")
    print("========================")

else:
    print("========================")
    print("Invalid pizza flavor")
    print("========================")
    exit()


Junasa_size = input("Enter size of your pizza (small/medium/large): ").lower()

match Junasa_size:
    case "small":
        Junasa_price = 180

    case "medium":
        Junasa_price = 250

    case "large":
        Junasa_price = 300

    case _:
        Junasa_price = 0
        print("Invalid size.")

if Junasa_price > 0:
    print("========================")
    print("Pizza price :"   , Junasa_price )
    print("========================")

