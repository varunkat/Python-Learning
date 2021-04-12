candy = [1,1,1,1,2,2,2,3]

dic = {}
for i in candy:
    dic[i] = dic.get(i,0) + 1
print(dic)

n = int(len(candy)/2)

key_count = 0
for k, v in dic.items():
    key_count+= 1

if key_count > n:
    out = n
else:
    out = key_count

print(n)
print(out)
