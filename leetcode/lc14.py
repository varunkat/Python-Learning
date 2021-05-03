#nums = [0,1,3,50,75]
nums = [-1]
lower = -2
upper = -1

rng = []
if nums == []:
    rng.append([upper,lower])

else:
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            x = nums[i] + 1
            y = nums[i+1] - 1
            rng.append([x,y])

    if nums[-1] < upper:
        x = nums[-1] + 1
        y = upper
        rng.append([x,y])
print(rng)
