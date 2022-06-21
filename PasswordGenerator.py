# This is a simple python file which will generate a password based upon user choice

# Imports
import random

# Welcome message
print("Welcome to the Pypassword Generator !")

# Get user's choice

# No of Letters in password
letters = int(input("How many letters would you like in your password ?\n"))
# No of Symbols in password
symbols = int(input("How many symbols would you like ?\n"))
# No of Numbers in password
number = int(input("How many numbers would you like ?\n"))

# Lists declaration
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '/', '<', '>']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Logic
passwords_list = []

for pass_letters in range(letters):
    passwords_list += random.choice(letters_list)

for pass_symbols in range(symbols):
    passwords_list += random.choice(symbols_list)

for pass_numbers in range(number):
    passwords_list += random.choice(number_list)

# Shuffle the generated password digits
random.shuffle(passwords_list)

# Print the generated password
password = ''
for charc in passwords_list:
    password += charc

print(f"You're generated password is : {password}")
