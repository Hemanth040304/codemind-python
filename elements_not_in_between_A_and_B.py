n = int(input())
arr = list(map(int,input().split()))
a, b = map(int,input().split())
c = 0
for i in range(n):
    if arr[i]<a or arr[i]>b:
        print(arr[i],end=" ")
        c = 1
if c==0:
    print("-1")