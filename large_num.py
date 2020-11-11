x = None
for i in [1,2,87,6,56]:
    if x is None:
        x = i
    if i > x:
        x = i
    print(i, x)
print('max:',x)
