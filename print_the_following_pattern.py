n = int(input())
for i in range(n,0,-1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+1):
        if i==1 or i==n or k==1 or k==n:
            print("*",end="")
        else:
            print(" ",end="")
    print("")