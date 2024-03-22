'''
This file will calculate the final word count in the given string.

Example:

string_input = "Hello World"

output = 5 
(since word "World" has 5 characters, excluding spaces)

'''

string_input = "Hello World Milan"
print(len(string_input))
stripped_string = string_input.replace(" ", "")
print(len(stripped_string))