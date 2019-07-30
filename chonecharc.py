#M
stng1,stng2=list(map(str,input().split()))
res=0
for i in range(0,len(stng1)):
    if stng1[i]!=stng2[i]:
        res=res+1
if res==1:
    print("yes")
else:
    print("no")
