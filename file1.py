while True:
    fname = input("enter file name:")
    if fname == 'exit' :
        quit()
    else :
        count = 0
        count1 = 0
        count2 = 0
        try :
            fhandle = open(fname)
            for line in fhandle :
                count1 = count1 + 1
                if line.startswith('From:') :
                    count = count + 1
                    print(line)
                elif line.startswith('Received:') :
                    count2 = count2 + 1
        except :
            print("cant open file name:", fname)
            quit()

        print("Count for from is:", count)
        print("Count for Received is:", count2)
        print("the total count is:", count1)
