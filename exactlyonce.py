#M
numl=int(input())
nums=list(map(int,input().split()))
nums=sorted(nums)
nums=nums[::-1]
q=0
for i in range(numl):
   q=int(str(q)+str(nums[i]))
print(q)
