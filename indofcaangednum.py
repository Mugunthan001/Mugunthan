numb=int(input())
numbs=list(map(int,input().split()))
for nu in range(len(numbs)-1):
   if(numbs[nu]>numbs[nu+1]):
      print(nu)
