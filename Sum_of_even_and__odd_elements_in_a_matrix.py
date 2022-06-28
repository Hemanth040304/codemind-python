n,m = map(int,input().split())
b = []
e,o = 0,0
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
for i in range(n):
    for j in range(m):
        if b[i][j]%2==0:
            e+=b[i][j]
        else:
            o+=b[i][j]
print(e,o)