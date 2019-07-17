d,n=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
i=0
sum=0
while (n>0):
  sum+=arr[i]
  n=n-1
  i=i+1
print(sum)
