'''
Find out the maximum number and increment it by 1 in the array

Example 1
Input = [1,3,2]
Output = [1,4,2]

Example 2
Input = [90,12,69,12]
Ouput = [91,12,69,12]

'''

input_array = [90,12,69,12]
max_value = max(input_array)
index_of_max_value = input_array.index(max_value)
input_array[index_of_max_value] = max_value + 1
print(input_array)
