#M
num=int(input())
nums=[int(i) for i in input().split()]
t=m=k=0
for i in range(0,num):
    if i==0:
        if nums[i]>nums[i+1]:
            k=2
        else:
            k=1
        m=k
    else:
        if nums[i-1]<nums[i]:
            k=m+1
            m=k
        else:
            k=1
            m=k
    t=t+k
print(t)
