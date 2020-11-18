fh = open('mbox-short.txt')
count = 0
for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        line = line.strip()
        #print(line)
        x = line.split()
        count = count + 1
        print(x[1])
print(count)
