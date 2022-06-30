n = int(input())
arr = list(map(int,input().split()))
a = []
for i in range(n):
    if arr[i] not in a:
        a.append(arr[i])
print(*a)