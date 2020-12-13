import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')


print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)


results = tree.findall('comments/comment')
print('Count:', len(results))
#print(results) #Will give the list of comment tags
lis = []
for com in results:
    x = com.find('count').text
    lis.append(x)



count = 0
for i in lis:
    j = int(i)
    count += j

print('Sum:', count)

#print(lis)
lis.clear()
