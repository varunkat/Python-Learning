hours = input("Enter total work hours:")
rate = input("Enter hourly rate:")
h = float(hours)
r = float(rate)
if h > 40 :
    comp = 40*r + (h-40)*(r*1.5)#adding 1.5 times to rate above 40 hours work
else :
    comp = h*r
print('total Pay:',comp)
