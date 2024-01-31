'''
Find the common Elements in an Array.

Array_1 = [1,2,3,2,1]
Array_2 = [1,2,3]
Array_3 = [1,2,3,4]

Output should be.,
[1,2,3]

Array can be of any size and by default there should be two arrays for comparison.

'''

# Milan Patel version of the solution
# Version 1, using "set".
Array_1 = [1,2,3,2,1]
Array_2 = [1,2,3]
Array_3 = [1,2,3,4]

common_elements = set(Array_1) & set(Array_2) & set(Array_3)
print(list(common_elements))




