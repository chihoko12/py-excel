from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

wb = load_workbook('16.quote.xlsx')

# protect a workdbook
wb.security = WorkbookProtection(
    workbookPassword='test', lockStructure=True)

wb.save('16.quote1_changed.xlsx')
