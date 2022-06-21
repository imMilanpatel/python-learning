# Python program to read an Excel file and filter out the expected data

# # Package imports
# import pandas as pd
#
# # Reads Excel file and the first workbook
# excel_worksheet_data = pd.read_excel(r'C:\Users\47700236\Desktop\dummy.xlsx', sheet_name=0)
#
# # Filtering dataframe
# excel_worksheet_data = excel_worksheet_data[(excel_worksheet_data['Price'] < 20 )]
#
# # Print the Filtered content
# print(excel_worksheet_data)



import csv
import xlrd

workbook = xlrd.open_workbook(r'C:\Users\47700236\Desktop\Apr22_Effort.xlsm')
for sheet in workbook.sheets():
    if sheet.name == "Effort":
        with open(r'C:\Users\47700236\Desktop\dummy.csv'.format(sheet.name), 'w+') as f:
            writer = csv.writer(f)
            for row in range(sheet.nrows):
                out = []
                for cell in sheet.row_values(row):
                    try:
                        out.append(cell.encode('utf8'))
                    except:
                        out.append(cell)
                writer.writerow(out)