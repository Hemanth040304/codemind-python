n = input()
arr = list(map(int,input().split()))
a,b = map(int,input().split())
mi = 9999
for i in arr:
    if i<a or i>b:
        if mi>i:
            mi=i
if mi==9999:
    print("-1")
else:
    print(mi)