n = int(input())
arr = list(map(int,input().split()))
a = []
for i in range(0,n,2):
    while arr[i]:
        arr[i]-=1
        print(arr[i+1],end=" ")