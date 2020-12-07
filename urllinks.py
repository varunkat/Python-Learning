# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
x = input('Enter Position:')
print('Retrieving :', url)
t = int(x)
lis1 = []
for tag in tags:
    x = tag.get('href', None)
    lis1.append(x)



print('Retrieving :', lis1[t].get('href', None))


#print(lis1)
#print(type(tags))
