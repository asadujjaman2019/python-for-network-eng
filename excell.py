import openpyxl

wb = openpyxl.load_workbook('e:/ACI-Contracts.xlsx')
ws = wb.active

values = [ws.cell(row=1,column=i).value for i in range(1,ws.max_column+1)]
print(values)