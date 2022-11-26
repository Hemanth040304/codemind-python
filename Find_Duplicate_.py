for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in set(arr):
        if arr.count(i)>1:
            print(i)
            break