'''
File will calculate perfect number but only upto 
a limit as it might consume huge computer resource to get a higher perfect number
'''

def is_perfect_number(num):
    # Ensure the number is positive
    if num <= 0:
        return False
    
    # Find the sum of proper divisors
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Check if the sum of divisors equals the original number
    return divisors_sum == num

# Example usage:
number_to_check = int(input("Enter the number: "))
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")