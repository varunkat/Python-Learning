def computepay(h,r):
    if h > 40:
        return 40*r + (h-40)*r*1.5
    else:
        return h*r

hrs = input("Enter total hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)

c = computepay(h,r)
print(c)
