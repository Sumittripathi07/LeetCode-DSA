# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# nums = [4, 4, 4, 4, 4, 1, 1, 1, 2, 2, 3]
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# sortedFreq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
# print(sortedFreq)

# final = []
# for i in range(k):
#     final.append(list(sortedFreq)[i])
# print(final)


# ----------------------------------------------------------------------------------------------
# Method 2

counts = {}
for num in nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

# 2: Sort in descending order based on the counts
counts_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# 3: Slice the first k elements to build the result list
sorted_counts = dict(counts_list[:k])

print([num for num in sorted_counts])
