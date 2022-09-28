n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(*(arr[k:]+arr[:k]))