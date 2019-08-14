#M
numl=int(input())
l=list(map(int,input().split()))
p=0
for i in range(numl):
    for j in range(i+1,numl):
        for k in range(j+1,numl):
            if l[i]>l[j] and l[j]>l[k]:
                p=p+1
if numl==1:
    print(1)
else:
    print(p)
