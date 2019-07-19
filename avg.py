numl=int(input())
nums=list(map(int,input().split()))
tem=0
div=len(nums)
for i in range(numl):
    tem+=nums[i]
res=tem//div
print(res)
