n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in sorted(set(arr),key=arr.index):
    if arr.count(i)==i:
        print(i,end=" ")
        c = 1
if c==0:
    print("-1")