n = int(input())
arr = list(map(int,input().split()))
k = int(input())
a = []
for i in range(n):
    if arr.count(arr[i])==k and arr[i] not in a:
        a.append(arr[i])
if len(a)==0:
    print("-1")
else:
    print(*a)