n = int(input())
arr = list(map(int,input().split()))
s = 0
x = 0
for i in range(n-1,-1,-1):
    s+=arr[i]*(2**x)
    x+=1
print(s)