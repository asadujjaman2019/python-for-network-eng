import openpyxl

wb = openpyxl.load_workbook('e:/ACI-Contracts.xlsx')
ws = wb.active

print('Total number of rows: '+str(ws.max_row)+'. And total number of columns: '+str(ws.max_column))

print('The value in cell A1 is: '+ws['B1'].value)