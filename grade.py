score = input("Enter the score for grade:")
try :
    s = float(score)
    if s >= 0.0 and s <= 1.0 :
        if s >= 0.9 :
            print('A')
        elif s >= 0.8 :
            print('B')
        elif s >= 0.7 :
            print('C')
        elif s >= 0.6 :
            print('D')
        else :
            print('F')
    else :
        print('Note: Value entered is out of range, Please enter between 0.0 and 1.0')
except :
        print('Note: Value entered is not a numeric, Please enter numeric value')
