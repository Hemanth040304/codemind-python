n = int(input())
x = 1
c=0
while x<=n//2:
    if n%x==0:
        c+=1
    x+=1
if c==1:
    print("prime")
else:
    print("not a prime")