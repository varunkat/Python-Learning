nums = [5,7,7,8,8,10,11,12]
tgt = 8
res = [3,4]


i = len(nums)

index = int(i/2)

start = 0
end = 0
lis = []
if nums[index] == tgt:
    for i in range(index):
        if nums[index-i] == nums[index]:
            start = index-i
        if nums[index+i] == nums[index]:
            end = index+i
    lis.append(start)
    lis.append(end)
print(lis)
