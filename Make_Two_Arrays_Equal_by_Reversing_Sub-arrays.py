n = int(input())
arr = list(map(int,input().split()))
m = int(input())
brr = list(map(int,input().split()))
count = 0
for i in range(0,n):
    if arr[i] in brr:
        count+=1
if count==n and count==m:
    print(True)
else:
    print(False)