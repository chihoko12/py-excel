from openpyxl import Workbook

count = input('The number of worksheets to be created: ')

wb = Workbook()
ws = wb.active
ws.title = 'overview_1'

for i in range(2, int(count) + 1):
    wb.create_sheet(title=f'overview_{i}')

wb.save(f'reference.xlsx')
