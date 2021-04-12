nums = [1,2,3,4]
final = []
res = 1
for i in range(len(nums)):
    lis = nums[:i]+nums[i+1:]
    for j in lis:
        res = res*j
    final.append(res)
    res = 1

print(final)
