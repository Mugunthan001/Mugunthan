#M
stng=list(map(str,input()))
t=""
for i in range(0,len(stng)-1,2):
    t=stng[i]
    stng[i]=stng[i+1]
    stng[i+1]=t
for i in range(0,len(stng)):
    print(stng[i],end="")
