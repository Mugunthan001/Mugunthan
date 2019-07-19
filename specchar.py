giv=str(input())
count=0
for i in giv:
    if i.isnumeric() or i.isalpha():
        pass
    else:
        count+=1
print(count)
