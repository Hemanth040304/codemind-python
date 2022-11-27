n = int(input())
arr = list(map(int,input().split()))
ma = -100
for i in range(n):
    su = 0
    for j in range(i,n):
        su += arr[j]
        if ma<su:
            ma = su
print(ma)