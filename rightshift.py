#M
num1,num2=map(int,input().split())
tem=[]
l=list(map(int,input().split()))
tem=(l[-num2:]+l[:-num2])
for i in range(0,len(tem)):
	print(tem[i],end=" ")
