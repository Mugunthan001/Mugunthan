#M
import sys,string
numl = int(input())
L = [ int(x) for x in input().split()]
numl = len(L)
cnt = 0
for i in range(0,numl-2) :
    for j in range(i+1, numl-1):
        for k in range(j+1, numl):
            if L[i] > L[j] > L[k] :
                cnt += 1
print(cnt)
