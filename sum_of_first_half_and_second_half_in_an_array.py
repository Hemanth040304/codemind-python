n=int(input())
arr = list(map(int,input().split()))
print(sum(arr[:n//2]))
print(sum(arr[n//2:]))