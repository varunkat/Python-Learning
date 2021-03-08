s = 'cccaaa'

dic = {}
sort = {}
for i in s:
    dic[i] = dic.get(i,0) + 1

final = sorted(dic.values(), reverse = True)# will always dtores value in list
print(final)

for i in final:
    for v in dic.keys():
        if dic[v] == i:
            sort[v] = dic[v]

print(sort)


str = ''
for k, v in sort.items():
    for i in range(v):
        str = str + k

print(str)
