n = int(input())
arr = list(map(int,input().split()))
arr = set(arr)
arr = list(arr)
c = 0
for i in range(len(arr)):
    if arr[i]%2==0:
        c+=1
print(c)