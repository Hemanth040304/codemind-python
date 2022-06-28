n,m = map(int,input().split())
b = []
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
    print(sum(a),end=" ")