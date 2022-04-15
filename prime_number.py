n = int(input())
i=1
x=0
while i<=n/2 :
    if n%i==0:
        x+=1
    i+=1
    
if x==1:
    print("prime")
else:
    print("not a prime")