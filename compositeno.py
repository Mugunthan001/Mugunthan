numb=int(input())
flagco=0
if(numb>2):
    for i in range(2,int(numb/2)+1):
        if numb%i==0:
            print("yes")
            flagco=1
            break
if flagco==0 or numb==2:
    print("no")
