'''

Input: 

list1 = [1,2,4] 
list2 = [1,3,4]

Output: [1,1,2,3,4,4]

'''
list1 = [1,2,4] 
list2 = [1,3,4]
output = []

for number in list1:
    output.append(number)
    
for number2 in list2:
    output.append(number2)

output.sort()

print(output)
