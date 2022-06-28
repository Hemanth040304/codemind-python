n,m = map(int,input().split())
b = []
e = 0
o = 0
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
    if i%2==0:
        e+=sum(a)
    else:
        o+=sum(a)
print(e,o)