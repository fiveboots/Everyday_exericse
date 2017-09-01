# _*_ coding: utf-8 _*_
#[
#	[1, 82, 65535], 
#	[20, 90, 13],
#	[26, 809, 1024]
#]
import os, json, xlwt

root = 'source/0016/'
filename = 'numbers.txt'
fpath = os.path.join(root, filename)
print(fpath)
with open(fpath, 'r') as f:
    data = json.load(f)
    wb = xlwt.Workbook()
    
    sheet1 = wb.add_sheet('numbers', cell_overwrite_ok=True)
    
    for index, numbers in enumerate(data):
        # we can print the index and the numbers. numbers are three list with 
        # different index
        # print(index, numbers)
        for i, number in enumerate(numbers):
            sheet1.write(index, i, number )
    wb.save(root + 'numbers.xls')
    '''
    for index, numbers in enumerate(data):
        for number in numbers:
           print(index, i, number)
    '''
