fh = open('mbox-short.txt') #opening file in fil handler
dic = {} #init a dictionary
lis = list() #init a list
for line in fh:
    if line.startswith('From') and not line.startswith("From:"):
        line = line.strip() #to remove leading and trailing spaces
        x = line.split() #splitting and converting into list
        #print(x[1]) #to print second element in list
        lis.append(x[1]) # appending to initiated list
#print(lis)

for email in lis:
    dic[email] = dic.get(email, 0) + 1 # to count the words in dict
print(dic)

max_count = None #initiating two variables to none to find max and min
max_word = None
min_count = None
min_word = None
for k, v in dic.items(): #iterating through key value pairs in DICT
    if max_count is None or max_count < v:
        max_count = v
        max_word = k
    elif min_count is None or min_count > v:
        min_count = v
        min_word = k
print(max_word, max_count,'\t', min_word, min_count)
# done
