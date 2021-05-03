lis = [2,3,6,6,5]
lis.sort()
print(lis[0])
for i in range(len(lis)):
    if lis[i] < lis[0]:
        print(lis[i])
        break
    else:
        continue  
