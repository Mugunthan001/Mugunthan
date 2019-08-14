#M
import sys, string, math
n1,n2 = input().split()
n1,n2 = int(n1),int(n2)
L = [ int(x) for x in input().split()]
L.sort()
cnt = 0
a = n1 // 3
for i in range(0,a) :
    L2 = L[3*i : 3*(i+1)]
    if 5-max(L2) >= n2 :
        cnt += 1
print(cnt)
