n,m = map(int,input().split())
c = 0
for i in range(n):
    b = list(map(int,input().split()))
    for j in b:
        if j < 0:
            c+=1
print(c)