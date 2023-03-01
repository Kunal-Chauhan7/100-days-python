print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip /100
final_tip = bill * tip_percentage
final_bill = bill + final_tip
bill_for_each = final_bill / people
bill_for_each = round(bill_for_each,2)
print(f"Each person should pay: ${bill_for_each}")
