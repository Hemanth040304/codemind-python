t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    c = 0
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(arr)-min(arr))
    t-=1