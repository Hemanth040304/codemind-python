n = int(input())
sum = 0
arr = list(map(int,input().split()))
for i in range(0,n):
    sum+=arr[i]
avg = sum/n
print("%.2f"%avg)