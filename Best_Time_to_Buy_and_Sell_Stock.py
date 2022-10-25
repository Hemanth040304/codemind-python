n = int(input())
arr = list(map(int,input().split()))
mi,ma =0,0
for i in range(0,n):
    for j in range(i+1,n):
        mi = arr[j]-arr[i]
        if mi > ma:
            ma = mi
print(ma)