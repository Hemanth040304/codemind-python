n = input()
arr = list(map(int,input().split()))
a,b = map(int,input().split())
ma = -1
for i in arr:
    if i<a or i>b:
        if ma<i:
            ma=i
print(ma)