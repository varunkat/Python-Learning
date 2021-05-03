from collections import deque


days = 1
day = []

for i in range(len(T) - 1):
    if T[i+1] > T[i]:
        days = 1

    else:
        value = T[i]
        value1 = max(T[i+1:])
        for t in T[i+1:]:
            if t <= value and value1 > value:
                days = days + 1
            if t <= value and value1 < value:
                days = 0
            if t > value:
                break

    day.append(days)
    days = 1

days = 0
day.append(days)
print(day)
'''T = [89,62,70,58,47,47,46,76,100,70]
N = len(T)
if N==0:
    output = []
elif N==1:
    output = [0]

stack = deque()
output = [0]*N
stack.append(0)
for i in range(1, N):
    while(stack and T[i] > T[stack[-1]]):
        elem = stack.pop()
        print(elem)
        output[elem] = i-elem

    stack.append(i)
print(output)'''
