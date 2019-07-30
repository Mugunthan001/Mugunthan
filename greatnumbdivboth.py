#M
num1,num2=map(int,input().split())
s=0
for i in range(1,max(num1,num2)+1):
    if num1%i==0 and num2%i==0: s=i
print(s)
