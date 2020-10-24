from openpyxl import load_workbook

wb = load_workbook('13.checklist.xlsx')

for ws in wb.worksheets:
    # ungroup selected sheets before selecting only one sheet
    ws.sheet_view.tabSelected = None

ws_matome = wb['まとめ']
wb.move_sheet(ws_matome, offset=-wb.index(ws_matome))

# select the first sheet
ws.active = 0
wb.save('13.checklist_top_changed.xlsx')
