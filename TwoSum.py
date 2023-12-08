# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [2,7,11,15]
target = 9
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i, j])