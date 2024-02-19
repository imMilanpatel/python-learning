# Challenge: list challenges to be completed here. minimum of one challenge per tutorial
# 1. Take input from the user into the empty list using input() function.

empty_list = []
print(f"List before user input: {empty_list} ")

# Input from user
total_elements = int(input("Enter the total number of elements to be entered into the list:"))

# Inserting the numbers typed by the user into the empty list
for number in range(total_elements):
    if number == 0:
        numbers = input(f"Enter the {number + 1}st number and type 'Enter' key for entering the new number: ")
        empty_list.append(numbers)
    elif number == 1:
        numbers = input(f"Enter the {number + 1}nd number and type 'Enter' key for entering the new number: ")
        empty_list.append(numbers)
    elif number == 2:
        numbers = input(f"Enter the {number + 1}rd number and type 'Enter' key for entering the new number: ")
        empty_list.append(numbers)
    else:
        numbers = input(f"Enter the {number + 1}th number and type 'Enter' key for entering the new number: ")
        empty_list.append(numbers)

# Printing
print(f"List after geting user input: {empty_list}")