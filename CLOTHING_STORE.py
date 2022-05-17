n = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(0,n):
    for j in range(0,n):
        if i!=j and arr[i]==arr[j] and arr[i]!=0 and arr[j]!=0:
            count+=1
            arr[i]=0
            arr[j]=0
print(count)