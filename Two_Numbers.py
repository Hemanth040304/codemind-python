n = int(input())
arr = list(map(int,input().split()))
arr.sort()
for i in range(0,n):
    if arr.count(arr[i])==1:
        print(arr[i],end=" ")