n = int(input())
arr = list(map(int,input().split()))
ans = 'NO'
for i in range(n):
    no = 0
    for j in range(n):
        if i&j:
            no += arr[j]
        else:
            no -= arr[j]
    if no%360==0:
        ans="YES"
print(ans)