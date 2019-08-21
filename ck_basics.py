#M
n,k=map(int,input().split())
lis=list(map(int,input().split()))
c=0
for i in range(0,n):
	if(lis[i]==k):
		c=c+1
print(c)
