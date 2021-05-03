S = '1222311'

lis = []
count = 1
for i in range(len(S) - 1):

    if S[i] == S[i+1]:
        count = count+1
        if i == (len(S) - 2):
            T = (count, int(S[i]))
            lis.append(T)
    else:
        T = (count, int(S[i]))
        lis.append(T)
        count = 1

print(*lis)


a=input()
s=''
for i in range(0,len(a)):
    if i!=0:
        if a[i]==a[i-1]:
            continue
    p=0
    for j in range(i,len(a)):
        if a[i]==a[j]:
            p+=1
        else:
            break
    s+='('+str(p)+', '+a[i]+')'+' '
print(s)
