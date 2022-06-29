n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in range(n):
    if i%2 and arr[i]%2==0:
        print(False)
        c = 1
        break
if c==0:
    print(True)