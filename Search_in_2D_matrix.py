n,m = map(int,input().split())
arr = []
c = 0
for i in range(n):
    b = list(map(int,input().split()))
    arr.append(b)
k = int(input())
for i in range(n):
    for j in range(m):
        if arr[i][j]==k:
            c=1
            break
if c==0:
    print("false")
else:
    print("true")