# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://www.python123.io/ws/demo.html'
def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text

html = getHTMLText(url)
soup = BeautifulSoup(html, 'html.parser')
print(soup.body.text)
hrefs = soup.find_all('a')
for a in hrefs:
    print(a['href'])
    print(a.attrs['href'])

