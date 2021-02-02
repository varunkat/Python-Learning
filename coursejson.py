import json
import requests
import urllib.request, urllib.parse, urllib.error
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
dat = data.decode()
data1 = eval(dat) #used to convert string into dictionary
final_data = data1['comments']

count = 0
lis1 = []

for i in final_data:
    x = i['count']
    count = count + 1
    lis1.append(x)

#print(lis1)
print('Count:', count)

sum = 0
for j in lis1:
    y = int(j)
    sum = sum + j

print('Total:', sum)
