'''
This program will print the following pattern,

        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * * 

'''

def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print("  " * (rows - i), end="")
        
        # Print stars
        print("* " * (2 * i - 1))

# Define the number of rows for the pattern
rows = 10

# Call the function to print the pattern
print_pattern(rows)
