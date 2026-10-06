Junasa_employee = {
        "E100": {"name": "Liane uy",
                 "rank": "JO 5",
                 "Duty hours": (42, 43, 40, 40),
                 "Basicpay" : 290000,
                 "requirmentHrs": 160},

        "E105": {"name": "Robert santos",
                 "rank": "Manager 1",
                 "Duty Hours": (30, 35,31,30),
                 "Basicpay": 60000,
                 "requirements": 120 }
        }

Junasa_search = input("Enter employee ID: ").upper()

for employeeid, sheet in Junasa_employee.items():

    if Junasa_search == employeeid:

        print("Found")

        Name = sheet["name"]
        jobrank = sheet["rank"]
        dootyhrs = sheet["Duty Hours"]
        basicP = sheet["Basicpay"]
        quiredhrs = sheet["requirements"]


        total_hours = 0

        for hours in dootyhrs:
            total_hours += hours
        rate = basicP / quiredhrs
        overtime = 0
        if total_hours > quiredhrs:
            overtime = total_hours - quiredhrs
        overtime_rate = rate * 1.5
        overtime_pay = overtime * overtime_rate
        grosspay = basicP + overtime_pay

        print("=-=-=-=-=-=-=-=-=-=-=")
        print("Employee ID:", employeeid)
        print("Name:", Name)
        print("Rank:", jobrank)
        print("Duty Hours:", dootyhrs)
        print("Total Hours:", total_hours)
        print("Basic Pay:", basicP)
        print("Required Hours:", quiredhrs)
        print("Regular Rate:", rate)
        print("Overtime Hours:", overtime)
        print("Overtime Rate:", overtime_rate)
        print("Overtime Pay:", overtime_pay)
        print("Gross Pay:", grosspay)









