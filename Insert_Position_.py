for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.append(k)
    arr.sort()
    c = -1
    for i in range(n):
        if arr[i]==k:
            c=i
    if c!=-1:
        print(c)
    else:
        print(n)