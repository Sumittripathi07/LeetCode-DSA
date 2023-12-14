# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
numCount = nums.count(val)
for i in range(numCount):
    nums.remove(val)
print(len(nums))
