n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
c = 0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        if arr[i]>c:
            c=arr[i]
if c == 0:
    print("-1")
else:
    print(c)