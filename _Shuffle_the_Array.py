n = int(input())
arr = list(map(int,input().split()))
y = int(input())
for i in range(0,y):
    print(arr[i],arr[y],end=" ")
    y+=1