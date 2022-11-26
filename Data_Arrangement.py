n = int(input())
arr = list(map(int,input().split()))
n = []
p = []
for i in arr:
    if i<0:
        print(i,end=" ")
for i in arr:
    if i>-1:
        print(i,end=" ")