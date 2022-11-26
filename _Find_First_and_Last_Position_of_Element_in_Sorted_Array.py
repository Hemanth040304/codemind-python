n = int(input())
arr = list(map(int,input().split()))
k = int(input())
f,s = -1,-1
for i in range(n):
    if arr[i]==k and f==-1:
        f = i
        s = i
    elif arr[i]==k and f!=-1:
        s = i
print(f,s)