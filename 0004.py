# _*_ coding: utf-8 _*_
# if there is file is writen all by English
# count the number of each word that has been in this file
import re

test_file = open('source/0004_test.txt', 'r')
str = test_file.read()
#function str has formed a list of all string in the file as is showing below.
'''
for i in str[:20]:
    print(i)
'''

pat = re.compile('\b?(\w+)\b?')
words = pat.findall(str)
#now words has become a list filled with all the word in the file.
#there is anothe for the word searching process(using the re mudule in another way)

#  words = re.findall(r'\w+', str) 
#for i in another_words[:10]:
#    print(i)

wordsDict = dict()
for word in words:
    if word.lower() in wordsDict:
        wordsDict[word.lower()] += 1
    else:
        wordsDict[word.lower()] = 1
        # I was thinking if alice is in {'Alice': 'jack'} >>> False


for key, value in wordsDict.items():
    print('%s: %s' % (key, value))
    
#ansList = sorted(wordsDict.items(), key=lambda t: t[1], reverse=True)
#print(ansList)   # ansList now are a list of tuples made by words and its count.
#print(ansList[1])


'''
>>> dic = {'Jack': 'hello'}
>>> 'hello' in dic
False
>>> 'jack' in dic
False
>>> 'Jack'in dic
True
'''
# we should notice that upper and lower is quite different in python dic.
# and the result will be different if we do things differently


'''
wordsDict = dict()
for word in words:
    if word.lower() in wordsDict:
        wordsDict[word.lower()] += 1
    else:
        wordsDict[word.lower()] = 1
        # I was thinking if there is a word in 

for key, value in wordsDict.items():
    print('%s: %s' % (key, value))
if: 1
you: 23
are: 8
looking: 1
for: 2
someone: 3
can: 7
pour: 1
out: 3
your: 4
love: 10
to: 24
let: 1
me: 1
suggest: 1
the: 25    # here we got 25
empowered: 14
'''
'''
wordsDict = dict()
for word in words:
    if word in wordsDict:
        wordsDict[word] += 1
    else:
        wordsDict[word] = 1
        # I was thinking if there is a word in 

for key, value in wordsDict.items():
    print('%s: %s' % (key, value))
If: 1
you: 23
are: 8
looking: 1
for: 2
someone: 3
can: 7
pour: 1
out: 3
your: 4
love: 10
to: 24
let: 1
me: 1
suggest: 1
the: 22  # but here we got 22, and maybe we will find a The: 3
empowered: 14
'''
