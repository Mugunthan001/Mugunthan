numl=int(input())
nelem=list(map(int,input().split()))
nelem.sort()
for se in nelem:
    print(se,end=' ')
