a = "apple apple"
b = "banana"
#Output: ["sweet","sour"]

x = None
y = None
lis = list()
lis1 = a.split()
lis2 = b.split()
lis3 = list()
print(lis1)
print(lis2)
lis = lis1 + lis2

for word in lis:
    if lis.count(word) == 1:
        lis3.append(word)

print(lis3)


#    for j in b:
#        j = j.split()
#        if i == j:
#            continue
#        else:
#            lis.append(i)
#            lis.append(j)
#print(lis)
