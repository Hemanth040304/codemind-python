n = int(input())
count=0
arr = list(map(int,input().split()))
for i in range(n):
    c=arr.count(arr[i])
    if c==arr[i]:
        print(arr[i],end=" ")
        arr[i]=0
        count+=1
if count==0:
    print("-1")