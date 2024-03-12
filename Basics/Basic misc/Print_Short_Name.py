# Input: Milan Ravi Patel
# Output: M.R Patel

# Function definition
def short_name(firstname, middlename, lastname)-> str:
    output = firstname[0] + "." + middlename[0] + " " + lastname
    return output
    


# Input
first_name = input("Enter your First Name: ")
middle_name = input("Enter your Middle Name: ")
last_name = input("Enter your Last Name: ")
results = short_name(first_name, middle_name, last_name)
print(results)