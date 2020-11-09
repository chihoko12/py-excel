import logging
import sys

from openpyxl import Workbook

logging.basicConfig(filename='create_book.log',
                    level=logging.INFO,
                    format='%(asctime)s: [%(levelname)s %(message)s')
# log format
# https://docs.python.org/ja/3/library/logging.html#logrecord-attributes

logging.info('the process has started')
try:
    # get the number from user input
    count = sys.argv[1]
    for i in range(int(count)):
        wb = Workbook()
        ws = wb.active
        ws.title = 'overview'

        file_name = f'22.ref_{i + 1}.xlsx'
        wb.save(file_name)
        logging.info('the workbook was created: %s', file_name)

except Exception:
    logging.exception('exception happened')

logging.info('the process has done.')
