n11,n22=input().split()
n11=int(n11)
n22=int(n22)
for num1 in range(n11,n22):
  sum=0
  temp=num1
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==num1):
     print(num1,end=" ")
