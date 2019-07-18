numb=int(input())
c=0
for i in range(1,numb+1):
	if(numb%i==0):
		c+=1
if(c==2):
	print("yes")
else:
	print("no")
