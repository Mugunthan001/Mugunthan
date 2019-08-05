#M
cst1,cst2=map(str,input().split())
yas=0
if len(cst1)>len(cst2):
  cst1,cst2=cst2,cst1
p=0
while p<len(cst1):
  yas+=(ord(cst2[p])-ord(cst1[p]))
  p+=1
for p in range(p,len(cst2)):
  yas+=ord(cst2[p])-ord('a')+1
print(yas)
