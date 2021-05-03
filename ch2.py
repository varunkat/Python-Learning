users = {
'user1' : ['book1', 'book2', 'book3'],
'user2' : [ 'book2'],
'user3' : [ 'book2']
}

lis = users['user1']
lis_set = set(lis)
new_set = None
for k,v in users.items():

    v_set = set(v)
    new_set = lis_set.intersection(v_set)
    lis_set = set(v)

new_lis = list(new_set)
print(new_lis)
