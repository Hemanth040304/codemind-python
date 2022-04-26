n = int(input())
x=2
c=0
d=0
p=0
while x<=n//2:
    if n%x==0:
        c+=1
    x+=1
if c!=0:
    print("Not Mega Prime")
else:
    while n:
        if n%10==2 or n%10==3 or n%10==5 or n%10==7:
            c+=1
        d+=1
        n//=10
    if c==d:
        print("Mega Prime")
    else:
        print("Not Mega Prime")