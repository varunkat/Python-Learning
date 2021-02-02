

import json


f = open('EmployeeData.json')
data = json.load(f)


lis1 = []
lis2 = []
lis3 = []
lis4 = []
count1 = 0
count2 = 0
for dict in data:
    if dict['liveLocation'] is not None:
        count1 = count1 + 1
        x = dict['id']
        lis1.append(x)
        y = dict['name']
        lis2.append(y)
        z = dict['email']
        lis3.append(z)
        a = dict['creditBalance']
        lis4.append(a)

merged_list = []
for i in range(len(lis1)):
    t = (lis1[i], lis2[i], lis3[i], lis4[i])
    merged_list.append(t)

merged_list.sort(key = lambda x: x[1] )
for i in merged_list:
    print(i)

sum = 0
for ct in lis4:
    sum = sum+ct

print('total credit:', sum)
