#M
numl,fnum=map(int,input().split())
q=list(map(int,input().split()))
w=[]
e=[]
r=[]
s=0
for i in range(0,numl):
    if q[i]!=fnum and abs(q[i]-fnum):
        w.append(abs(q[i]-fnum))
        e.append(q.index(q[i]))
for i in range(0,3):
    s=w.index(min(w))
    r.append(q[e[s]])
    w.pop(w.index(min(w)))
    e.pop(s)
print(*r)
