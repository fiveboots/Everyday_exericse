# _*_ coding: utf-8 _*_

#第0015题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
#{
#    "1" : "上海",
#    "2" : "北京",
#    "3" : "成都"
#}

import json, xlwt
import os

root = 'source/0015/'
name = 'city.txt'
fpath = os.path.join(root, name)

with open(fpath, 'r') as f:
    data = json.load(f)
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('name of cities', cell_overwrite_ok=True)
    for index,(key, value) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        sheet1.write(index, 1, value)
    
    wb.save(root + 'city.xls')
        
