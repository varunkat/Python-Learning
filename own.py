fh = open('raw.txt')
lis = list()
cost = dict()
doc = dict()
for line in fh:
    line = line.strip()
    x = line.split(",")

    lis.append(x[1:5])



#doc[lis[2]].add(lis[0:2])
x = lis[2], y = lis[-1]
cost[x] = float(y)

print(cost)
