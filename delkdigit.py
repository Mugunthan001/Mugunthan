#M
from itertools import combinations
dig,num=map(int,input().split())
a=len(str(dig))
lst=list(combinations(str(dig),a-num))
lst=sorted(lst)
print(*lst[0],sep='')
