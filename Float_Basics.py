# ------------------------------------------------------------------------------------------------------------------
# Challenge 1: Declare two floats and find the sum, difference, product, quotient and remainder of the two numbers
# ------------------------------------------------------------------------------------------------------------------

from Integers_Basics import Calculator

Calculator_Instance = Calculator(21.2, 11.9)
Calculator_Instance.display_results()


# Add your code here

# ----------------------------------------
# Challenge 2: Find the square root of 121
# ----------------------------------------
import math

# Version 1
number = 121
result = number ** 0.5
print(f"Square root of the {number} is {result} using normal calculation")


# Version 2
square_root = math.sqrt(number)
print(f"Using math library the square root of the {number} is {square_root}")

#################################################################################