# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup
import os

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('failed')

def savePics(html, rpath):
    if not os.path.isdir(rpath):
        os.mkdir(rpath)
    soup = BeautifulSoup(html, 'html.parser')
    #pics = soup.find_all('img', width="500")
    pics = soup.find_all('img', attrs={'width':'506'})
    '''
    for i in pics[:5]:
        print(i)
    '''
    for img_url in pics:
        img_src = img_url['src']
        with open(rpath + os.path.split(img_src)[1], 'wb') as f:
            f.write(requests.get(img_src).content)
    print('Pics saved')
        
    
def main():
    target_url = 'https://tieba.baidu.com/p/4127610206' 
    rpath = 'source/0013_copy2/'
    html = getHTMLText(target_url)
    savePics(html, rpath)

main()

