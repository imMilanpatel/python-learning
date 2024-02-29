'''
Input : III
Output : 3
Explanation --> III == 3

'''

# Roman numbers equivalents in Integers
romans_numerics = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

# Function with the actual logic
def roman_numbers_to_integers(Roman_Number):
    '''
    This method will convert Roman Numbers to Integers.
    Please provide your inputs in Roman Numerics only.

    '''
    total = 0

    for input_charcters in range(len(Roman_Number)):
        try:
            curr_index = input_charcters
            curr_value = romans_numerics[Roman_Number[curr_index]]
            next_value = romans_numerics[Roman_Number[curr_index+1]]
            print(curr_value)
            print(next_value)

            if curr_value < next_value:
                total -= curr_value
            else:
                total += curr_value

        except IndexError:
            pass
        
    return print(total)

# Input
Roman_num = input("Enter the Roman Number: ")
Integer_num = roman_numbers_to_integers(Roman_num)