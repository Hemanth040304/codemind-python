t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    c = 1
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            c+=1
    print(c)
    t-=1