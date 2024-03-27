'''
Input: 

list1 = [1,2,4] 
list2 = [1,3,4]

Output: [1,1,2,3,4,4]
'''

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    
    while i < len(list1) or j < len(list2):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    return result

# Example usage:
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(merge_sorted_lists(list1, list2))  # Output: [1, 1, 2, 3, 4, 4]

list1 = []
list2 = []
print(merge_sorted_lists(list1, list2))  # Output: []

list1 = []
list2 = [0]
print(merge_sorted_lists(list1, list2))  # Output: [0]
