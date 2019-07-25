num1,num2,num3=map(int,input().split())
res=0
for i in range(0,num3):
   res=res+num1
   num1=num1+num2
print(res)
