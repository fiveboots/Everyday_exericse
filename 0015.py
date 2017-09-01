# _*_ coding: utf-8 _*_

#��0015�⣺ ���ı��ļ� city.txtΪ������Ϣ, ��������ݣ����������ţ�������ʾ��
#{
#    "1" : "�Ϻ�",
#    "2" : "����",
#    "3" : "�ɶ�"
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
        
