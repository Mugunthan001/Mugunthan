#M
numl=int(input ()) 
nums=list(map(int, input ().split()))
x=[]
for i in range(0,numl):
	if i==nums[i]:
		x.append(i)
for i in range(0,len(x)):
	print(x[i],end=" ")
if len(x)==0:
	print("-1")
