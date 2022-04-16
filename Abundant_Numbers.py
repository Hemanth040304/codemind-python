n = int(input())
fact = 0
x = 1
while x<=n//2:
    if n%x==0:
        fact+=x
    x+=1
if fact>n:
    print(True)
else :
    print(False)