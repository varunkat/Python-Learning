list = list()
fh = open('romeo.txt')
for i in fh:
    x = i.split()
    for j in x:
        if j not in list:
            list.append(j)
            list.sort()
print(list)
print(len(list))
