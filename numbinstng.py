stng=input()
res=[]
for ch in stng:
    if(ch.isnumeric()):
        res.append(ch)
print(''.join(res))
