sample1_data = open('Sample-1.txt')
sample2_data = open('Sample-2.txt')

str = ''

sample1_lis1 = []
sample1_lis2 = []
sample2_lis1 = []
sample2_lis2 = []


for word in sample1_data:
    word = word.strip()
    x = word.split('.')
    for i in x:
        if i is not str:
            sample1_lis1.append(i)

for i in sample1_lis1:
    y = i.split()
    for j in y:
        sample1_lis2.append(j)


dic1 = {}

for word in sample1_lis2:
    dic1[word] = dic1.get(word, 0) + 1

print(dic1)

keys1_count = len(dic1.keys())
print(keys1_count)
print('-------------------------------------------------')
for word in sample2_data:
    word = word.strip()
    x = word.split('.')
    for i in x:
        if i is not str:
            sample2_lis1.append(i)

for i in sample2_lis1:
    y = i.split()
    for j in y:
        sample2_lis2.append(j)

dic2 = {}

for word in sample2_lis2:
    dic2[word] = dic2.get(word, 0) + 1

print(dic2)

keys2_count = len(dic2.keys())
print(keys2_count)
print('---------------------------------------------------')

key_max = max(keys1_count, keys2_count)
print(key_max)

print('---------------------------------------------------')

lis_ex = []
for k, v in dic1.items():
    for key, value in dic2.items():
        if k == key and v == value:
            lis_ex.append(k)

print(lis_ex)
print('----------------------------------------------------')

count = 0

for i in lis_ex:
    count = count +1

print(count)
print('--------------------------------------------------')


per = (count/key_max)*100

print(per)

result = None


if per == 0:
    result = 0
elif per > 0 and per <= 25:
    result = 0.3
elif per > 25 and per <= 50:
    result = 0.6
elif per > 50 and per <= 75:
    result = 0.8
elif per > 75 and per < 100:
    result = 0.9
else:
    result = 1

print('---------------------------------------------------')

print(result)
