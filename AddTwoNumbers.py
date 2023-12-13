# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
import numpy as np
l1 = [2,4,3]
l2 = [5,6,4]
# ans=""
# for i in range(len(l1)):
#     ans = ans+str(l1[i]+l2[i])
    
# print(ans)

sum = [x + y for (x, y) in zip(l1, l2)] 
print(sum)