"""
Example

input_array = [1,1,2,2,3,4]

split_array_1 = [1,2,3]

split_array_2 = [1,2,4]

"""

input_array = [1,1,2,2,3,4]

split_array_1 = []

split_array_2 = []

#############
for number in input_array:
    if number not in split_array_1:
        split_array_1.append(number)
    else:
        split_array_2.append(number)

print(f"split array 1 = {split_array_1}")
print(f"split array 2 = {split_array_2}")