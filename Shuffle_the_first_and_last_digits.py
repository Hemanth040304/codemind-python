a = list(map(int,input().split()))
print(a[len(a)-1],end=" ")
print(*a[1:-1],end=" ")
print(a[0])