# This file will mostly be empty and it is just to test the code components.
year_ranges = {
    (1600, 1699): 6,
    (1700, 1799): 4,
    (1800, 1899): 2
}

'''
# Get user input
user_input = int(input("Enter a year: "))

# Check user input against year ranges
for year_range, value in year_ranges.items():
    print(year_range)
    if year_range[0] <= user_input <= year_range[1]:
        print(f"Value for the range {year_range}: {value}")
        break
else:
    print("Year not in any range.")
'''

year = 1600

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")