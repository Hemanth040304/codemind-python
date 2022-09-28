n,k = map(int,input().split())
arr = list(map(int,input().split()))
c = 0
x = 0
for i in range(n):
    if arr[i]>k and x==1:
        break
    elif arr[i]>k:
        x+=1
    else:
        c+=1
print(c)