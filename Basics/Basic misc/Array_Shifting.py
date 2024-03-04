'''
input_1 = 7
input_2 = [1,2,3,4,5,6,7]
input_3 = 2

output:
[3, 4, 5, 6, 7, 1, 2]

'''
list_of_numbers = []

def array_shifting(index_range, list_of_numbers_only):
    for _ in range(index_range):
        element_removed = list_of_numbers_only.pop(0)
        list_of_numbers_only.append(element_removed)
        
    return list_of_numbers_only
                
    
def create_array(array_size):
    for index in range(array_size):
        numbers = int(input(f"Enter number to be inserted at {index} position: "))
        list_of_numbers.append(numbers)
    
    return list_of_numbers

length_of_array = int(input("Enter the size of array to be created: "))
create_array(length_of_array)
print(f"Number list before shifting: {list_of_numbers}")
shifting_index = int(input("Enter the index from which the elements needs to be shifted: "))
array_shifting(shifting_index, list_of_numbers)
print(f"Number list After Shifting: {list_of_numbers}")