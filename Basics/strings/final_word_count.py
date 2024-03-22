'''
This file will calculate the final word count in the given string.

Example:

string_input = "Hello World"

output = 5 
(since word "World" has 5 characters, excluding spaces)

'''

# Function definition

def last_word_count(str) -> int:
    count = 0
    for character in string_input[:: -1]:
        if character != " ":
            count += 1
        else:
            break
    return count

# Inputs
string_input = "Hello World"
print(f"Input: {string_input}")
stripped_string = string_input.replace(" ", "")

# Output
result = last_word_count(stripped_string)
print(f"Output: {result}")