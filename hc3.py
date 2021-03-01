
str2 = input()
A = input()
B = input()



lis2 = set(str2.split(' '))

set_A = set(A.split(' '))
set_B = set(B.split(' '))

happy = 0

for i in set_A:
    if i in lis2:
        happy = happy + 1

for j in set_B:
    if j in lis2:
        happy = happy - 1

print(happy)
