file = input("Enter file name:")
fh = open(file)
count = 0
tot = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip()
        x = line.split(": ") # used to split a line with a seperator
        count = count + 1
        y = float(x[1])
        tot = tot + y
        print(y)
#print(type(float(x[1]))) # syntax to print the type

av = tot/count
print("total count:", count, "Sum of float:", tot)
print("Average spam confidence:",av)
