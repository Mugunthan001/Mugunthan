#M
num1,num2=map(int,input().split())
prod=num1*num2
m=[]
for i in range(1,prod+1):
    if i%num1==0 and i%num2==0:
        m.append(i)
print(min(m))
