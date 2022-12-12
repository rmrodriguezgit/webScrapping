from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

# Seleccionar 3 sitios web
# html.read()

html = urlopen('https://www.msn.com/es-mx')
print(html.read())

