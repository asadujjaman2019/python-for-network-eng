import openpyxl

wb = openpyxl.load_workbook('e:/ACI-Contracts.xlsx')
ws = wb.active

data=[ws.cell(row=i,column=2).value for i in range(2,12)]
print(data)