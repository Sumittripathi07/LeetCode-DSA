# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"


word1 = "abcd"
word2 = "pq"
ans = []
i = 0
while i < len(word1) or i < len(word2):
    if i < len(word1):
        ans.append(word1[i])
    if i < len(word2):
        ans.append(word2[i])
    i += 1
ans = "".join(ans)
print(ans)
