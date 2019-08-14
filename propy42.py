#M
import sys,string
def maxOfSegmentMins(L, n1, n2):
    if n2 == 1:
        return min(L)
    if n2 == 2 :
        return max(L[0], L[n1 - 1])
    return max(L)
n1,n2 = input().split()
n1,n2 = int(n1),int(n2)
L = [ int(x) for x in input().split()]
n1 = len(L)
ans = maxOfSegmentMins(L, n1, n2)
print(ans)
