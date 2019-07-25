#M
bhav,mah=map(int,input().split())
res=list(map(int,input().split()[:mah]))
res1=[]
for i in res:
   if(i<=i+1):
     res1.append(i)
print(res1[mah-1])  
