hours = input("Enter the total hours:") #input takes in string format
for i in range(0,100) :  #defining range for executing loop, is there a better way?
    if float(hours) < 10 : #four spaces for indented block
        print("Working hours are less, please enter again")
        hours = input("Enter the total hours:")
rate = input("Enter the rate:")
for j in range(0,100) :
    if float(rate) < 10 :
        print("Pay is too less, please enter again")
        rate = input("Enter the rate:")
comp = float(hours) * float(rate) #converting string to float
print("Final compensation:",comp)
