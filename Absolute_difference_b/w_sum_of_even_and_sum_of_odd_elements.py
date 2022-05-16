n = int(input())
arr = list(map(int,input().split()))
ev = 0
od = 0
for i in range(0,n):
    if arr[i]%2==0:
        ev+=arr[i]
    else:
        od+=arr[i]
if ev>od:
    print(ev-od)
else:
    print(od-ev)