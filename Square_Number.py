n = int(input())
x = 1
while x*x<=n:
    if n==x*x:
        print(True)
        x=0
        break
    x+=1
if x!=0:
    print(False)