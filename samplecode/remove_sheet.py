from openpyxl import load_workbook

wb = load_workbook('14.checklist.xlsx')

for ws in wb.worksheets:
    if ws.title.startswith('作業用_'):
        wb.remove(ws)

wb.save('14.checklist_changed.xlsx')
