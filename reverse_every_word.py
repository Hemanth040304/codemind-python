n = input()
n = n.split(" ")
for j in range(len(n)):
    for i in range(len(n[j])-1,-1,-1):
        print(n[j][i],end="")
    print(end=" ")