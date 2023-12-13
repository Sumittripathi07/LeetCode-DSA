# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.


s = "   fly me   to   the moon  "
x = s.strip().split()
print(len(x[-1]))
