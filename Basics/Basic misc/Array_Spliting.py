"""
Example

input_array = [1,1,2,2,3,4]

split_array_1 = [1,2,3]

split_array_2 = [1,2,4]

"""

# Logic
def array_split(input_array, array_1, array_2):
    for number in input_array:
        if number not in array_1 and len(array_1) != 0.5 * len(input_array):
            array_1.append(number)
        else:
            array_2.append(number)


# Inputs
input_array = [1,1,2,2,3,4]
split_array_1 = []
split_array_2 = []

# Function call
array_split(input_array, split_array_1, split_array_2)

# Output verification
print(f"split array 1 = {split_array_1}")
print(f"split array 2 = {split_array_2}")