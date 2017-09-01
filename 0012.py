# _*_ coding: gbk _*_

#���д��ı��ļ� filtered_words.txt�����������Ϊ�������ݣ�
# ���û��������дʣ���ӡFreedom, �����ӡ�����ʻ�
import os

word_filter = set()
fpath = 'source/0012/filtered_words.txt'
if not os.path.exists(fpath):
    print('Sorry, we cannot find the file, please check it again.')
with open(fpath) as f:
    for line in f.readlines():
        word_filter.add(line.strip())

while True:
    s = input()
    if s == 'quit':
        break
    for w in word_filter:
        if w in s:
            s = s.replace(w, '#' * len(w))
    print(s)

