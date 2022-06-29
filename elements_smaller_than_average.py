n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)/n
c = 0
for i in range(n):
    if arr[i]<=avg:
        c+=1
print(c)