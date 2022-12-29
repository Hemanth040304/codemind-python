arr = list(map(int,input().split()))
s = []
for i in arr:
    s.append(i*i)
s.sort()
print(*s)