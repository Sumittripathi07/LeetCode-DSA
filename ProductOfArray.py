# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


# nums = [1,2,3,4]
# ans=[]
# x=1
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i!=j:
#             x*=nums[j]  
#     ans.append(x)
#     x=1
# print(ans)


nums = [1,2,3,4]
x = []
ans=1
for i in range(len(nums)):
    ans = ans * nums[i]
for j in range(len(nums)):
    a=int(ans/nums[j])
    x.append(a)
print(x) 
