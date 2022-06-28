n = int(input())
arr = list(map(int,input().split()))
count = 0
d = 0
for i in range(2,n):
    if arr[i]==arr[i-1]+arr[i-2]:
        count+=1
    else:
        d = 1
        break
if count>0 and d==0:
    print('yes')
else:
    print('no')