from openpyxl import load_workbook

wb = load_workbook('11.summary.xlsx')

for i, ws in enumerate(wb.worksheets):
    ws.title = 'ID_' + ws.title
    if (i + 1) % 10 == 0:
        ws.sheet_properties.tabColor = '0000FF'

wb.save('11.summary_changed.xlsx')
