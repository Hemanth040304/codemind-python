test = int(input())
while test:
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(0,n):
                if arr[i]+arr[j]==arr[k] and k!=j:
                    count+=1
    if count==0:
        print("-1")
    else:
        print(count)
    test-=1