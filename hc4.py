vowels = ['a', 'e', 'i', 'o', 'u', 'y']

num = int(input())
words = list(input().split())


count = 0
score = 0
for word in words:
    for letter in word:
        if letter in vowels:
            count = count + 1
    print('ct',count)
    if count%2 == 0:
        score = score + 2
    else:
        score = score + 1
    count = 0
print(score)

 
