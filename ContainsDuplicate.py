# Input: nums = [1,2,3,1]
# Output: true


nums = [1,2,3,1]
nums.sort()
n = len(nums)
for i in range(1, n):
    if nums[i] == nums[i - 1]:
        print(True)
print(False)