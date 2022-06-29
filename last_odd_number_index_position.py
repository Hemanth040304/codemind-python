n = int(input())
arr = list(map(int,input().split()))
ind = 0
for i in range(n):
    if arr[i]%2:
        ind = i
print(ind)