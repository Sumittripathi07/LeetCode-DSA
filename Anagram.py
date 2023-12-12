# Input: s = "anagram", t = "nagaram"
# Output: true

s = "anagram"
t = "nagaram"

newS=''.join(sorted(s))
newT=''.join(sorted(t))

if newS==newT:
    print("true")
else:
    print("false")