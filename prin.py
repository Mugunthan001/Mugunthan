n11,n22=input().split()
n11=int(n11)
n22=int(n22)
for i in range(n11+1,n22):
    for j in range(2,i):
         if(i%j==0):
           break
         else:
           print(i,end=" ")
