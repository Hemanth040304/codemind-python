def digit(n):
    s = 0
    while n:
        s+=n%10
        n//=10
    return s

n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(n):
    s+=digit(arr[i])
print(s)