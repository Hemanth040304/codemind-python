t = int(input())
while t:
    n , m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append(a[i])
    for i in range(m):
        c.append(b[i])
    print(*sorted(c))
    t-=1