#M
stng=list(str(input()))
k=t=len(stng)
h=0
for i in range(0,k//2):
    i=0
    if stng[i]==stng[k-1]:
        stng.pop(i)
        stng.pop(k-2)
    else:
        h=9
        break
    k=k-2
if t%2==0 and h!=9:
    print("YES")
elif t%2!=0:
    if len(stng)==1:
        print("YES")
    else:
        print("NO")
