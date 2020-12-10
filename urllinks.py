

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

ct = input('Enter Count: ') #input for total repetitions
pos = input('Enter Position: ')#input for retrieving url at specific position
y = int(pos) - 1 #index to access element in list
lis = [] #initializing a list
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    x = tag.get('href', None)
    lis.append(x) #appending tags to list

print('Retrieving:' ,url)
print('Retrieving:' ,lis[y])

i = 1
for i in range(1,int(ct)): #declaring range for loop with count
    html = urllib.request.urlopen(lis[y], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    lis.clear()#clearing list to append new URL's
    tags = soup('a')
    for tag in tags:
        x = tag.get('href', None)
        lis.append(x)
    print('Retrieving:' ,lis[y])

lis.clear() #clearning list and freeing up space after executions
