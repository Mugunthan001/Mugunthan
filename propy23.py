#M
stng=input()
x=y=z=0
for i in range(0,len(stng)):
    if stng[i]=='G':
        x+=1
    elif stng[i]=='L':
        y+=1
    else:
        z+=1
if x%2==0 and ((y%2!=0 and (z==0 or z%2!=0)) or (z%2!=0 and (y==0 or y%2!=0))):
    print("yes")
else:
    print("no")
