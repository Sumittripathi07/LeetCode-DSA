# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

import re

s = "ab_a"
word = re.sub(r"_\W+", "", s).lower()
# word.strip("_")
print(word)
if word == word[::-1]:
    print("True")
