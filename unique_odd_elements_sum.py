n = int(input())
arr = list(map(int,input().split()))
arr = set(arr)
arr = list(arr)
s = 0
for i in range(len(arr)):
    if arr[i]%2 :
        s+=arr[i]
print(s)