'''
This file will calculate the final word count in the given string.

Example:

string_input = "Hello World"

output = 5 
(since word "World" has 5 characters, excluding spaces)

'''

string_input = "Hello W"
stripped_string = string_input.replace(" ", "")

count = 0
for characters in string_input[:: -1]:
    if characters != " ":
        count += 1
    else:
        break

print(count)