n = int(input())
arr = list(map(int,input().split()))
ma = max(arr)
m = len(str(ma))
count = 0
for i in range(n):
    if len(str(arr[i]))==m:
        count += 1
print(count)