#M
num1,num2=map(int,input().split())
list1=list(map(int,input().split()))
num1=[]
list1.insert(0,0)
for y in range(num2):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list1[i]     
     num1.append(s)
for y in num1:
     print(y)
