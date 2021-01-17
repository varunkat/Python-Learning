import re

emails = open("email.txt")
def emailchecker(emails):
    l1 = []
    regex = '^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #regex to check valid email address
    for i in emails:
        x = i.strip() #string format to remove leading and trailing spaces
        if(re.search(regex, x)): #checking with regex
            l1.append(x)
    l1.sort() #lists can be sorted
    print(l1)
    return

emailchecker(emails)
