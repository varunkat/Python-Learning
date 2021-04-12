lis = []
def fun(lis, func):
    for i in lis:
        print(func(i))


lis = [1,2,3]

fun(lis, lambda x:x+1)
