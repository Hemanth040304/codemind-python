def fun(n):
    x = 1
    for i in range(2,n+1):
        if n%i==0:
            x+=i
    return x

s = input().split(",")
r = []
for i in s:
    if str(fun(int(i))) in s:
        r.append(int(i))
if len(r)==0:
    print("-1")
else:
    print(*sorted(r))