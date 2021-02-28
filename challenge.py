keyName = ['daniel', 'daniel', 'daniel', 'luis', 'luis', 'luis', 'luis', 'steve', 'steve', 'steve']
keyTime = ['10:40', '10:00', '11:00', '09:00', '14:10', '15:00', '14:40', '08:00', '17:10', '17:20']

'''10:00-11:00 is considered one hour'''

lis = []

#always iterate through index not value

for i in range(len(keyName)):
    t = (keyName[i], keyTime[i])
    lis.append(t)

lis.sort(key = lambda x:x[1])
print(lis)


count = 0
name= []
time_hrs= []
time_mts = []


for i in lis:
    name.append(i[0])
    time_hrs.append(int(i[1].split(':')[0]))
    time_mts.append(int(i[1].split(':')[1]))

print(name)
print(time_hrs)
print(time_mts)

lis2 = []
for j in range(len(name)-1):
    if name[j] == name[j+1]:
        count = count + 1
        if count == 2:
            h = time_hrs[j-1]
            h1 = time_hrs[j+1]
            m = time_mts[j+1]
            if h1 - h == 1 and m == 0:
                lis2.append(name[j+1])
                count = 0

print(lis2)
