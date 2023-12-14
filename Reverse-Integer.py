# Example 1:
# Input: x = -123
# Output: -321

# Example 2:
# Input: x = 120
# Output: 21

# Example 3
# Input : x = 1563847412
# Output: 0 #Because answer of this reverse value is more then 32bit


x = 1563847412
if x >= 0:
    ans = int(str(x)[::-1])
    if ans.bit_length() >= 32:
        print(0)
    else:
        print(ans)

else:
    num = str(abs(x))[::-1]
    ans = int("-" + num)
    if ans.bit_length() >= 32:
        print(0)
    else:
        print(ans)
