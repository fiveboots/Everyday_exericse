# _*_ coding: gbk _*_

#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词，打印Freedom, 否则打印正常词汇
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

