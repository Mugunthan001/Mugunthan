#M
stng1,stng2=input().split()
char=abs(len(stng2)-len(stng1))
for g in range(len(stng1)):
  if(len(stng2)==1 and stng2[g] in stng1):
    break
  if(stng1[g]!=stng2[g]):
    char=char+1
print(char)
