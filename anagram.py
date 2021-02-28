s = 'mom'
lis = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        x = s[i:j]
        lis.append(x)
print(lis)
