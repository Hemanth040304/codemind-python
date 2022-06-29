n = int(input())
arr = list(map(int,input().split()))
avg = sum(arr)//n
c = 0
for i in range(n):
    if avg<=arr[i]:
        c+=1
print(c)