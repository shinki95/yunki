from xlrd import open_workbook

wb = open_workbook('contact.xlsx')
ws = wb.sheet_by_index(0)

name = []
phone_number = []
major = []

for row in range(1, 4):
    name.append(sheet.cell(row,0))
    phone_number.append(sheet.cell(row,1))
    major.append(sheet.cell(row,2))

information = list(zip(name, phone_number,major))
contact = dict(zip(name,information))
contact[input("what's your name: ")]