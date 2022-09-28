n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(n-1):
    if arr[i+1]>arr[i]:
        s += arr[i+1]-arr[i]
print(s)