n = int(input())
arr = list(map(int,input().split()))
k = int(input())
if k>n:
    k%=n
for i in range(n-k,n):
    print(arr[i],end=" ")
for i in range(0,n-k):
    print(arr[i],end=" ")