# This file will check whether the number given as input is a power of four or not?
# Eg: Input = 16 output = True that is 16 = 4^2
# An integer n is a power of 4 if there exists an integer x such that n == 4^x

# Function definition
def power_of_four(number) -> bool:
    ''' Check if n is a positive integer and n is a power of 4 '''
    if number > 0 and (number & (number - 1)) == 0 and number.bit_length() % 2 == 1:
        return True
    else:
        return False
    
# User input
input_number = int(input("Enter the number: "))
print(power_of_four(input_number))