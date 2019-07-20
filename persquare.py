num1,num2=input().split()
num1=int(num1)
num2=int(num2)
res=num1*num2
for i in range(0,res+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
