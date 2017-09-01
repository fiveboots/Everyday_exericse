# _*_ coding: utf-8 _*_
#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
#假设内容都是英文，请统计出你认为每篇日记最重要的词

import re
import os

def findword(fpath, pat):
    if not os.path.isdir(fpath):
        print("We cannot find the path, please check it again")
    filelist = os.listdir(fpath)
    for fileName in filelist:
        filepath = os.path.join(fpath, fileName)
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.txt':
            with open(filepath) as f:
                #os.path.splitext(path)  
                #分割路径，返回路径名和文件扩展名的元组('source/0006\\nameofile', '.txt')
                data = f.read()
                words = pat.findall(data)
                wordsDict = dict()
                for word in words:
                    word = word.lower()
                    usual_list = ['a', 'the', 'to', 'is', 'of', 'in', 'and']
                    usual_list.extend(['she', 'he'])
                    if word in usual_list:
                        continue
                    if word in wordsDict:
                        wordsDict[word] += 1
                    else:
                        wordsDict[word] = 1
            anslist = sorted(wordsDict.items(), key=lambda t:t[1], reverse=True)
            #ansList = sorted(wordsDict.items(), key=lambda t: t[1], reverse=True)
            #print(ansList)   # ansList now are a list of tuples made by words and its count.
            #print(ansList[1]) # it will show the second tuple. the word and the count.

            print('file: %s -->the most word: %s' % (fileName, anslist[0]))
            
if __name__ == '__main__':
    fpath = 'source/0006'
    pat = re.compile('\d?(\w+)\d?')
    findword(fpath, pat)
