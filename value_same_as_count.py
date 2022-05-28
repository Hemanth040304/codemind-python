n = int(input())
count=0
arr = list(map(int,input().split()))
for i in range(n):
    c=arr.count(arr[i])
    if c==arr[i]:
        count+=1
        arr[i]=0
print(count)