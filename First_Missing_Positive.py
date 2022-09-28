n = int(input())
arr = list(map(int,input().split()))
x = 1
while True:
    if x not in arr:
        print(x)
        break
    x+=1