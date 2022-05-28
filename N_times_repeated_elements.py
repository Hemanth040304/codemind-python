n = int(input())
arr = list(map(int,input().split()))
t = int(input())
count = 0
for i in range(n):
    c=arr.count(arr[i])
    if c==t:
        print(arr[i],end=" ")
        arr[i]=0
        count+=1
if count==0:
    print("-1")