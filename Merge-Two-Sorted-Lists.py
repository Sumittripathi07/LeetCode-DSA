# Merge Two Sorted Lists
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


list1 = [1, 2, 4]
list2 = [1, 3, 4]
list1.extend(list2)
list1.sort()
print(list1)
