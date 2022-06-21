# This is a simple python program to calculate Tip to be paid for the waiter

# Welcome messages
print("Welcome to the Tip Calculator !")

# Ask user for the total bill amount
total_bill = float(input("What was the total bill? ₹ "))

# Ask user for the tip percentage
tip = int(input("What percentage tip would you like to give? 10 or 12 or 15 ? "))

# Ask user about the total number of people
number_of_people = int(input("How many people to split the bill ? "))

# Tip calculator logic
tips_amount = ((((tip / 100) * total_bill) + total_bill ) / number_of_people)
tips_amount = "{:.2f}".format(tips_amount)
# Print total tip
print(f"Each person should pay ₹ {tips_amount}")
