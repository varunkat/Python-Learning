'''2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

25200
88200'''

from datetime import datetime
num = int(input())
for _ in range(num):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))

'''num = int(input())
final_list = []
for i in range(num):
    str1 = input()
    str2 = input()

    day = []
    tzone = []
    day.append(str1.split()[1])
    tzone.append(str1.split()[5])
    day.append(str2.split()[1])
    tzone.append(str2.split()[5])

    x = int(tzone[0])
    y = int(tzone[1])

    res = abs(x+y)/100

    d1 = int(day[0])
    d2 = int(day[1])

    diff = d1-d2

    if diff == 0:
        secs = res*3600
    else:
        min = str(res).split('.')[1]
        secs = diff*24*3600 + int(min)*600
    final_list.append(int(secs))

print(final_list)'''
