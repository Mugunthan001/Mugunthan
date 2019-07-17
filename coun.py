d,r=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
i=0
sum=0
while r>0:
  sum+=arr[i]
  r=r-1
  i=i+1
print(sum)
