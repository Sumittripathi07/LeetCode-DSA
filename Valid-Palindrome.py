# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
x = ""
for i in s:
    if i.isalnum():
        x = x + i
print(x)
x = x.lower()
print(x)
if x == x[::-1]:
    print(True)
else:
    print(False)
