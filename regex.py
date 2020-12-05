import re
fhandle = open('regex_sum_1037047.txt') #opening file using file handler

num_list = [] #initiating a list

for line in fhandle:     #iterating through file handler
    line1 = line.strip()  #removing leading and trailing spaces
    lis2 = re.findall('[0-9]+', line1) #using regular expression to find all the matching expressions
    num_list = num_list+lis2 #Appending results to initiated list

#print(lis)

count = 0
for i in num_list: #iterating over list
    x = int(i) # converting string to integer
    count = count + x # calculating count

print(count) # printing final count
