n,m = map(int,input().split())
c = 0
b = []
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
    co = 0
    ca = 0
    for j in range(m-1):
        if a[j]<a[j+1]:
            co+=1
    for j in range(m-1):
        if a[j]>a[j+1]:
            ca+=1
    if co==m-1 or ca==m-1:
        c+=1
print(c)