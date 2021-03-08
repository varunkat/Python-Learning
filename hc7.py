
import re
S = 'Sorting12340'

p1 = '[A-Z]'
p2 = '[a-z]'
p3 = '[0-9]'

s4 = []
if re.search(p1, S):
    s1 = re.findall(p1, S)
    s1.sort()
if re.search(p2, S):
    s2 = re.findall(p2, S)
    s2.sort()
if re.search(p3, S):
    s3 = re.findall(p3, S)
    s3.sort()
    for i in s3:
        s4.append(i)
    s4.sort(key = lambda x:int(x)%2 == 0)


final = s2+s1+s4

print(final)

final_str = ''
for i in final:
    final_str+= i

print(final_str)
