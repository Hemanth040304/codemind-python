n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)//n
if avg in arr:
    print(True)
else:
    print(False)