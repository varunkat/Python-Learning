#1 dictionaries

d = {'ekniranjan':'prabhas',
'RRR':['ram','ntr'],
'dasara':'nani',
'bahubali':'anushka'}

keys = d.keys()
print(keys)
for i in keys:
    print(i)

values = d.values()
print(values)
for i in values:
    print(i)

items = d.items()
print(items)
for i in items:
    print(i)


val = d['bahubali'] #retrieve specific key values using dict
print(val)

val2 = d['RRR']
print(val2)

print(val2[0])

for k,v in d.items():
    if k == 'dasara':
        print(v)
    else:
        print('N/A')

lis = (1,2,3)
print(sum(lis))