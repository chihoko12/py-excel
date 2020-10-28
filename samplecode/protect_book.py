from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

wb = load_workbook('16.quotation.xlsx')

wb.security = WorkbookProtection(
  workbookPassword = 'test', lockStructure=True
)

wb.save('quotation1_changed.xlsx')
