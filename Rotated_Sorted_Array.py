n ,k = map(int,input().split())
arr = list(map(int,input().split()))
if k in arr:
    print(arr.index(k))
else:
    print("-1")