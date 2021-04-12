s = 'aaadbbcc'
key = 2
dic = {}
for i in s:
    dic[i] = dic.get(i, 0)+1
print(dic)
#dic1 = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1], reverse = True)}
dic1 = {k:v for k,v in sorted(dic.items(), key = lambda x:(x[1], x[0]))}
print(dic1)
'''st = ''

print(len(s))


for i in range(key):
    for k, v in dic1.items():
            st = st+k

print(st)'''
