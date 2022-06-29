n = int(input())
arr = list(map(int,input().split()))
k = int(input())
s = 0
for i in range(n):
    if arr[i]<=k:
        s+=arr[i]
print(s)