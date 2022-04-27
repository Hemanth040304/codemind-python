n = int(input())
for i in range(0,n):
    for j in range(0,n-i):
        print(j+1,end="")
    print(end="
")