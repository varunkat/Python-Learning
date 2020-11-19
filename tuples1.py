fh = open('mbox-short.txt')
lis = list()
lis1 = list()
dic = dict()
for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        line = line.strip()
        x = line.split()
        y = x[5] #assigning list value to string value
        z = y.split(":")
        lis.append(z[0])

for hour in lis:
    dic[hour] = dic.get(hour, 0) + 1 # counting the occurances of numbers and storing in dict

for k, v in dic.items():
    final = (k,v)
    lis1.append(final)

lis2 = sorted(lis1)
for i, j in lis2:
    print(i,j)
