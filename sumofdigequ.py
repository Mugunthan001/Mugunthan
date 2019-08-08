#M
num1,num2=map(int,input().split())
j=u=0
x=list(map(int,input().split()))
for i in range(0,num1-1):
    for y in range(i+1,num1):
        j=x[i]+x[y]
        if j==num2:
            u=1
            print("yes")
if u==0: 
    print("no")
