t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    x,y = 0,n-1
    a = []
    while(y>=x):
        if y==x:
            a.append(arr[y])
        else:
            a.append(arr[y])
            a.append(arr[x])
        y-=1
        x+=1
    print(*a)
    t-=1