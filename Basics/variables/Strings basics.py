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
input_string = "Hello Python learners, Let's start our learnings"
each_character(input_string)

#########################################################


# 2. Create a string & find the length of it.
# Using inbuild function
lenght = len(input_string)
print(f"String length found using inbuilt function is {lenght}")

# Using for loop and a method
def string_length(string):
    str_len = 0
    for characters in string:
        str_len  += 1
    print(f"String length calculated using custom method is {str_len}")

string_length(input_string)

# Using Join method and without for loop
def string_length_cal(string):
    str_len = sum(1 for _ in ''.join(string))
    print(f"String length calculated using join method without for loop is {str_len}")

string_length_cal(input_string)

#############################################################################################

# 3. Print a string with different predefined variables in it.
name = "Milan Patel"
age = 27
city = "Tiruchirappalli,Tamilnadu,India"

# Using f-string
f_string_result = f"Hello, my name is {name}, I am {age} years old, and I live in {city}."
print(f_string_result)

# Using format method
format_method_result_ = "Hello, my name is {}, I am {} years old, and I live in {}.".format(name, age, city)
print(format_method_result_)

#############################################################################################

# 4. Write a program that adds 'ing' to every string.
def add_ing_to_strings(strings):
    modified_strings = [s + 'ing' for s in strings]
    return modified_strings

# Example usage:
input_strings = ["read", "kiss", "swim", "play"]
result_strings = add_ing_to_strings(input_strings)

# Print the output
print("Original strings:", input_strings)
print("Strings with 'ing':", result_strings)

##############################################################################################

# 5. Write a program that replaces every 's' in a string with a '$'
modified_string = input_string.replace("s","$")
print(f"Actual Input String {input_string}")
print(f"Modified Input String {modified_string}")

###############################################################################################