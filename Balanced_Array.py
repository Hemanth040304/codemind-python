t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(0,n):
        if sum(arr[0:i])==sum(arr[i+1:]):
            print("YES")
            break
    else:
        print("NO")
    t-=1