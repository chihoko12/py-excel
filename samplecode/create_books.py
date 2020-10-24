from openpyxl import Workbook

count = input('the number of workbooks to be created: ')
for i in range(int(count)):
    wb = Workbook()
    ws = wb.active
    ws.title = 'overview'
    wb.save(f'ref_{i + 1}.xlsx')
