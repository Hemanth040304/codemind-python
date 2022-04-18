n = int(input())
x=0
c=0
while x*(x+1)<=n:
    if x*(x+1)==n:
        print("YES")
        c+=1
        break
    x+=1
if c==0:
    print("NO")