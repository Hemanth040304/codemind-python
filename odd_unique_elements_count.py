n = int(input())
arr = list(map(int,input().split()))
c = 0
arr = set(arr)
arr = list(arr)
for i in range(len(arr)):
    if arr[i]%2:
        c+=1
print(c)