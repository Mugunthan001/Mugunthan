#M
stng=list(input())
tem=[]
for ch in stng:
    if ch not in tem:
        tem.append(ch)
if(stng==tem):
    print("Yes")
else:
    print("No")
