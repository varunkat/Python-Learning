classx = None
for i in [1,2,87,6,56]:
    if x is None:
        x = i
    if i > x:
        x = i
    print(i, x)
print('max:',x)


zork = 0 # This is used to calculate the total sum of list
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
