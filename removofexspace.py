#M
stng=list(input())
i=0
while i!=len(stng):
    if stng[i]==" " and stng[i+1]==" ":
        stng.pop(i+1)
    i=i+1
for i in range(len(stng)): 
    print(stng[i],end="")
