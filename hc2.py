str = input()
num = int(input())

def tools(str, num):
    lent = len(str)
    s = int(lent/num)
    lis = []

    for i in range(s):
        x = str[0:num]
        y = ''
        for i in x:
            if i not in y:
                y = y+i
        lis.append(y)
        str = str[num:]
    for i in lis:
        print(i)
    #print(lent)
    #print(s)

tools(str,num)
