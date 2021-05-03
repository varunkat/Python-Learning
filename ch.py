

string1 = 'friends'
string2 = 'finderss'


def dups(string1, string2):
    s1 = sorted(string1)
    s2 = sorted(string2)

    dic1 = {}
    dic2 = {}

    for i in s1:
        dic1[i] = dic1.get(i, 0) + 1
    for j in s2:
        dic2[j] = dic2.get(j,0) + 1


    print(dic1)
    print(dic2)


    ct = 0
    for k in dic2.keys():
        ct =ct + 1
    print(ct)

    count = 0
    for k,v in dic2.items():
        if k in dic1.keys() and v in dic1.values():
            count = count+1

    if ct != count:
        return False
    else:
        return True
    

print(dups(string1, string2))
