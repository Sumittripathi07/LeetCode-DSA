# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


nums1 = [1, 2]
nums2 = [3, 4]

nums = nums1 + nums2
nums.sort()

if len(nums) % 2 != 0:
    centerIndex = len(nums) // 2
    print(nums[centerIndex])
else:
    middle1 = nums[len(nums) // 2 - 1]
    middle2 = nums[len(nums) // 2]
    print((float(middle1) + float(middle2)) / 2.0)
