a,b = map(int,input().split())
while b>a:
    b=b&b-1
print(a&b)
