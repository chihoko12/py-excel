from datetime import date
from openpyxl import load_workbook

wb = load_workbook('15.minutes.xlsx')
for ws in wb.worksheets:
    ws.sheet_view.tabSelected = None

ws_template = wb['template']
ws_copy = wb.copy_worksheet(ws_template)

today = date.today()
ws_copy.title = f'{today:%Y-%m-%d}'

# move the copied sheet to the first
wb.move_sheet(ws_copy, offset=-wb.index(ws_copy))

# select the first sheet
wb.active = 0
wb.save('15.minutes_changed.xlsx')
