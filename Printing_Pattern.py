'''
Print the following Pattern

*
**
***
****
*****

'''

# Input
rows_to_be_printed = 5

# Milan Patel's version
# Version 1 using normal for loop

for stars in range(1, rows_to_be_printed + 1):
    print("*" * stars)

# Version 2 using one line for loop using join method
print('\n'.join('*' * stars for stars in range(1, rows_to_be_printed + 1)))




