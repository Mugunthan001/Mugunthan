num=int(input())
if(num==0):
  for prod in range(0,5):
    print(0,end=" ")
else:
  for prod in range(1,6):
    print(prod*num,end=" ")
