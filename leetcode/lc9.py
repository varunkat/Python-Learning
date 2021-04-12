A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
c = [40,40]
d = [40,40]

dic = {}
for i in range(len(c)):
    dic[c[i]] = i

lis1 = []
for i in d:
    for k,v in dic.items():
        if i == k:
            lis1.append(v)

print(lis1)
