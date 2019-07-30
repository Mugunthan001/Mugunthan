#M
stng=input()
p=(sorted(stng))
q=list(set(stng))
ma=[]
s=0
for i in range(0,len(q)):
    ma.append(stng.count(q[i]))
s=ma.index(max(ma))
print(q[s])
