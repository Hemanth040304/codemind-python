def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1

n = int(input())
arr = list(map(int,input().split()))
ma = arr.index(max(arr))
mi = arr.index(min(arr))
count = 0
if mi<ma:
    for i in range(mi,ma+1):
        if prime(arr[i]):
            count+=1
    print(count)
else:
    for i in range(ma,mi+1):
        if prime(arr[i]):
            count+=1
    print(count)