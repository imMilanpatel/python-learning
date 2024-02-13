# ------------------------------------------------------------------------------------------------------------------
# Challenge 1: Declare two integers and find the sum, difference, product, quotient and remainder of the two numbers
# ------------------------------------------------------------------------------------------------------------------

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_sum(self):
        return self.num1 + self.num2

    def calculate_difference(self):
        return self.num1 - self.num2

    def calculate_product(self):
        return self.num1 * self.num2

    def calculate_quotient(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"

    def calculate_remainder(self):
        if self.num2 != 0:
            return self.num1 % self.num2
        else:
            return "Cannot calculate remainder when divisor is zero"

    def display_results(self):
        print(f"Sum: {self.calculate_sum()}")
        print(f"Difference: {self.calculate_difference()}")
        print(f"Product: {self.calculate_product()}")
        print(f"Quotient: {self.calculate_quotient()}")
        print(f"Remainder: {self.calculate_remainder()}")

# Example usage
calculator_instance = Calculator(10, 5)
calculator_instance.display_results()

####################################################################
# --------------------------------
# Challenge 2: Find the cube of 39
# --------------------------------

# Version 1
cube_of_39 = 39 * 39 * 39
print(f"Cube of the number is using regular way is {cube_of_39}")

# Version 2
result = pow(39,3)
print(f"Cube of the number using 'pow' power method is {result}")

####################################################################################