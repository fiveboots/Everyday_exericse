import xlwt
from datetime import datetime
import string
import random

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0,00')
style1 = xlwt.easyxf(num_format_str='h:mm AM/PM')
style2 = xlwt.easyxf(num_format_str='general')

wb = xlwt.Workbook()

ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(),style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

ws2 = wb.add_sheet('B Test Sheet')
for x in range(5):
    for y in range(5):
        a = random.choice(string.digits)
        ws2.write(x, y, a)

for i in range(5):
    ws2.write(5, i, xlwt.Formula("A4+A5"))
'''
for i in range(5):
    for le in ["A", "B", "C", "D", "E"]:
        ws2.write(4, i, xlwt.Formula(le+ "3+" + le + "4"))
'''
#wb.save('0014_xlwt_examples.xls')
rpath = 'source/0014_xlwt'
wb.save(rpath + '/examples3.xls')
