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
        print(f"Sum: {self.calculate_sum():.2f}")
        print(f"Difference: {self.calculate_difference():.2f}")
        print(f"Product: {self.calculate_product():.2f}")
        print(f"Quotient: {self.calculate_quotient():.2f}")
        print(f"Remainder: {self.calculate_remainder():.2f}")

####################################################################
# --------------------------------
# Challenge 2: Find the cube of 39
# --------------------------------
class Cuberoot:
    def __init__(self, number):
        self.number = number

    # Version 1
    def normal_way(self):
        cube_of_39 = self.number * self.number * self.number
        return cube_of_39 

    # Version 2
    def power_method(self):
        result = pow(self.number,3)
        return result
    
    # Display Result
    def display_values(self):
        print(f"Cube of the number is using regular way is {self.normal_way():.2f}")
        print(f"Cube of the using 'pow' power method is {self.power_method():.2f}")

cube_root_calculator = Cuberoot(39)
cube_root_calculator.display_values()
####################################################################################