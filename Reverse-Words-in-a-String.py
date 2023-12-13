# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.


s = "  hello world  "
s = s.strip().split()[::-1]
result = " ".join(s)
print(result)
