a = int(input())
b = int(input())
x = 0
n = 1
while n<=a//2:
    if a%n==0:
        x+=n
    n+=1
if x==b:
    n=1
    x=0
    while n<=b//2:
        if b%n==0:
            x+=n 
        n+=1
if x==a:
    print("Amicable")
else :
    print("Not Amicable")