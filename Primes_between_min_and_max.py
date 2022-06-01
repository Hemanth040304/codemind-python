def isprime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
c = 0
n = int(input())
arr = list(map(int,input().split()))
mi=min(arr)
mini=arr.index(mi)
ma=max(arr)
maxi=arr.index(ma)
if mini>maxi:
    for i in range(maxi,mini+1):
        if isprime(arr[i]):
            c+=1
    print(c)
else:
    for i in range(mini,maxi+1):
        if isprime(arr[i]):
            c+=1
    print(c)