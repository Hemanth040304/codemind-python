n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
s = 0
for i in range(n):
    if arr[i]<a or arr[i]>b:
        s+=arr[i]
print(s)