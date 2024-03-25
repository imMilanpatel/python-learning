'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''

list_one = [2,4,3][::-1]
list_two = [5,6,4][::-1]
                #  3 4 2 + 
                #  4 6 5
expected_output = [7,0,8] 

output = []
for index_of_number in range(len(list_one)):
    element = list_one[index_of_number] + list_two[index_of_number]
    if element < 10:
        output.append(element)
    else:
        element_0th = element[0]
        element_1st = element[1]



  
print(output)