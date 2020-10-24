from openpyxl import load_workbook

wb = load_workbook('13.checklist.xlsx')

# move this sheet one sheet back from the current position
wb.move_sheet('まとめ', offset=1)

wb.save('13.checklist_changed.xlsx')
