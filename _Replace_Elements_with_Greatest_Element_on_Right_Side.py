n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n):
    m = -1
    for j in range(i+1,n):
        if m<arr[j]:
            m=arr[j]
    arr[i]=m
print(*arr)