points = [[1,1], [2,2], [3,3]]


dic1 = {}
lis1 = []
p1 = []
val = []

for i in range(len(points)):
    for j in range(len(points)):
        if i == j:
            continue
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[j][0]
        y2 = points[j][1]
        t1 = [x1,y1]
        t2 = [x2,y2]
        #if (t1,t2) not in p1 or (t2,t1) not in p1:
        p1.append((t1,t2))
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        lis1.append(dist)
        dic1[dist] = dic1.get(dist, 0) + 1
for k,v in dic1.items():
    val.append(v)
print(dic1)
print(lis1)
print(p1)
print(int(max(val)/2))
#447. Number of Boomerangs
