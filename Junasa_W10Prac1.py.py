while True:
    Junasa_name = input("Enter your name: ")
    Junasa_position = input("Enter your position: (Janitor, clerk, cashier, manager) ")
    Junasa_hours = float(input("Enter actual hours worked: "))

    Junasa_position = Junasa_position.lower()

    match Junasa_position:

        case "janitor":
            Junasa_monthly = 18000

        case "clerk":
            Junasa_monthly = 22000

        case "cashier":
            Junasa_monthly = 24000

        case "manager":
            Junasa_monthly = 40000
        case _:
            print("Position not needed.")
            continue


    Junasa_bms = Junasa_monthly / 2
    Junasa_hr = Junasa_bms / 88

    Junasa_absence_hours = 0
    Junasa_absence_deduction = 0
    Junasa_overtime_hours = 0
    Junasa_overtime_rate = 0
    Junasa_overtime_pay = 0

    if Junasa_hours < 88:
        Junasa_absence_hours = 88 - Junasa_hours
        Junasa_absence_deduction = Junasa_absence_hours * Junasa_hr

    elif Junasa_hours > 88:
        Junasa_overtime_hours = Junasa_hours - 88
        Junasa_overtime_rate = Junasa_hr * 1.25
        Junasa_overtime_pay = Junasa_overtime_hours * Junasa_overtime_rate

    Junasa_net_salary = (
            Junasa_bms
            - Junasa_absence_deduction
            + Junasa_overtime_pay
    )

    print("\n=============================================")
    Junasa_name = Junasa_name
    print(f"Employee Name:              {Junasa_name}")
    print(f"Job Position:               {Junasa_position.title()}")
    print(f"Actual Hours Worked:        {Junasa_hours:,.2f}")
    print(f"Monthly Salary:             {Junasa_monthly:,.2f}")
    print(f"Basic Half-Month:           {Junasa_bms:,.2f}")
    print(f"Hourly Rate:                {Junasa_hr:,.2f}")

    if Junasa_hours < 88:
        print(f"Absent Hours:           {Junasa_absence_hours:,.2f}")
        print(f"Absence Deduction:      {Junasa_absence_deduction:,.2f}")
        print("Overtime Hours:          0.00")
        print("Overtime Pay:            0.00")

    elif Junasa_hours > 88:
        print("Absent Hours:            0.00")
        print("Absence Deduction:       0.00")
        print(f"Overtime Hours:         {Junasa_overtime_hours:,.2f}")
        print(f"Overtime Rate:          {Junasa_overtime_rate:,.2f}")
        print(f"Overtime Pay:           {Junasa_overtime_pay:,.2f}")

    else:
        print("Absent Hours:            0.00")
        print("Absence Deduction:       0.00")
        print("Overtime Hours:          0.00")
        print("Overtime Pay:            0.00")

    print("=============================================")
    print(f"NET HALF-MONTH SALARY: {Junasa_net_salary:,.2f}")
    print("=============================================")
    again = input("Do you want to enter again (Y/N): ")

    if again.upper() != "Y":
        print("THANK YOU")
        break






