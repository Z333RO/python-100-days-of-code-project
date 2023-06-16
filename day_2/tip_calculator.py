print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much would you like to tip in percentage? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_calc = tip / 100 * bill + bill
bill_per_person = tip_calc / people
# tip_total = str(round(bill_per_person, 2)) << has issues with printing 2 decimal places for whole numbers
tip_total = "{:.2f}".format(bill_per_person)

# print("Each person should pay " + tip_total) << original code
print(f"Each person should pay: ${tip_total}")