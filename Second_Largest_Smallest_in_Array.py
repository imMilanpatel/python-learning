'''
Code to find the second largest and Second Smallest number in an Array!
'''

# Milan Patel's versions.
# Version 1 using "sorted function and simple indexing logic"

def second_largest(array_with_numbers):
    sorted_array = sorted(array_with_numbers)
    second_largest = sorted_array[len(sorted_array) - 2]
    return second_largest 
    
def second_smallest(array_with_numbers):
    sorted_array = sorted(array_with_numbers)
    second_smallest = sorted_array[1]
    return second_smallest


# Inputs
number_array = [50,8,75,2,95]

# Function Call
second_largest_number = second_largest(number_array)
second_smallest_number = second_smallest(number_array)

# Output Printing
print(f"Second Largest number is: {second_largest_number}")
print(f"Second Smallest number is: {second_smallest_number}")