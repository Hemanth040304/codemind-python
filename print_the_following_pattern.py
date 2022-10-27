n = int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for l in range(i+1):
        print(l,end="")
    print("")