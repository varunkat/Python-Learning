

'''lis_red = []
lis_white = []
lis_blue = []
for i in nums:
    if i == 0:
        lis_red.append(i)
    elif i == 1:
        lis_white.append(i)
    elif i == 2:
        lis_blue.append(i)

print(lis_red)
print(lis_white)
print(lis_blue)

final = lis_red+lis_white+lis_blue
print(final)'''

nums = [2,0,2,1,1,0]
def sortcolors(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = nums[j]
            nums[j] = 0
            j =j+1
    for i in range(j, len(nums)):
        if nums[i] == 1:
            nums[i] = nums[j]
            nums[j] = 1
            j = j+1
    for i in range(j, len(nums)):
        nums[i] = 2
    return nums

print(sortcolors(nums))
