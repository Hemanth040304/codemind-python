a = int(input())
arr = list(map(int,input().split()))
b = int(input())
brr = list(map(int,input().split()))
c = []
for i in range(a):
    c.insert(brr[i],arr[i])
print(*c)