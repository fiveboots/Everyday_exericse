# _*_ coding: gbk _*_

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
    pics = soup.find_all('img', bdwater="杉本有美吧,1280,860")
    '''
    for i in pics[:5]:
        print(i)
    '''
    for img_url in pics:
        img_src = img_url['src']
        with open(rpath + os.path.split(img_src)[1], 'wb') as f:
            f.write(requests.get(img_src).content)
            f.close()
    print('Pics saved')
        
    
def main():
    target_url = 'http://tieba.baidu.com/p/2166231880' 
    rpath = 'source/0013/'
    html = getHTMLText(target_url)
    savePics(html, rpath)

main()
