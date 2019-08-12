#M
numl=int(input())
nums=list(map(int,input().split()))
nums=sorted(nums)
k=j=0
for i in range(0,numl):
    if i==0:
        k=k+1
        j=nums[i]
    else:
        if j<=nums[i]: k=k+1
        j = j + nums[i]
print(k)
