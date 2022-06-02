n = input()
n = n.split(" ")
for i in range(len(n)):
    if i%2==0:
        for j in range(len(n[i])-1,-1,-1):
            print(n[i][j],end="")
    else:
        for j in range(len(n[i])):
            print(n[i][j],end="")
    print(end=" ")