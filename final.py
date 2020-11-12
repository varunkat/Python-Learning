max = None
min = None
count = 0
while True:
    num = input('Enter the number:')
    if num == "done":
        break
    try :
        n = int(num)
        if max is None:
            max = n
        elif min is None:
            min = n
        elif n > max:
            max = n
        elif n < min:
            min = n
    except:
        print("enter Valid input!")
        continue

print(max, min)
print("All printed")
