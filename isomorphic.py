#M
stng1,stng2=list(map(str,input().split()))
lg1=len(set(stng1)) 
lg2=len(set(stng2))
if lg1==lg2:
	print ("yes") 
else:
	print ("no") 
