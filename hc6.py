
string = 'aabbbccde'

dic = {}
for i in s:
    dic[i] = dic.get(i,0) + 1


x = sorted(sorted(dic.items(), key = lambda x:x[0]), key = lambda x:x[1], reverse = True)



for i in x[0:3]:
    print(i[0], i[1])
