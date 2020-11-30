#Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]



logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs_d = []
logs_l = []
for st in logs:
    if st.split(" ")[1].isdigit():
        logs_d.append(st)
    else:
        logs_l.append(st)

print(logs_l)


for x in logs_d:
    i = 1
    for i in x:
        logs_d.sort(key = i)

print(logs_d)


return sorted(logs_l,key = lambda x:(x.split()[1:],x.split()[0])) + logs_d  #code fusing lambda
