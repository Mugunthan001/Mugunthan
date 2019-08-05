#M
num1=int(input())
a=list(map(int,input().split()))
res=0
for i in range(0,num1-2):
	for j in range(1,num1-1):
		for k in range(2,num1):
			if(a[i]<a[j] and a[j]<a[k]):
				res+=1
print(res)
