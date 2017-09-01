# _*_ coding: utf-8 _*_
# 将纯文本students.txt的信息写入到一个.xls 文件中
#{
#	"1":["张三",150,120,100],
#	"2":["李四",90,99,95],
#	"3":["王五",60,66,68]
#}

import os
from collections import OrderedDict
import json, xlwt

def file_path(fpath):
    if not os.path.isdir(fpath):
        os.mkdir(fpath)
    files = os.listdir(fpath)

    for fileName in files:
        file_path = os.path.join(fpath, fileName)
    return file_path
    
fpath = 'source/0014/'    
file_path = file_path(fpath)

with open(file_path, 'r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    
    wb = xlwt.Workbook()  # we creat a new .xls file as the name of wb
    
    #wb.add_sheet(name, **) then we can do all the work based on sheet1.
    sheet1 = wb.add_sheet('student', cell_overwrite_ok=True)
    for index, (key, values) in enumerate(data.items()):
        #print(index, key, values)
        
        sheet1.write(index, 0, key)
        for i, value in enumerate(values):
            sheet1.write(index, i+1, value)
        # here i is serving as a index.
        
    wb.save(fpath + 'students.xls')

