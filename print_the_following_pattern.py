n = int(input())
x = 1
for i in range(0,n):
    for j in range(n-1,i,-1):
        print(" ",end='')
    for k in range(x):
        print(x-i,end="")
    print("")
    x += 2