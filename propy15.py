#M
numb=input()
arry=map(int,input().split())
sin=[]
for i in arry:
    eat=bin(i)
    sin.append(eat)
fine=sorted(sin)
fine.reverse()
for j in fine:
    print(int(j,2))
