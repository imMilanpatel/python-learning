# This file will read data from an XML file


# Imports
import pandas

#Thing to search
item = "Manchow Soup"


#File Read
file = "E:\GitRepos\python-learning\File_RW\XML\Menu.xml"

# reading the file
menu_df = pandas.read_xml(file, parser="etree")
print(menu_df)

# Check if "item" is in the DataFrame
has_item = f"{item}" in menu_df["ItemName"].values
price_of_item =  menu_df.loc[menu_df['ItemName'] == f'{item}', 'Price'].values[0]


# Assert if "Manchow Soup" is in the menu
assert has_item, f"{item} is not in the menu."
print(f"{item} is in the menu and it's price is {price_of_item}.")
