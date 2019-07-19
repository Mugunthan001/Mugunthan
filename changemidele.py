stng=list(input())
size=len(stng)
if size%2==0:
	dig=size//2
	stng[dig-1]=stng[dig]='*'
else:
	dig=size//2
	stng[dig]='*'
print(*stng,sep="")
