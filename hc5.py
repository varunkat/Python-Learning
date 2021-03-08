'''INPUT

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1


----------------------

OUTPUT

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12'''


N = int(input().split()[0])

print('enter K')
K = int(input())

lis = []
for i in range(N):
    val = input().split()
    lis.append(val)

print(lis)

lis.sort(key = lambda x:int(x[K]))

for i in lis:
    print(i)
