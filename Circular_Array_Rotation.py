n,k,q = map(int,input().split())
arr = list(map(int,input().split()))
b = []
if k>n:
    k%=n
for i in range(n-k,n):
    b.append(arr[i])
for i in range(0,n-k):
    b.append(arr[i])
while q:
    x = int(input())
    print(b[x])
    q-=1