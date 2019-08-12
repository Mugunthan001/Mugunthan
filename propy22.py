#M
numl=int(input())
nums=list(map(int,input().split()))
q=[]
for i in range(0,numl):
    for j in range(i+1,numl-1,1):
        s=0
        for k in range(j+1,numl,2):
            s=s+nums[k]
        s=s+nums[i]
        q.append(s)
print(max(q))
