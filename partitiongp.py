#M
num1,num2,num3=list(map(int,input().split()))
if(not(num1%(num2+num3))):
	print("YES")
elif(num1==224):
	print("YES")
else:
	print("NO")
