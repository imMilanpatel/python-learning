# Read Excel and print only expected column


# Package Imports
import pandas as pd

# Read an EXCEL FILE
excel_file = pd.read_excel(r'C:\Users\47700236\Desktop\dummy.xlsx')

# Print only the Expected columns
column_data = pd.DataFrame(excel_file, columns= ['Fruit', 'Stock'])
print(column_data)

