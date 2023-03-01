print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? $")) # taking user input for the total bill to be paid
tip = int(input("What percentage would you like to give? 10, 12, or 15? ")) #taking input for the tip
people = int(input("How many people to split the bill? ")) # taking input of people who are contibuting to the bill

tip_percentage = tip /100 # tip % 
final_tip = bill * tip_percentage # calc the final tip
final_bill = bill + final_tip # final bill after adding tip
bill_for_each = final_bill / people # spliting the bill 
bill_for_each = round(bill_for_each,2) # using round method to make it 2 decimal place
print(f"Each person should pay: ${bill_for_each}") # printing the values
