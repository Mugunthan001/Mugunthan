#M
numl=int(input())
nums=[int(o) for o in input().split(" ")]
res=0
for p in range(numl):
      for g in range(p):
           if(nums[g]<nums[p]):
                res+=nums[g]
print(res)
