n = int(input())
x = 1
c=0
while x*x<=n:
    if x*x==n:
        c+=1
        print(True)
        break
    x+=1
if c==0:
    print(False)