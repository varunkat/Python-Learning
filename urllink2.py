# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

#extracting span attributes from link
set = soup.find_all('span', attrs = {'class':'comments'})


#Finding integer values from the extracted list
lis1 = []
for i in set:
    x = str(i)
    lis = re.findall('[0-9]+', x)
    lis1 = lis1+lis

#printing total count of list elements
print('Count', len(lis1))

#Finding total sum of integer values in the list
count = 0
for j in lis1:
    num = int(j)
    count = count + num

print('Sum', count)
