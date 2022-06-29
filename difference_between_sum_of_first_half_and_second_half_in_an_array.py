n = int(input())
arr = list(map(int,input().split()))
f,s = 0,0
f = sum(arr[:n//2])
s = sum(arr[n//2:])
print(abs(f-s))