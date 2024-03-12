# This program will return the second highest element from the list

# Function definition
def second_highest(list_of_numbers)-> int:
    first_max = max(list_of_numbers)
    first_max_index = list_of_numbers.index(first_max)
    list_of_numbers.remove(first_max)
    second_max = max(list_of_numbers)
    list_of_numbers.insert(first_max_index-1,first_max)
    return second_max

# Input
number_list = [10,12,44,2,135,20,1,4124,120]
results = second_highest(number_list)
print(results)
print(number_list)