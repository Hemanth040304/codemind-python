n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(m):
    if b[i] in a:
        ind = a.index(b[i])
        a[ind]=0
        b[i]=0
if len(b)==b.count(0):
    print("Yes")
else:
    print("No")