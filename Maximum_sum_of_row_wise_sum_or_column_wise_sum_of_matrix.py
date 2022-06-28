n,m = map(int,input().split())
b = []
x = 0
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
    if sum(a)>x:
        x=sum(a)
for i in range(n):
    s = 0
    for j in range(m):
        s+=b[i][j]
    if s>x:
        x=s
print(x)