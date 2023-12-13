# Input: nums = [3,2,3]
# Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
x = {}
for num in nums:
    if num not in x:
        x[num] = 1
    else:
        x[num] += 1

# maxValue = max(x.values())
maxKey = max(x, key=x.get)

print(maxKey)
