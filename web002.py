
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print('impresión div')
print(bs.div)
print('impresión body')
print(bs.body)
print('impresión h1')
print(bs.h1)
