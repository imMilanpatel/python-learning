# Simple file with a method to calculate the number of vowels in a string

# method to calculate vowels in a string.
''' 
If a string has repeated vowels then also it will be calculate.
Eg: Zoologist, here there are three "o" and those three will be calculated as individual only.
'''
def vowels_counter(string):
    vowels_list = ['a','e','i','o',"u"]
    vowel_counter = 0
    for characters in string:
        if characters in vowels_list:
            vowel_counter += 1
                
    return vowel_counter

# Input
input_string = "Zoologist"
vowel_count = vowels_counter(input_string)
print(f" Vowels count in the following string is/are {vowel_count}")