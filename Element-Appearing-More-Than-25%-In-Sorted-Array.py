# Element Appearing More Than 25% In Sorted Array
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6


arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
x = {}
for ele in arr:
    if ele not in x:
        x[ele] = 1
    else:
        x[ele] += 1
print(max(x, key=x.get))
