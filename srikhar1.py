import json


f = open('EmployeeData.json')
data = json.load(f)

lis1 =[]
lis2 =[]
lis3 =[]
lis4= []

for dict in data:
    if dict['liveLocation'] is not None:
        x = dict['id']
        lis1.append(x)
        y=dict['name']
        lis2.append(y)
        z=dict['email']
        lis3.append(z)
        a=dict['creditBalance']
        lis4.append(a)


final_list = []
for i in range(len(lis1)):
    tuple = (lis1[i], lis2[i], lis3[i], lis4[i])
    final_list.append(tuple)


for i in final_list:
    print(i)
final_list.sort(key = lambda x:x[1])
print("_____________________________________________________")
for j in final_list:
    print(j)
