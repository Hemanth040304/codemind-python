n = int(input())
arr = list(map(int,input().split()))
z = arr.count(0)
o = arr.count(1)
if z+o==n:
    print(True)
else:
    print(False)