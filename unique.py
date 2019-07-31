#M
numl=int(input())
nums=list(map(int,input().split()))
r=[]
for i in range(0,numl-1):
    for j in range(i+1,numl):
        if nums[i]==nums[j]:
            r.append(nums[i])
x=list(set(sorted(r)))
if len(x)==0:
    print("unique")
else:
    for i in range(0,len(x)):
        print(x[i],end=" ")
