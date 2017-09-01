# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup


url = 'http://linyii.com'
def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text

html = getHTMLText(url)
soup = BeautifulSoup(html, 'html.parser')
hrefs = soup.find_all('a')
for a in hrefs:
    print(a['href']) # for the tag a, now its attrs is serving as a dict, so, ['href'] will show its values.
    print(a.text) 
    #print(a.attrs['href'])

