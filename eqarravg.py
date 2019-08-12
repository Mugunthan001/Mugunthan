#M
numl=int(input())
nums=list(map(int,input().split()))
x=y=u=k=0
for i in range(0,numl-1):
    if i==0:
        x=(x+nums[i])/(i+1)
    else:
        x=0
        for t in range(0,i):
            x=x+nums[t]
        x = (x + nums[i]) // (i + 1)
    k=0
    for j in range(i+1,numl):
        y=y+nums[j]
        k=k+1
        if j==numl-1:
            y=y//(k)
    if x==y:
        u=1
        print("yes")
if u==0:
    print("no")
