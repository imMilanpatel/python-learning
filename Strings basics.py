'''
This file contains basic files to learn and practise about strings.
Taken from: https://github.com/inspirezonetech/TeachMePythonLikeIm5/blob/main/variables/strings.py
Solutions will be based on the challenges mentioned in the above repo only.

'''

# Challenge:1. Create a string & print out each character individually.

# Method to printout each character of a string individually.
'''
# Using for loop
def each_character(string):
    for character in string:
        print(character)
'''
# Using Join Function
def each_character(string):
    print('\n'.join(string))

# Input String for the challenge 1
input_string = "Hello Python learner"
each_character(input_string)

# Input String for the challenge 1
input_string = "Hello Python learner"
each_character(input_string)

#########################################################


# 2. Create a string & find the length of it.
# Using inbuild function
lenght = len(input_string)
print(f"String lenth found using inbuilt function is {lenght}")

# Using for loop and a method
def string_length(string):
    str_len = 0
    for characters in string:
        str_len  += 1
    print(f"String lenght calculated using custom method is {str_len}")

string_length(input_string)

# Using Join method and without for loop
def string_length_cal(string):
    str_len = sum(1 for _ in ''.join(string))
    print(f"String length calculated using join method without for loop is {str_len}")

string_length_cal(input_string)





# 3. Print a string with different predefined variables in it.
# 4. Write a program that adds 'ing' to every string.
# 5. Write a program that replaces every 's' in a string with a '$'