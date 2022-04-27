n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("0",end="")
        else:
            print("x",end="")
    print(end="
")