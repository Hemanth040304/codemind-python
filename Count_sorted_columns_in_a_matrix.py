n,m = map(int,input().split())
c = 0
b = []
for i in range(m):
    b.append([])
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        b[j].append(a[j])
for i in b:
    p=i.copy()
    p.sort()
    q = p[::-1]
    if i==p or i==q:
        c+=1
print(c)